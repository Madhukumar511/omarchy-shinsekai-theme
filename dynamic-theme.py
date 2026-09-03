#!/usr/bin/env python3
import subprocess, re, os, colorsys, sys

def get_current_background():
    bg_link = os.path.expanduser("~/.local/state/omarchy/current/background")
    if os.path.exists(bg_link):
        return os.path.realpath(bg_link)
    return os.path.expanduser("~/.config/omarchy/themes/shinsekai/backgrounds/01-asuna-meadow-nature.png")

def boost_color_for_readability(r, g, b, min_s=0.55, target_v=0.88):
    h, s, v = colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)
    # Ensure optimal saturation (not washed out, not blinding)
    s = max(min(s, 0.85), min_s)
    # Ensure luminous high brightness for crystal-clear readability against dark backgrounds
    v = max(min(v, 0.98), target_v)
    nr, ng, nb = colorsys.hsv_to_rgb(h, s, v)
    hex_code = f"#{int(nr*255):02x}{int(ng*255):02x}{int(nb*255):02x}"
    return hex_code, int(nr*255), int(ng*255), int(nb*255)

def extract_hue_clustered_palette(image_path):
    cmd = f'magick "{image_path}" -resize 120x120! -colors 32 -format "%c" histogram:info:'
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout
    
    # 12 hue bins (30 deg each)
    bins = [[] for _ in range(12)]
    
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
            
            # Filter pure grays/blacks
            if v < 0.12 or (s < 0.12 and v > 0.88):
                continue
                
            bin_idx = int((h * 360) // 30) % 12
            bins[bin_idx].append({
                'hex': hex_col,
                'count': count,
                'r': int(r * 255),
                'g': int(g * 255),
                'b': int(b * 255),
                'h': h,
                's': s,
                'v': v,
                'weight': count * (s ** 0.6) * (1.0 - abs(v - 0.6) * 0.4)
            })
            
    bin_scores = []
    for idx, b in enumerate(bins):
        if not b:
            continue
        total_weight = sum(item['weight'] for item in b)
        best_col = max(b, key=lambda x: x['s'] * (1.0 - abs(x['v'] - 0.65)))
        bin_scores.append((total_weight, idx, best_col))
        
    bin_scores.sort(key=lambda x: x[0], reverse=True)
    
    if len(bin_scores) >= 2:
        raw_p = bin_scores[0][2]
        raw_s = None
        for item in bin_scores[1:]:
            if abs(item[1] - bin_scores[0][1]) >= 2:
                raw_s = item[2]
                break
        if not raw_s:
            raw_s = bin_scores[1][2]
    elif len(bin_scores) == 1:
        raw_p = bin_scores[0][2]
        raw_s = {'r': 56, 'g': 189, 'b': 248}
    else:
        raw_p = {'r': 56, 'g': 189, 'b': 248}
        raw_s = {'r': 0, 'g': 229, 'b': 255}
        
    p_hex, pr, pg, pb = boost_color_for_readability(raw_p['r'], raw_p['g'], raw_p['b'], min_s=0.55, target_v=0.88)
    s_hex, sr, sg, sb = boost_color_for_readability(raw_s['r'], raw_s['g'], raw_s['b'], min_s=0.50, target_v=0.84)
    
    return {
        'hex': p_hex, 'r': pr, 'g': pg, 'b': pb
    }, {
        'hex': s_hex, 'r': sr, 'g': sg, 'b': sb
    }

def apply_dynamic_theme(image_path=None):
    if not image_path:
        image_path = get_current_background()
        
    if not os.path.exists(image_path):
        return
        
    primary, secondary = extract_hue_clustered_palette(image_path)
    theme_dir = os.path.expanduser("~/.config/omarchy/themes/shinsekai")
    
    # 1. Update chromium.theme
    with open(os.path.join(theme_dir, "chromium.theme"), "w") as f:
        f.write(f"{primary['r']},{primary['g']},{primary['b']}\n")
        
    # 2. Update colors.toml (with guaranteed high-contrast white foreground and crisp luminous ANSI accents)
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
color6 = "#06b6d4"
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

    # 4. Trigger full Omarchy OS theme pipeline
    env = os.environ.copy()
    env["OMARCHY_THEME_SKIP_BACKGROUND"] = "1"
    subprocess.run("omarchy-theme-set shinsekai >/dev/null 2>&1", shell=True, env=env)
    subprocess.run("hyprctl reload >/dev/null 2>&1", shell=True)
    
    print(f"[Shinsekai Dynamic] High-contrast theme applied for: {os.path.basename(image_path)} -> Primary: {primary['hex']} | Secondary: {secondary['hex']}", flush=True)

if __name__ == "__main__":
    img = sys.argv[1] if len(sys.argv) > 1 else None
    apply_dynamic_theme(img)
