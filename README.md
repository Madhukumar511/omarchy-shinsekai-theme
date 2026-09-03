# Shinsekai (新世界) — Dynamic Anime Aesthetic Theme for Omarchy

<p align="center">
  <img src="preview.png" width="850" alt="Shinsekai Theme Preview">
</p>

<p align="center">
  <strong>新世界 (Shinsekai) — <em>"New Worlds"</em></strong><br>
  A curated anime visual theme for <strong>Omarchy Linux & Hyprland</strong> featuring <strong>12 iconic 4K & 8K anime landscapes, celestial skies, and character art</strong> with <strong>Real-Time Dynamic Color Adaptation</strong> and a built-in <strong>CLI Wallpaper Manager</strong>.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Omarchy%20%7C%20Hyprland-blue?style=for-the-badge&logo=archlinux" alt="Platform">
  <img src="https://img.shields.io/badge/Wallpapers-12%20Curated%204K%2F8K-purple?style=for-the-badge" alt="Wallpapers">
  <img src="https://img.shields.io/badge/Theming-Real--Time%20Dynamic%20Sync-green?style=for-the-badge" alt="Dynamic Theming">
  <img src="https://img.shields.io/badge/CLI%20Tool-Wallpaper%20Manager-magenta?style=for-the-badge" alt="CLI Tool">
  <img src="https://img.shields.io/badge/License-MIT-orange?style=for-the-badge" alt="License">
</p>

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Wallpaper Gallery (12 Masterpieces)](#wallpaper-gallery-12-masterpieces)
- [Wallpaper Manager CLI (`shinsekai-wallpaper`)](#wallpaper-manager-cli-shinsekai-wallpaper)
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

---

## Key Features

- **Real-Time Dynamic Color Adaptation**:
  - Automatically extracts dominant color palettes and gradient pairs on wallpaper change.
  - Live reloads Hyprland window borders in a single frame.
  - Updates Brave/Chromium browser theme, top bar (Omarchy QuickShell), Walker launcher, and GTK apps instantly.
- **CLI Wallpaper Manager & Quality Checker**:
  - Built-in `shinsekai-wallpaper` CLI to download, quality-check (4K/8K resolution guard), optimize, and manage custom wallpapers directly from terminal.
- **Luminance & Contrast Guard**:
  - Enforces minimum brightness (`v >= 0.88`) on all dynamically extracted accent colors.
  - Guarantees 100% crisp terminal text readability and WCAG contrast even on dark or muted backgrounds.
- **12 Curated 4K & 8K Visual Masterpieces**:
  - High-definition art across iconic anime universes (*Sword Art Online, Your Name, Genshin Impact, Frieren, Violet Evergarden, Studio Ghibli, Suzume, Weathering With You, Wuthering Waves, Cyberpunk Edgerunners, Demon Slayer, and Twilight Horizon*).
- **Glowing Anime Gradient Borders & Acrylic Glassmorphism**:
  - 45° glowing dual-tone active window borders with multi-pass frosted glass blur and subtle deep velvet shadows.
- **Silky Spring Animations**:
  - Snappy cubic-bezier physics transitions (`shinsekaiEase: 0.16, 1, 0.3, 1`) for window popins and workspace sliding.
- **Full Suite of Companion App Themes**:
  - Out-of-the-box configurations for Starship, Fastfetch, Btop, Alacritty, Kitty, Foot, Neovim, VSCode, Obsidian, Vencord (Discord), and Hyprlock.

---

## Wallpaper Gallery (12 Masterpieces)

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

## Wallpaper Manager CLI (`shinsekai-wallpaper`)

Shinsekai includes a custom terminal tool to add, download, inspect, and manage wallpapers with automatic quality inspection and dynamic palette adaptation.

### Download & Add a Wallpaper from URL

Find an image link on Google, Wallhaven, or AlphaCoders and add it directly:

```bash
# Add from web URL with a custom name
shinsekai-wallpaper add "https://w.wallhaven.cc/full/z8/wallhaven-z8opey.jpg" "saber-avalon"

# Or add from a local downloaded file
shinsekai-wallpaper add ~/Downloads/anime_wallpaper.png "my-custom-art"
```

The CLI automatically:
1. Validates the resolution (checks for native **4K/8K** or **2K/1080p**).
2. Sharpens and scales the image into clean 4K UHD format (quality 95).
3. Adds it to the theme gallery.
4. Immediately adapts your entire system color scheme to match the new image.

### CLI Commands Cheat Sheet

| Command | Action |
| :--- | :--- |
| `shinsekai-wallpaper list` | List all installed wallpapers with resolutions & file sizes |
| `shinsekai-wallpaper add <url-or-path> [name]` | Download or import a wallpaper with 4K quality check |
| `shinsekai-wallpaper set <number-or-name>` | Set specific wallpaper as active |
| `shinsekai-wallpaper remove <number-or-name>` | Delete a wallpaper from theme |
| `shinsekai-wallpaper next` | Cycle to next wallpaper |
| `shinsekai-wallpaper current` | Show currently active wallpaper |

---

## How Dynamic Theming Works

1. **Background Detection**: A background service (`shinsekai-watcher.py`) monitors wallpaper symlink changes with zero CPU overhead.
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
- **Guaranteed WCAG Contrast**: Eliminates unreadable command arguments across all 12 wallpapers.

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

## Verifying & Switching Wallpapers

After installation, cycle through wallpapers and watch your entire desktop dynamically adapt in real-time:

```bash
# Cycle to next wallpaper
shinsekai-wallpaper next

# List all wallpapers
shinsekai-wallpaper list
```

Or press **`SUPER + CTRL + SPACE`** on your keyboard to open the visual thumbnail picker.

---

## Keyboard Shortcuts

| Shortcut | Action |
| :--- | :--- |
| `SUPER + CTRL + SPACE` | **Interactive Wallpaper Switcher GUI** |
| `SUPER + SHIFT + CTRL + SPACE` | **Theme Selector Menu** |
| `SUPER + SPACE` | **Omarchy Root Menu** |
| `SUPER + ALT + SPACE` | **Walker / Application Launcher** |
| `SUPER + ENTER` | **Launch Terminal** (frosted acrylic blur) |

---

## Included App Styles

Shinsekai ships with complete styling templates for all major tools:

- **Terminal & Shell**: `starship.toml`, `fastfetch.jsonc`, `alacritty.toml`, `kitty.conf`, `btop.theme`
- **Desktop Environment**: `hyprland.lua`, `gtk.css`, `walker.css`, `mako.ini`, `swayosd.css`, `hyprlock.conf`, `icons.theme` (Yaru-blue-dark)
- **Code Editors & Apps**: `vscode.json`, `neovim.lua`, `obsidian.css`, `vencord.theme.css` (Discord), `zed.json`

---

## Project File Structure

```
~/.config/omarchy/themes/shinsekai/
├── backgrounds/                # 12 Curated 4K/8K Anime Wallpapers
├── shinsekai-wallpaper        # Custom Wallpaper Downloader & CLI Manager
├── dynamic-theme.py           # Hue-Clustering Dynamic Color Extractor & System Sync
├── shinsekai-watcher.py       # Background Watcher Daemon
├── shinsekai-daemon.sh        # Standalone Bash Watcher
├── colors.toml                # Active Dynamic Palette
├── hyprland.lua               # Hyprland Window Borders, Blur & Animations
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
