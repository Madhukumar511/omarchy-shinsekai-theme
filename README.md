# Shinsekai (新世界) — Dynamic Anime Aesthetic Theme for Omarchy

<p align="center">
  <img src="preview.png" width="850" alt="Shinsekai Theme Preview">
</p>

<p align="center">
  <strong>新世界 (Shinsekai) — <em>"New Worlds"</em></strong><br>
  A curated anime visual theme for <strong>Omarchy Linux & Hyprland</strong> featuring <strong>12 default 4K & 8K anime landscapes, celestial skies, and character art</strong> with <strong>Real-Time Dynamic Color Adaptation</strong>, a built-in <strong>CLI Wallpaper Manager</strong>, and <strong>Trash Recovery (Undo)</strong>.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Omarchy%20%7C%20Hyprland-blue?style=for-the-badge&logo=archlinux" alt="Platform">
  <img src="https://img.shields.io/badge/Wallpapers-12%20Default%204K%2F8K%20(Expandable)-purple?style=for-the-badge" alt="Wallpapers">
  <img src="https://img.shields.io/badge/Theming-Real--Time%20Dynamic%20Sync-green?style=for-the-badge" alt="Dynamic Theming">
  <img src="https://img.shields.io/badge/CLI%20Tool-shin--bg%20Manager-magenta?style=for-the-badge" alt="CLI Tool">
  <img src="https://img.shields.io/badge/License-MIT-orange?style=for-the-badge" alt="License">
</p>

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Wallpaper Gallery (12 Default Masterpieces)](#wallpaper-gallery-12-default-masterpieces)
- [Wallpaper Manager CLI (`shin-bg`)](#wallpaper-manager-cli-shin-bg)
- [Trash Recovery & Undo System](#trash-recovery--undo-system)
- [How Dynamic Theming Works](#how-dynamic-theming-works)
- [Luminance & Readability Guard](#luminance--readability-guard)
- [Terminal Download & Installation Guide](#terminal-download--installation-guide)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Included App Styles](#included-app-styles)
- [Project File Structure](#project-file-structure)
- [License](#license)

---

## Overview

**Shinsekai (新世界)** brings together iconic anime universes into a single, cohesive desktop experience.

From vast open meadows and Lake Itomori sunsets to celestial snow peaks, wisteria mountain trails, neon moonlit skylines, and striking character art, each wallpaper brings a distinct atmosphere.

Powered by a custom **Hue-Clustered Dynamic Color Engine**, your entire system—window borders, top bar, browser accents, terminal syntax, launcher, and notifications—automatically adapts in real-time to match whichever wallpaper you choose.

Users can freely add as many custom 4K wallpapers as they want (`[01-N]`) using the built-in `shin-bg` CLI tool.

---

## Key Features

- **Real-Time Dynamic Color Adaptation**:
  - Automatically extracts dominant color palettes and gradient pairs on wallpaper change.
  - Live reloads Hyprland window borders, Walker launcher, SwayOSD, and top bar in a single frame.
  - Retints Brave/Chromium browser theme and terminal syntax instantly.
- **Dynamic Lock Screen Engine with Toggle**:
  - Frosted glass multi-pass blur and dynamic wallpaper accent glow on the lock screen.
  - Turn dynamic lockscreen theming ON or OFF anytime with `shin-bg lock on/off`.
- **Day & Night Time-of-Day Auto-Cycling**:
  - Seamlessly transitions wallpapers across **Day** (07:00-17:00), **Sunset** (17:00-20:00), and **Night** (20:00-07:00).
  - Smart manual selection pause: selecting a specific wallpaper automatically pauses auto-cycling. Toggle with `shin-bg auto on/off`.
- **Music-Reactive Audio Border Pulse**:
  - Low-overhead PipeWire audio stream tracker that pulses and smoothly rotates Hyprland window border gradients in sync with music/video playback. Toggle with `shin-bg pulse on/off`.
- **CLI Wallpaper Manager & Quality Checker (`shin-bg`)**:
  - Add, download, rename, quality-check (4K/8K resolution guard), and manage custom wallpapers directly from any terminal.
- **Trash Recovery & Undo System**:
  - Accidental deletions are safely preserved in recovery trash; restore anytime with `shin-bg undo` or `shin-bg restore <number>`.
- **Zero-Battery Kernel Inotify Engine**:
  - Event-driven background watcher uses pure Linux kernel inotify blocking (`0.00% CPU, 0 battery consumption`).
- **Luminance & Contrast Guard**:
  - Enforces minimum brightness (`v >= 0.88`) on all dynamically extracted accent colors for 100% crisp terminal text readability.
- **12 Curated 4K & 8K Visual Masterpieces (Expandable)**:
  - High-definition art across iconic anime universes (*Sword Art Online, Your Name, Genshin Impact, Frieren, Violet Evergarden, Studio Ghibli, Suzume, Weathering With You, Wuthering Waves, Cyberpunk Edgerunners, Demon Slayer, and Twilight Horizon*).
- **Silky Spring Animations**:
  - Snappy cubic-bezier physics transitions (`shinsekaiEase: 0.16, 1, 0.3, 1`) for window popins and workspace sliding.

---

## Wallpaper Gallery (12 Default Masterpieces)

| 01. Sword Art Online — Asuna Sunlit Meadow (4K) | 02. Your Name — Mitsuha Lake Itomori Sunset (4K) |
| :---: | :---: |
| <img src="backgrounds/01-asuna-meadow-nature.png" width="380" alt="Asuna Meadow"> | <img src="backgrounds/02-mitsuha-lake-nature.png" width="380" alt="Mitsuha Lake"> |

| 03. Genshin Impact — Columbina Celestial Snow (8K) | 04. Frieren — Blue Flower Field (4K) |
| :---: | :---: |
| <img src="backgrounds/03-columbina-snow-8k.jpg" width="380" alt="Columbina Snow"> | <img src="backgrounds/04-frieren-field-4k.png" width="380" alt="Frieren Field"> |

| 05. Violet Evergarden — Water Meadow (8K) | 06. Spirited Away — Sea Railway Train (4K) |
| :---: | :---: |
| <img src="backgrounds/05-violet-evergarden-8k.jpg" width="380" alt="Violet Evergarden"> | <img src="backgrounds/06-spirited-away-train-4k.jpg" width="380" alt="Spirited Away Train"> |

| 07. Suzume — Cosmic Starry Twilight (4K) | 08. Weathering With You — Sunshine Clouds (8K) |
| :---: | :---: |
| <img src="backgrounds/07-suzume-door-starry-4k.jpg" width="380" alt="Suzume Door"> | <img src="backgrounds/08-weathering-with-you-8k.jpg" width="380" alt="Weathering With You"> |

| 09. Wuthering Waves — Chisa's Crimson Reach (4K) | 10. Cyberpunk Edgerunners — Moon Skyline (5K) |
| :---: | :---: |
| <img src="backgrounds/09-wuthering-waves-chisa-4k.jpg" width="380" alt="Chisa Crimson Reach"> | <img src="backgrounds/10-edgerunners-moon-4k.jpg" width="380" alt="Edgerunners Moon"> |

| 11. Demon Slayer — Wisteria Mountain (4K) | 12. Anime Scenery — Twilight Horizon (4K) |
| :---: | :---: |
| <img src="backgrounds/11-demon-slayer-wisteria-4k.jpg" width="380" alt="Demon Slayer Wisteria"> | <img src="backgrounds/12-anime-sunset-horizon-4k.jpg" width="380" alt="Twilight Horizon"> |

---

## Wallpaper Manager CLI (`shin-bg`)

Shinsekai includes a custom terminal tool to download, inspect quality, and manage wallpapers from any terminal location (`no cd required`).

### CLI Commands Reference

| Command | Action | Example |
| :--- | :--- | :--- |
| `shin-bg` | Open interactive manager with clipboard link detector | `shin-bg` |
| `shin-bg list` | View all installed wallpapers with assigned numbers `[01-N]` | `shin-bg list` |
| `shin-bg set <number>` | Switch active wallpaper by number (auto-pauses cycling) | `shin-bg set 4` |
| `shin-bg add <url-or-path> [name]` | Download 4K/8K wallpaper & auto-assign next number | `shin-bg add <link> solo-leveling` |
| `shin-bg rename <num> <name>` | Rename wallpaper while preserving index order | `shin-bg rename 13 lord-of-mysteries` |
| `shin-bg auto [on\|off\|status]` | Toggle Day/Night time-of-day auto wallpaper transitions | `shin-bg auto on` |
| `shin-bg pulse [on\|off\|status]` | Toggle music-reactive audio glowing window borders | `shin-bg pulse on` |
| `shin-bg lock [on\|off\|status]` | Toggle dynamic lockscreen blur & accent border sync | `shin-bg lock off` |
| `shin-bg remove <number>` | Safely move wallpaper to recovery trash | `shin-bg remove 13` |
| `shin-bg restore [number]` | Undo / Restore deleted wallpaper | `shin-bg undo` or `shin-bg restore 13` |
| `shin-bg trash` | View deleted wallpapers in recovery trash | `shin-bg trash` |
| `shin-bg next` | Cycle to next wallpaper | `shin-bg next` |
| `shin-bg current` | Show currently active wallpaper | `shin-bg current` |

---

## Trash Recovery & Undo System

If you accidentally delete a wallpaper:
- Removed wallpapers are moved to `.trash/` instead of permanent deletion.
- Run **`shin-bg undo`** to immediately restore the last deleted wallpaper.
- Or run **`shin-bg restore <number>`** to recover a specific wallpaper number.

---

## Dynamic Lock Screen Engine & Toggle

Shinsekai integrates directly with both Omarchy's lock screen (`omarchy-shell`) and Hyprland's `hyprlock`:
- **Frosted Acrylic Background**: Multi-pass Gaussian blur (`passes = 3`, `size = 8`, `vibrancy = 0.90`) rendered live over your current anime wallpaper.
- **Dynamic Glow Border**: When active or typing, the password entry border pulses in the dominant accent color extracted from your current wallpaper.
- **Toggle Mode Anytime**:
  ```bash
  # Enable dynamic wallpaper blur & glowing accent border
  shin-bg lock on

  # Disable to use clean neutral minimal dark lockscreen
  shin-bg lock off

  # Check current lockscreen dynamic state
  shin-bg lock status
  ```

---

## Day & Night Time-of-Day Auto-Cycling

Shinsekai can automatically transition between anime atmospheres according to your local time:
- **Day (07:00 – 17:00)**: Sunlit meadows, blue flower fields, open skies (*Asuna, Frieren, Violet Evergarden, Weathering With You*).
- **Sunset (17:00 – 20:00)**: Golden hour horizons, lake sunsets, twilight vistas (*Your Name Lake Itomori, Twilight Horizon, Sea Train*).
- **Night (20:00 – 07:00)**: Celestial skies, neon cityscapes, starry doors, moonlit skylines (*Suzume, Edgerunners, Columbina, Wisteria Mountain*).

```bash
# Enable auto-cycling
shin-bg auto on

# Disable auto-cycling (keeps your current wallpaper)
shin-bg auto off

# Check current time-slot and auto-cycle status
shin-bg auto status
```
> **Smart Pause:** Selecting any wallpaper manually via `shin-bg set <number>` or `SUPER + CTRL + SPACE` automatically pauses auto-cycling so your custom choice is never overwritten.

---

## Music-Reactive Audio Border Pulse

Turn your window borders into a live audio visualizer:
- **PipeWire Native Stream Tracking**: Detects audio from YouTube, Spotify, VLC, browser tabs, or media players with zero lag.
- **Dynamic Gradient Rotation**: Window borders gently pulse and rotate their dual-tone 45° anime gradient in sync with playing audio.
- **Zero-CPU Idle Sleep**: Immediately halts when music/video stops, using **0.00% CPU** during silence.

```bash
# Turn on audio-reactive window borders
shin-bg pulse on

# Turn off audio-reactive borders (returns to static gradient)
shin-bg pulse off

# Check status
shin-bg pulse status
```

---

## How Dynamic Theming Works

1. **Kernel Event Detection**: A background service (`shinsekai-watcher.py`) blocks in Linux kernel `inotify` sleep with **0.00% CPU / 0 battery draw**.
2. **Hue Clustering**: Quantizes wallpaper into 12 distinct Hue sectors (30° bins) to aggregate color weight and identify the true dominant atmosphere of the artwork.
3. **Full-Desktop Broadcast**:
   - Triggers `omarchy-theme-set` to update the top bar, Walker launcher, SwayOSD, and GTK apps.
   - Retints Brave/Chromium browser via policy JSON.
   - Reloads Hyprland active border gradients in 1 frame.

---

## Luminance & Readability Guard

To prevent dark or muted backgrounds from making terminal text and syntax highlighting dim:
- **Locked Foreground**: Pure starlight white (`#f8fafc`) for base text.
- **Brightness Floor (`v >= 0.88`)**: Automatically lifts dark tones into clear, luminous pastel/neon highlights.
- **Guaranteed WCAG Contrast**: Eliminates unreadable command arguments across all wallpapers.

---

## Terminal Download & Installation Guide

### Method 1: Automated Installer (Fastest)

Run the one-line installer in your terminal:

```bash
omarchy theme install https://github.com/Madhukumar511/omarchy-shinsekai-theme.git
```

Then enable the background color sync daemon and CLI tool:

```bash
mkdir -p ~/.config/systemd/user ~/.local/bin
ln -nsf ~/.config/omarchy/themes/shinsekai/shinsekai-wallpaper ~/.local/bin/shinsekai-wallpaper
ln -nsf ~/.config/omarchy/themes/shinsekai/shinsekai-wallpaper ~/.local/bin/shin-bg
ln -nsf ~/.config/omarchy/themes/shinsekai/shinsekai-wallpaper ~/.local/bin/shinsekai

cat << 'EOF' > ~/.config/systemd/user/shinsekai-dynamic.service
[Unit]
Description=Shinsekai Theme Dynamic Wallpaper Color Sync
After=graphical-session.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 %h/.config/omarchy/themes/shinsekai/shinsekai-watcher.py
Restart=always
RestartSec=1

[Install]
WantedBy=default.target
EOF

systemctl --user daemon-reload
systemctl --user enable --now shinsekai-dynamic.service
```

---

### Method 2: Manual Git Clone (Step-by-Step)

If you prefer cloning and setting up manually:

```bash
# 1. Clone repository to Omarchy themes directory
git clone https://github.com/Madhukumar511/omarchy-shinsekai-theme.git ~/.config/omarchy/themes/shinsekai

# 2. Activate theme in Omarchy
omarchy theme set shinsekai

# 3. Setup Wallpaper Manager CLI
mkdir -p ~/.local/bin
ln -nsf ~/.config/omarchy/themes/shinsekai/shinsekai-wallpaper ~/.local/bin/shinsekai-wallpaper
ln -nsf ~/.config/omarchy/themes/shinsekai/shinsekai-wallpaper ~/.local/bin/shin-bg
ln -nsf ~/.config/omarchy/themes/shinsekai/shinsekai-wallpaper ~/.local/bin/shinsekai

# 4. Enable real-time dynamic background color service
mkdir -p ~/.config/systemd/user
cat << 'EOF' > ~/.config/systemd/user/shinsekai-dynamic.service
[Unit]
Description=Shinsekai Theme Dynamic Wallpaper Color Sync
After=graphical-session.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 %h/.config/omarchy/themes/shinsekai/shinsekai-watcher.py
Restart=always
RestartSec=1

[Install]
WantedBy=default.target
EOF

systemctl --user daemon-reload
systemctl --user enable --now shinsekai-dynamic.service

# 5. Reload Hyprland
hyprctl reload
```

---

### Method 3: Walker GUI Menu

1. Copy the repository URL: `https://github.com/Madhukumar511/omarchy-shinsekai-theme.git`
2. Open Walker launcher (`SUPER + ALT + SPACE` or `SUPER + SPACE`).
3. Navigate: **Install > Style > Theme**.
4. Paste the URL and press **Enter**.

---

## Verifying & Switching Wallpapers

After installation, cycle through wallpapers and watch your entire desktop dynamically adapt in real-time:

```bash
# Cycle to next wallpaper
shin-bg next

# List all wallpapers
shin-bg list
```

Or press **`SUPER + CTRL + SPACE`** on your keyboard to open the visual thumbnail picker.

---

## Keyboard Shortcuts

| Shortcut | Action |
| :--- | :--- |
| `SUPER + CTRL + SPACE` | **Interactive Wallpaper Switcher GUI** |
| `SUPER + CTRL + L` | **Lock System** (Frosted Glass & Dynamic Glow Border) |
| `SUPER + SHIFT + CTRL + SPACE` | **Theme Selector Menu** |
| `SUPER + SPACE` | **Omarchy Root Menu** |
| `SUPER + ALT + SPACE` | **Walker / Application Launcher** |
| `SUPER + ENTER` | **Launch Terminal** (frosted acrylic blur) |

---

## Included App Styles

Shinsekai ships with complete styling templates for all major tools:

- **Terminal & Shell**: `starship.toml`, `fastfetch.jsonc`, `alacritty.toml`, `kitty.conf`, `btop.theme`
- **Desktop Environment**: `hyprland.lua`, `gtk.css`, `walker.css`, `mako.ini`, `swayosd.css`, `hyprlock.conf`, `shell.lock.toml`, `icons.theme` (Yaru-blue-dark)
- **Code Editors & Apps**: `vscode.json`, `neovim.lua`, `obsidian.css`, `vencord.theme.css` (Discord), `zed.json`

---

## Project File Structure

```
~/.config/omarchy/themes/shinsekai/
├── backgrounds/                # 12+ Default 4K/8K Anime Wallpapers (Expandable to [01-N])
├── .trash/                     # Wallpaper Recovery Trash for Undo
├── shinsekai-wallpaper        # Custom Wallpaper Downloader & CLI Manager (shin-bg)
├── dynamic-theme.py           # Hue-Clustering Dynamic Color Extractor & System Sync
├── shinsekai-watcher.py       # Zero-CPU Linux Kernel Inotify Background Daemon
├── shinsekai-pulse.py         # PipeWire Music-Reactive Dynamic Border Visualizer
├── shinsekai-daemon.sh        # Standalone Bash Watcher
├── colors.toml                # Active Dynamic Palette
├── hyprland.lua               # Hyprland Window Borders, Blur & Animations
├── hyprlock.conf              # Dynamic Hyprlock Lockscreen Styling
├── shell.lock.toml            # Omarchy Quickshell Dynamic Lockscreen Styling
├── chromium.theme             # Brave / Chromium RGB Accent Theme
├── fastfetch.jsonc            # Anime System Info Configuration
├── starship.toml              # Shell Prompt Styling
├── alacritty.toml             # Alacritty Terminal Theme
├── kitty.conf                 # Kitty Terminal Theme
├── btop.theme                 # System Monitor Theme
├── icons.theme                # System Icon Set (Yaru-blue-dark)
├── preview.png                # Theme Selector Preview Banner
├── preview-unlock.png         # Hyprlock Lockscreen Preview
├── unlock.png                 # Lockscreen Asset
└── README.md                  # Theme Documentation
```

---

## License

Released under the **MIT License**. Free to use, modify, and distribute.

### Artwork & Wallpaper Attribution
All wallpapers curated in this repository belong to their respective original artists and animation studios (including CoMix Wave Films, Kyoto Animation, Studio Ghibli, Wit Studio, Ufotable, Trigger, etc.). They are included under non-commercial fair use for personal desktop customization. If you are an artist and wish to have your artwork specifically credited, linked, or removed, please open an issue and it will be handled promptly.
