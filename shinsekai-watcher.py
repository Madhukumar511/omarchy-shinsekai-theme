#!/usr/bin/env python3
import os, time, subprocess, sys, select, ctypes, json, random, datetime, colorsys, re

# Zero CPU inotify event-driven watcher & background service manager
SCRIPT = os.path.expanduser("~/.config/omarchy/themes/shinsekai/dynamic-theme.py")
BG_LINK = os.path.expanduser("~/.local/state/omarchy/current/background")
THEME_NAME_FILE = os.path.expanduser("~/.local/state/omarchy/current/theme.name")
WATCH_DIR = os.path.expanduser("~/.local/state/omarchy/current")
CONFIG_FILE = os.path.expanduser("~/.config/omarchy/themes/shinsekai/.config.json")
BG_DIR = os.path.expanduser("~/.config/omarchy/themes/shinsekai/backgrounds")

last_target = ""
last_time_slot = ""
was_shinsekai_active = True
classification_cache = {}

def is_shinsekai_active():
    if os.path.exists(THEME_NAME_FILE):
        try:
            with open(THEME_NAME_FILE, "r") as f:
                return f.read().strip().lower() == "shinsekai"
        except Exception:
            pass
    return False

def get_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except Exception:
            pass
    return {"auto_cycle": False, "audio_reactive": False}

def classify_wallpaper_time_slot(filename):
    if filename in classification_cache:
        return classification_cache[filename]
        
    path = os.path.join(BG_DIR, filename)
    if not os.path.exists(path):
        return "day"
        
    try:
        cmd = f'magick "{path}" -resize 24x24! -format "%c" histogram:info:'
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=2).stdout
        total_pixels = 0
        total_lum = 0
        warm_sunset_weight = 0

        for line in res.strip().split('\n'):
            if not line or ':' not in line: continue
            parts = line.split(':')
            count = int(parts[0].strip())
            m = re.search(r'#([0-9a-fA-F]{6})', parts[1])
            if not m: continue
            hex_val = m.group(1)
            r = int(hex_val[0:2], 16) / 255.0
            g = int(hex_val[2:4], 16) / 255.0
            b = int(hex_val[4:6], 16) / 255.0
            h, s, v = colorsys.rgb_to_hsv(r, g, b)
            lum = 0.2126 * r + 0.7152 * g + 0.0722 * b
            total_pixels += count
            total_lum += lum * count

            h_deg = h * 360
            if (10 <= h_deg <= 55 or 320 <= h_deg <= 360) and s > 0.30 and 0.20 <= v <= 0.85:
                warm_sunset_weight += count * s * v

        avg_lum = total_lum / max(total_pixels, 1)
        sunset_score = warm_sunset_weight / max(total_pixels, 1)

        fn_lower = filename.lower()
        if sunset_score > 0.12 or "sunset" in fn_lower or "horizon" in fn_lower or "twilight" in fn_lower:
            slot = "sunset"
        elif avg_lum >= 0.40:
            slot = "day"
        else:
            slot = "night"
    except Exception:
        slot = "day"

    classification_cache[filename] = slot
    return slot

def get_dynamic_time_slot_pools():
    if not os.path.exists(BG_DIR):
        return {"day": [], "sunset": [], "night": []}
        
    all_wallpapers = sorted([f for f in os.listdir(BG_DIR) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))])
    
    pools = {"day": [], "sunset": [], "night": []}
    for f in all_wallpapers:
        slot = classify_wallpaper_time_slot(f)
        pools[slot].append(f)
        
    # If any slot is empty, fall back to all wallpapers so cycle never breaks
    for k in pools:
        if not pools[k] and all_wallpapers:
            pools[k] = all_wallpapers
            
    return pools

def sync_theme():
    global last_target, was_shinsekai_active
    active = is_shinsekai_active()

    if not active:
        if was_shinsekai_active:
            print("[Shinsekai Event] Switched away from Shinsekai theme. Deactivating all Shinsekai effects.", flush=True)
            was_shinsekai_active = False
            last_target = ""
            subprocess.run(["hyprctl", "reload"], capture_output=True)
        return

    if not was_shinsekai_active:
        print("[Shinsekai Event] Shinsekai theme activated. Re-applying dynamic theme.", flush=True)
        was_shinsekai_active = True
        last_target = ""

    if os.path.exists(BG_LINK):
        try:
            target = os.path.realpath(BG_LINK)
            if target != last_target:
                last_target = target
                print(f"[Shinsekai Event] Wallpaper changed: {os.path.basename(target)}", flush=True)
                subprocess.run([sys.executable, SCRIPT, target])
        except Exception as e:
            print(f"[Shinsekai Error] {e}", flush=True)

def check_time_of_day_cycle():
    global last_time_slot
    if not is_shinsekai_active():
        return
        
    cfg = get_config()
    if not cfg.get("auto_cycle", False):
        return
        
    hour = datetime.datetime.now().hour
    if 7 <= hour < 17:
        current_slot = "day"
    elif 17 <= hour < 20:
        current_slot = "sunset"
    else:
        current_slot = "night"
        
    if current_slot != last_time_slot:
        last_time_slot = current_slot
        pools = get_dynamic_time_slot_pools()
        pool = pools.get(current_slot, [])
        if pool:
            chosen = random.choice(pool)
            target_path = os.path.join(BG_DIR, chosen)
            print(f"[Shinsekai Auto-Cycle] Dynamic Classification -> Time of day ({current_slot.upper()} {hour:02d}:00) matched: {chosen}", flush=True)
            subprocess.run(f'omarchy theme bg set "{target_path}"', shell=True)
            subprocess.run([sys.executable, SCRIPT, target_path])

# Run once on startup if active
sync_theme()
check_time_of_day_cycle()

# Inotify syscall setup
libc = ctypes.CDLL("libc.so.6", use_errno=True)
IN_MODIFY = 0x00000002
IN_ATTRIB = 0x00000004
IN_CLOSE_WRITE = 0x00000008
IN_MOVED_TO = 0x00000080
IN_CREATE = 0x00000100
IN_DELETE = 0x00000200

inotify_fd = libc.inotify_init1(0x00080000)
if inotify_fd >= 0:
    watch_flags = IN_MODIFY | IN_ATTRIB | IN_CLOSE_WRITE | IN_MOVED_TO | IN_CREATE | IN_DELETE
    wd = libc.inotify_add_watch(inotify_fd, WATCH_DIR.encode('utf-8'), watch_flags)
    
    poll_obj = select.poll()
    poll_obj.register(inotify_fd, select.POLLIN)
    
    last_cycle_check = time.time()
    
    while True:
        try:
            # Poll with 30s timeout so we can also check time-of-day clock at 0% CPU
            events = poll_obj.poll(30000)
            if events:
                os.read(inotify_fd, 4096)
                time.sleep(0.15)
                sync_theme()
                
            # Check time-of-day cycle every 5 minutes
            if time.time() - last_cycle_check >= 300:
                last_cycle_check = time.time()
                check_time_of_day_cycle()
        except Exception:
            time.sleep(2)
            sync_theme()
else:
    while True:
        time.sleep(2)
        sync_theme()
