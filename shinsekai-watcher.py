#!/usr/bin/env python3
import os, time, subprocess, sys, select, ctypes, json, random, datetime

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

TIME_SLOTS = {
    "day": ["01-asuna-meadow-nature.png", "02-mitsuha-lake-nature.png", "04-frieren-field-4k.png", "05-violet-evergarden-8k.jpg", "08-weathering-with-you-8k.jpg"],
    "sunset": ["06-spirited-away-train-4k.jpg", "12-anime-sunset-horizon-4k.jpg", "09-wuthering-waves-chisa-4k.jpg"],
    "night": ["03-columbina-snow-8k.jpg", "07-suzume-door-starry-4k.jpg", "10-edgerunners-moon-4k.jpg", "11-demon-slayer-wisteria-4k.jpg", "13-lord-of-mysteries-4k.jpg"]
}

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
        pool = TIME_SLOTS.get(current_slot, [])
        existing = [f for f in pool if os.path.exists(os.path.join(BG_DIR, f))]
        if existing:
            chosen = random.choice(existing)
            target_path = os.path.join(BG_DIR, chosen)
            print(f"[Shinsekai Auto-Cycle] Time of day ({current_slot.upper()} {hour:02d}:00) -> {chosen}", flush=True)
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
