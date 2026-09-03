#!/usr/bin/env python3
import os, time, subprocess, sys

SCRIPT = os.path.expanduser("~/.config/omarchy/themes/shinsekai/dynamic-theme.py")
BG_LINK = os.path.expanduser("~/.local/state/omarchy/current/background")

last_target = ""

def check_and_update():
    global last_target
    if os.path.exists(BG_LINK):
        try:
            target = os.path.realpath(BG_LINK)
            if target != last_target:
                last_target = target
                print(f"[Shinsekai] Wallpaper changed to: {target}", flush=True)
                subprocess.run([sys.executable, SCRIPT, target])
        except Exception as e:
            print(f"[Shinsekai] Error: {e}", flush=True)

# Run once immediately on start
check_and_update()

# Continuous watch loop (polls every 300ms, zero CPU overhead)
while True:
    time.sleep(0.3)
    check_and_update()
