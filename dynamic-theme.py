#!/usr/bin/env python3
import subprocess, re, os, colorsys, sys, base64

def get_current_background():
    bg_link = os.path.expanduser("~/.local/state/omarchy/current/background")
    if os.path.exists(bg_link):
        return os.path.realpath(bg_link)
    return os.path.expanduser("~/.config/omarchy/themes/shinsekai/backgrounds/01-asuna-meadow-nature.png")

def extract_vibrant_colors(image_path):
    cmd = f'magick "{image_path}" -resize 120x120! -colors 16 -format "%c" histogram:info:'
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout
    
    parsed = []
    for line in res.strip().split('\n'):
        match = re.search(r'#([0-9a-fA-F]{6})', line)
        count_match = re.search(r'^\s*([0-9]+):', line)
        if match and count_match:
            hex_col = '#' + match.group(1).lower()
            count = int(count_match.group(1))
            
            r = int(hex_col[1:3], 16) / 255.0
            g = int(hex_col[3:5], 16) / 255.0
            b = int(hex_col[5:7], 16) / 255.0
            h, s, v = colorsys.rgb_to_hsv(r, g, b)
            
            parsed.append({
                'hex': hex_col,
                'count': count,
                'r': int(r * 255),
                'g': int(g * 255),
                'b': int(b * 255),
                'h': h,
                's': s,
                'v': v,
                'vibrancy': s * (1.0 - abs(v - 0.65)) * 2.0 + (0.1 if s > 0.3 else 0.0)
            })
            
    vibrant_sorted = sorted(parsed, key=lambda x: x['vibrancy'], reverse=True)
    
    if len(vibrant_sorted) >= 2:
        primary = vibrant_sorted[0]
        secondary = None
        for c in vibrant_sorted[1:]:
            if abs(c['h'] - primary['h']) > 0.15:
                secondary = c
                break
        if not secondary:
            secondary = vibrant_sorted[1]
    else:
        primary = {'hex': '#38bdf8', 'r': 56, 'g': 189, 'b': 248}
        secondary = {'hex': '#00e5ff', 'r': 0, 'g': 229, 'b': 255}
        
    return primary, secondary

def apply_dynamic_theme(image_path=None):
    if not image_path:
        image_path = get_current_background()
        
    if not os.path.exists(image_path):
        return
        
    primary, secondary = extract_vibrant_colors(image_path)
    
    theme_dir = os.path.expanduser("~/.config/omarchy/themes/shinsekai")
    
    # 1. Update chromium.theme
    with open(os.path.join(theme_dir, "chromium.theme"), "w") as f:
        f.write(f"{primary['r']},{primary['g']},{primary['b']}\n")
        
    # 2. Update colors.toml
    colors_toml = f"""accent = "{primary['hex']}"
cursor = "{secondary['hex']}"
foreground = "#f8fafc"
background = "#090d16"
selection_foreground = "#ffffff"
selection_background = "{primary['hex']}"

# Dynamic Window Borders
hyprland_active_border = "{primary['hex']} {secondary['hex']} 45deg"
hyprland_inactive_border = "rgba(15,23,42,0.65)"

color0 = "#0f172a"
color1 = "#ef4444"
color2 = "#10b981"
color3 = "#f59e0b"
color4 = "{primary['hex']}"
color5 = "{secondary['hex']}"
color6 = "#00e5ff"
color7 = "#e2e8f0"
color8 = "#334155"
color9 = "#f87171"
color10 = "#34d399"
color11 = "#fbbf24"
color12 = "{primary['hex']}"
color13 = "{secondary['hex']}"
color14 = "#67e8f9"
color15 = "#ffffff"
"""
    with open(os.path.join(theme_dir, "colors.toml"), "w") as f:
        f.write(colors_toml)
        
    # Also update the staged current theme colors if present
    current_theme_colors = os.path.expanduser("~/.local/state/omarchy/current/theme/colors.toml")
    if os.path.exists(current_theme_colors):
        with open(current_theme_colors, "w") as f:
            f.write(colors_toml)

    # 3. Update hyprland.lua & looknfeel.lua
    hypr_lua = f"""-- Shinsekai Dynamic Anime Theme for Hyprland
local active_border_color = {{ colors = {{ "rgba({primary['r']:02x}{primary['g']:02x}{primary['b']:02x}ee)", "rgba({secondary['r']:02x}{secondary['g']:02x}{secondary['b']:02x}ee)" }}, angle = 45 }}
local inactive_border_color = "rgba(0f172a66)"

hl.config({{
  general = {{
    gaps_in = 5,
    gaps_out = 10,
    border_size = 2,
    col = {{
      active_border = active_border_color,
      inactive_border = inactive_border_color,
    }},
  }},
  decoration = {{
    rounding = 10,
    active_opacity = 0.96,
    inactive_opacity = 0.88,
    dim_inactive = true,
    dim_strength = 0.12,
    blur = {{
      enabled = true,
      size = 6,
      passes = 3,
      new_optimizations = true,
      xray = false,
      ignore_opacity = false,
      noise = 0.01,
      contrast = 0.95,
      brightness = 0.88,
      popups = true,
    }},
    shadow = {{
      enabled = true,
      range = 18,
      render_power = 3,
      color = "rgba(00000088)",
      color_inactive = "rgba(00000055)",
    }},
  }},
  animations = {{
    enabled = true,
    bezier = {{
      "shinsekaiEase, 0.16, 1, 0.3, 1",
    }},
    animation = {{
      "windows, 1, 4, shinsekaiEase, popin 85%",
      "windowsOut, 1, 3, default, popin 85%",
      "windowsMove, 1, 4, shinsekaiEase",
      "border, 1, 6, default",
      "fade, 1, 3, default",
      "workspaces, 1, 4, shinsekaiEase, slide",
    }},
  }},
  group = {{
    col = {{
      border_active = active_border_color,
      border_inactive = inactive_border_color,
    }},
  }},
}})
"""
    with open(os.path.join(theme_dir, "hyprland.lua"), "w") as f:
        f.write(hypr_lua)
        
    looknfeel_path = os.path.expanduser("~/.config/hypr/looknfeel.lua")
    with open(looknfeel_path, "w") as f:
        f.write(hypr_lua)

    # 4. Trigger Omarchy full system & shell theme refresh
    # This automatically updates Top Bar (QuickShell), Walker launcher, Mako notifications,
    # SwayOSD overlays, Brave/Chromium, GTK apps, open terminals, Btop, and VSCode!
    env = os.environ.copy()
    env["OMARCHY_THEME_SKIP_BACKGROUND"] = "1"
    subprocess.run("omarchy-theme-set-templates 2>/dev/null", shell=True, env=env)
    subprocess.run("omarchy-theme-set-browser 2>/dev/null", shell=True, env=env)
    subprocess.run("omarchy-theme-set-gnome 2>/dev/null", shell=True, env=env)
    subprocess.run("omarchy-restart-terminal 2>/dev/null", shell=True, env=env)
    subprocess.run("omarchy-restart-btop 2>/dev/null", shell=True, env=env)
    subprocess.run("hyprctl reload 2>&1 >/dev/null", shell=True)
    
    # Update running omarchy-shell bar via IPC
    colors_b64 = base64.b64encode(colors_toml.encode('utf-8')).decode('utf-8')
    subprocess.run(f"omarchy-shell -q shell applyTheme '{colors_b64}' '' 2>/dev/null", shell=True)
    
    print(f"Full system dynamic theme applied for: {os.path.basename(image_path)} -> Primary: {primary['hex']} | Secondary: {secondary['hex']}", flush=True)

if __name__ == "__main__":
    img = sys.argv[1] if len(sys.argv) > 1 else None
    apply_dynamic_theme(img)
