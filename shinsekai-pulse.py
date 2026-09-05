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

def get_theme_colors():
    p_hex, s_hex = "#2cf535", "#b528e0"
    if os.path.exists(COLORS_FILE):
        try:
            with open(COLORS_FILE, "r") as f:
                content = f.read()
                m_acc = re.search(r'accent\s*=\s*\"(#[0-9a-fA-F]{6})\"', content)
                m_cur = re.search(r'cursor\s*=\s*\"(#[0-9a-fA-F]{6})\"', content)
                if m_acc: p_hex = m_acc.group(1)
                if m_cur: s_hex = m_cur.group(1)
        except Exception:
            pass
    return p_hex, s_hex

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
    
    while True:
        if not is_shinsekai_active() or not is_pulse_enabled():
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
