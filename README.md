# Komorebi — Scenery-First Anime Aesthetic Theme for Omarchy

> **Komorebi** *(木漏れ日)* — The poetic Japanese concept for *sunlight filtering through trees*.

An anime-inspired theme crafted for **Omarchy | Hyprland**, featuring **12 iconic 4K & 8K scenery-first environmental landscape wallpapers** paired with a luminous OLED-optimized color palette, dynamic glowing 4-color anime gradient borders, and smooth spring physics animations.

---

## Wallpaper Gallery Previews

| 01. Asuna — Sunlit Meadow (4K) | 02. Mitsuha — Lake Itomori Sunset (4K) |
| :---: | :---: |
| <img src="backgrounds/01-asuna-meadow-nature.png" width="380" alt="Asuna Meadow"> | <img src="backgrounds/02-mitsuha-lake-nature.png" width="380" alt="Mitsuha Lake"> |

| 03. Columbina — Celestial Snow (8K) | 04. Frieren — Blue Flower Field (4K) |
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

## Features & Visual Enhancements

- **12 Curated 4K & 8K Environmental Masterpieces:**
  - Scenery-first anime landscapes where character and nature naturally harmonize.
- **4-Color Glowing Anime Gradient Borders:**
  - Active window borders feature a vibrant 45° glowing anime rainbow gradient:
    - *Sakura Blossom Pink* (`#ff3388`)
    - *Asuna Solar Orange* (`#ff6d00`)
    - *Electric Cyber Cyan* (`#00f0ff`)
    - *Mitsuha Sunset Violet* (`#b344ff`)
- **Radiant Anime Shadow Glow & Glassmorphism:**
  - Soft neon pink-violet outer drop shadow glow with multi-pass acrylic frosted window blur.
- **Snappy Anime Spring Physics Animations:**
  - Smooth, responsive spring bezier curve transitions (`animeSpring`) for window popins and workspace sliding.
- **Luminous OLED-Optimized Color Palette:**
  - Deep velvet void night canvas (`#080b12`) with high-contrast starlight white text (`#f8fafc`) and neon character accents.
- **Integrated Tool Themes:**
  - Custom `btop.theme`, `icons.theme` (Papirus-Dark), Neovim, VSCode, and Hyprlock lockscreen assets included.

---

## Color Palette Reference

| Color | Hex | Role |
| :--- | :--- | :--- |
| **Background** | `#080b12` | Deep void celestial canvas |
| **Foreground** | `#f8fafc` | Crisp starlight mist white |
| **Accent Primary** | `#ff3388` | Sakura Blossom Neon Pink |
| **Accent Secondary** | `#ff6d00` | Asuna Solar Flare Orange |
| **Cyan** | `#00f0ff` | Electric Cyber Stream |
| **Purple** | `#b344ff` | Mitsuha Sunset Violet |
| **Green** | `#00e676` | Lake Itomori Emerald |
| **Yellow** | `#ffd600` | Solar Comet Gold |

---

## Keyboard Shortcuts

| Shortcut | Action |
| :--- | :--- |
| `SUPER + CTRL + SPACE` | **Interactive Wallpaper Switcher GUI** |
| `SUPER + SHIFT + CTRL + SPACE` | **Theme Selector Menu** |
| `SUPER + SPACE` | **Omarchy Root Menu** |
| `SUPER + ALT + SPACE` | **Walker / Apps Launcher** |
| `SUPER + ENTER` | **Launch Terminal** (with frosted glass blur) |

---

## Installation

### Terminal (Recommended)

Run the Omarchy theme installer:

```bash
omarchy theme install https://github.com/Madhukumar511/omarchy-komorebi-theme.git
```

### Walker Menu

1. Copy the repo link: `https://github.com/Madhukumar511/omarchy-komorebi-theme.git`
2. Open Walker / Omarchy menu (`SUPER + ALT + SPACE` or `SUPER + SPACE`)
3. Navigate: **Install > Style > Theme**
4. Paste URL and press **Enter**

---

## Optional: Enable Glowing Borders & Anime Physics

To enable the 4-color glowing anime rainbow borders and spring animations, copy `hyprland.lua` into your Hyprland configuration:

```bash
cp ~/.config/omarchy/themes/komorebi/hyprland.lua ~/.config/hypr/looknfeel.lua
hyprctl reload
```

---

## Wallpaper Cycling

Cycle between all 12 anime scenery wallpapers anytime via terminal:

```bash
omarchy theme bg next
```

Or press `SUPER + CTRL + SPACE` to open the visual thumbnail switcher.

---

## License

MIT License. Free to use and customize.
