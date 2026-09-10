#!/usr/bin/env python3
import subprocess, time, os, re, sys, json

CONFIG_FILE = os.path.expanduser("~/.config/omarchy/themes/shinsekai/.config.json")
THEME_NAME_FILE = os.path.expanduser("~/.local/state/omarchy/current/theme.name")
COLORS_FILE = os.path.expanduser("~/.local/state/omarchy/current/theme/colors.toml")

def is_shinsekai_active():
    if os.path.exists(THEME_NAME_FILE):
        try:
            with open(THEME_NAME_FILE, "r") as f:
                return f.read().strip().lower() == "shinsekai"
        except Exception:
            pass
    return False

_cached_colors = ("#eed132", "#55e064")
_last_mtime = 0

def get_theme_colors():
    global _cached_colors, _last_mtime
    candidates = [
        os.path.expanduser("~/.local/state/omarchy/current/theme/colors.toml"),
        os.path.expanduser("~/.config/omarchy/themes/shinsekai/colors.toml"),
    ]
    
    target_file = None
    for path in candidates:
        if os.path.exists(path) and os.path.getsize(path) > 0:
            target_file = path
            break
            
    if not target_file:
        return _cached_colors
        
    try:
        mtime = os.path.getmtime(target_file)
        if mtime == _last_mtime:
            return _cached_colors
            
        with open(target_file, "r") as f:
            content = f.read()
            
        p_hex, s_hex = None, None
        
        # Check hyprland_active_border first
        m_border = re.search(r'hyprland_active_border\s*=\s*\"(#[0-9a-fA-F]{6})\s+(#[0-9a-fA-F]{6})', content)
        if m_border:
            p_hex = m_border.group(1)
            s_hex = m_border.group(2)
        else:
            m_acc = re.search(r'accent\s*=\s*\"(#[0-9a-fA-F]{6})\"', content)
            m_cur = re.search(r'cursor\s*=\s*\"(#[0-9a-fA-F]{6})\"', content)
            if m_acc: p_hex = m_acc.group(1)
            if m_cur: s_hex = m_cur.group(1)
            
        if p_hex and s_hex:
            _cached_colors = (p_hex, s_hex)
            _last_mtime = mtime
    except Exception:
        pass
        
    return _cached_colors

def is_pulse_enabled():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                data = json.load(f)
                return data.get("audio_reactive", False)
        except Exception:
            pass
    return False

def reset_border():
    if not is_shinsekai_active():
        subprocess.run(["hyprctl", "reload"], capture_output=True)
        return
    p_hex, s_hex = get_theme_colors()
    pr, pg, pb = int(p_hex[1:3], 16), int(p_hex[3:5], 16), int(p_hex[5:7], 16)
    sr, sg, sb = int(s_hex[1:3], 16), int(s_hex[3:5], 16), int(s_hex[5:7], 16)
    lua_code = f'hl.config({{ general = {{ col = {{ active_border = {{ colors = {{ "rgba({pr:02x}{pg:02x}{pb:02x}ee)", "rgba({sr:02x}{sg:02x}{sb:02x}ee)" }}, angle = 45 }} }} }} }})'
    subprocess.run(["hyprctl", "eval", lua_code], capture_output=True)

def is_audio_playing():
    try:
        res = subprocess.run(["wpctl", "status"], capture_output=True, text=True, timeout=1).stdout
        audio_sec = res.split("Video")[0] if "Video" in res else res
        return "[active]" in audio_sec or "[running]" in audio_sec
    except Exception:
        return False

def run_pulse_daemon():
    print("[Shinsekai Pulse] Audio-reactive window border daemon running (PipeWire / Hyprland Lua mode).", flush=True)
    angle = 45
    step = 8
    was_playing = False
    was_active = is_shinsekai_active()
    
    while True:
        active = is_shinsekai_active()
        
        # When theme is switched away from Shinsekai to any other theme:
        if not active:
            if was_active or was_playing:
                # Instantly restore the other theme's native configuration
                subprocess.run(["hyprctl", "reload"], capture_output=True)
                was_playing = False
                was_active = False
            time.sleep(2)
            continue
            
        was_active = True
        
        if not is_pulse_enabled():
            if was_playing:
                reset_border()
                was_playing = False
            time.sleep(2)
            continue
            
        playing = is_audio_playing()
        
        if playing:
            was_playing = True
            p_hex, s_hex = get_theme_colors()
            pr, pg, pb = int(p_hex[1:3], 16), int(p_hex[3:5], 16), int(p_hex[5:7], 16)
            sr, sg, sb = int(s_hex[1:3], 16), int(s_hex[3:5], 16), int(s_hex[5:7], 16)
            
            angle = (angle + step) % 360
            lua_code = f'hl.config({{ general = {{ col = {{ active_border = {{ colors = {{ "rgba({pr:02x}{pg:02x}{pb:02x}ee)", "rgba({sr:02x}{sg:02x}{sb:02x}ee)" }}, angle = {angle} }} }} }} }})'
            subprocess.run(["hyprctl", "eval", lua_code], capture_output=True)
            time.sleep(0.05) # Smooth 20 FPS rotation during playback
        else:
            if was_playing:
                reset_border()
                was_playing = False
            # Sleep at zero CPU when silent
            time.sleep(0.6)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--reset":
        reset_border()
    else:
        run_pulse_daemon()
