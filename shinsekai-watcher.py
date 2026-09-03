#!/usr/bin/env python3
import os, time, subprocess, sys, select, ctypes

# Zero CPU / Zero Battery inotify event-driven watcher
# Puts process into kernel sleep (0.00% CPU) until wallpaper change event occurs

SCRIPT = os.path.expanduser("~/.config/omarchy/themes/shinsekai/dynamic-theme.py")
BG_LINK = os.path.expanduser("~/.local/state/omarchy/current/background")
THEME_NAME_FILE = os.path.expanduser("~/.local/state/omarchy/current/theme.name")
WATCH_DIR = os.path.expanduser("~/.local/state/omarchy/current")

last_target = ""

def is_shinsekai_active():
    if os.path.exists(THEME_NAME_FILE):
        try:
            with open(THEME_NAME_FILE, "r") as f:
                return f.read().strip().lower() == "shinsekai"
        except Exception:
            pass
    return False

def sync_theme():
    global last_target
    if not is_shinsekai_active():
        # Do not interfere with other Omarchy themes
        return

    if os.path.exists(BG_LINK):
        try:
            target = os.path.realpath(BG_LINK)
            if target != last_target:
                last_target = target
                print(f"[Shinsekai Event] Wallpaper changed: {os.path.basename(target)}", flush=True)
                subprocess.run([sys.executable, SCRIPT, target])
        except Exception as e:
            print(f"[Shinsekai Error] {e}", flush=True)

# Run once on startup if active
sync_theme()

# Set up Linux inotify using libc syscalls (pure kernel event notification, 0% CPU)
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
    
    while True:
        try:
            events = poll_obj.poll()
            if events:
                os.read(inotify_fd, 4096)
                time.sleep(0.15)
                sync_theme()
        except Exception:
            time.sleep(1)
            sync_theme()
else:
    while True:
        time.sleep(1)
        sync_theme()
