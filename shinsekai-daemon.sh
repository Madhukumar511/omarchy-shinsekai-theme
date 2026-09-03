#!/bin/bash
# Watches Omarchy background changes and extracts dynamic color palette in real-time
BG_DIR="$HOME/.local/state/omarchy/current"
SCRIPT="$HOME/.config/omarchy/themes/shinsekai/dynamic-theme.py"

# Apply on startup
python3 "$SCRIPT" 2>/dev/null || true

# Watch for background symlink changes
while true; do
  inotifywait -q -e create,modify,attrib,moved_to,close_write "$BG_DIR" 2>/dev/null
  sleep 0.1
  python3 "$SCRIPT" 2>/dev/null || true
done
