# Shinsekai (新世界) — Dynamic Scenery-First Anime Aesthetic Theme for Omarchy

<p align="center">
  <img src="preview.png" width="850" alt="Shinsekai Theme Preview">
</p>

<p align="center">
  <strong>新世界 (Shinsekai) — <em>"New Worlds"</em></strong><br>
  An intelligent, scenery-first anime theme for <strong>Omarchy Linux & Hyprland</strong> featuring <strong>12 curated 4K & 8K environmental landscape wallpapers</strong> with <strong>Real-Time Dynamic Color Adaptation</strong>.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Omarchy%20%7C%20Hyprland-blue?style=for-the-badge&logo=archlinux" alt="Platform">
  <img src="https://img.shields.io/badge/Wallpapers-12%20Curated%204K%2F8K-purple?style=for-the-badge" alt="Wallpapers">
  <img src="https://img.shields.io/badge/Theming-Real--Time%20Dynamic%20Sync-green?style=for-the-badge" alt="Dynamic Theming">
  <img src="https://img.shields.io/badge/License-MIT-orange?style=for-the-badge" alt="License">
</p>

---

## Table of Contents

- [Overview & Philosophy](#overview--philosophy)
- [Key Features](#key-features)
- [Wallpaper Gallery (12 Masterpieces)](#wallpaper-gallery-12-masterpieces)
- [How Dynamic Theming Works](#how-dynamic-theming-works)
- [Luminance & Readability Guard](#luminance--readability-guard)
- [Installation Guide](#installation-guide)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Included App Styles](#included-app-styles)
- [Project File Structure](#project-file-structure)
- [License](#license)

---

## Overview & Philosophy

**Shinsekai** was designed around a single guiding principle: **Scenery First**.

When someone glances at your desktop, they should be struck by the vast, breathtaking environmental landscape first, with iconic anime characters harmoniously integrated into their world.

Powered by a custom **Hue-Clustered Dynamic Color Engine**, every window border, the top bar, browser accents, terminal text, launcher, and notifications automatically adapt in real-time to match whichever wallpaper you select.

---

## Key Features

- **Real-Time Dynamic Color Adaptation**:
  - Automatically extracts dominant color palettes and gradient pairs on wallpaper change.
  - Live reloads Hyprland window borders in a single frame.
  - Updates Brave/Chromium browser theme, top bar (Omarchy QuickShell), Walker launcher, and GTK apps instantly.
- **Luminance & Contrast Guard**:
  - Enforces minimum brightness (`v >= 0.88`) on all dynamically extracted accent colors.
  - Guarantees 100% crisp terminal text readability and WCAG contrast even on dark or dull wallpapers.
- **12 Curated 4K & 8K Environmental Masterpieces**:
  - Uncompressed, high-definition art across iconic anime universes (*Sword Art Online, Your Name, Genshin Impact, Frieren, Violet Evergarden, Studio Ghibli, Suzume, Weathering With You, Wuthering Waves, Cyberpunk Edgerunners, Demon Slayer, and Twilight Horizon*).
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

## How Dynamic Theming Works

1. **Background Detection**: A background service (`shinsekai-watcher.py`) monitors wallpaper symlink changes with zero CPU overhead.
2. **Hue Clustering**: Quantizes wallpaper into 12 distinct Hue sectors (30° bins) to aggregate color weight and identify true dominant environmental landscapes (e.g. green hills vs purple accents).
3. **Full-Desktop Broadcast**:
   - Triggers `omarchy-theme-set` to update the top bar, Walker launcher, SwayOSD, and GTK apps.
   - Retints Brave/Chromium browser via policy JSON.
   - Reloads Hyprland active border gradients in 1 frame.

---

## Luminance & Readability Guard

To prevent dark or muted wallpapers from making terminal text and syntax highlighting dim:
- **Locked Foreground**: Pure starlight white (`#f8fafc`) for base text.
- **Brightness Floor (`v >= 0.88`)**: Automatically lifts dark tones into clear, luminous pastel/neon highlights.
- **Guaranteed WCAG Contrast**: Eliminates unreadable command arguments across all 12 wallpapers.

---

## Installation Guide

### Option A: Terminal Installation (Recommended)

```bash
# 1. Install theme
omarchy theme install https://github.com/Madhukumar511/omarchy-shinsekai-theme.git

# 2. Enable real-time dynamic background color service
mkdir -p ~/.config/systemd/user
cat << 'SERVICE_EOF' > ~/.config/systemd/user/shinsekai-dynamic.service
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
SERVICE_EOF

systemctl --user daemon-reload
systemctl --user enable --now shinsekai-dynamic.service
```

### Option B: Walker GUI Menu

1. Copy the repo URL: `https://github.com/Madhukumar511/omarchy-shinsekai-theme.git`
2. Open Walker / Omarchy menu (`SUPER + ALT + SPACE` or `SUPER + SPACE`).
3. Navigate to: **Install > Style > Theme**.
4. Paste the URL and press **Enter**.

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
├── backgrounds/                # 12 Curated 4K/8K Anime Scenery Wallpapers
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
