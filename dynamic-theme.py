#!/usr/bin/env python3
import subprocess, re, os, colorsys, sys, base64

THEME_NAME_FILE = os.path.expanduser("~/.local/state/omarchy/current/theme.name")

def is_shinsekai_active():
    if os.path.exists(THEME_NAME_FILE):
        try:
            with open(THEME_NAME_FILE, "r") as f:
                return f.read().strip().lower() == "shinsekai"
        except Exception:
            pass
    return False

def get_current_background():
    bg_link = os.path.expanduser("~/.local/state/omarchy/current/background")
    if os.path.exists(bg_link):
        return os.path.realpath(bg_link)
    return os.path.expanduser("~/.config/omarchy/themes/shinsekai/backgrounds/01-asuna-meadow-nature.png")

def boost_color_for_readability(r, g, b, min_s=0.55, target_v=0.92):
    h, s, v = colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)
    s = max(min(s, 0.82), min_s)
    v = max(min(v, 0.98), target_v)
    nr, ng, nb = colorsys.hsv_to_rgb(h, s, v)
    hex_code = f"#{int(nr*255):02x}{int(ng*255):02x}{int(nb*255):02x}"
    return hex_code, int(nr*255), int(ng*255), int(nb*255)

def extract_hue_clustered_palette(image_path):
    cmd = f'magick "{image_path}" -resize 120x120! -colors 48 -format "%c" histogram:info:'
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout
    
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
            
            if v < 0.28 or s < 0.20:
                continue
                
            bin_idx = int((h * 360) // 30) % 12
            weight = count * (s ** 2.2) * (v ** 2.0)
            
            bins[bin_idx].append({
                'hex': hex_col,
                'count': count,
                'r': int(r * 255),
                'g': int(g * 255),
                'b': int(b * 255),
                'h': h,
                's': s,
                'v': v,
                'weight': weight
            })
            
    bin_scores = []
    for idx, b in enumerate(bins):
        if not b:
            continue
        total_weight = sum(item['weight'] for item in b)
        best_col = max(b, key=lambda x: (x['s'] ** 2.0) * (x['v'] ** 1.8))
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
        raw_p = {'r': 239, 'g': 68, 'b': 68}
        raw_s = {'r': 245, 'g': 158, 'b': 11}
        
    p_hex, pr, pg, pb = boost_color_for_readability(raw_p['r'], raw_p['g'], raw_p['b'], min_s=0.55, target_v=0.92)
    s_hex, sr, sg, sb = boost_color_for_readability(raw_s['r'], raw_s['g'], raw_s['b'], min_s=0.50, target_v=0.88)
    
    return {
        'hex': p_hex, 'r': pr, 'g': pg, 'b': pb
    }, {
        'hex': s_hex, 'r': sr, 'g': sg, 'b': sb
    }

def apply_dynamic_theme(image_path=None):
    if not is_shinsekai_active():
        return

    if not image_path:
        image_path = get_current_background()
        
    if not os.path.exists(image_path):
        return
        
    primary, secondary = extract_hue_clustered_palette(image_path)
    p_hex_clean = primary['hex'].lstrip('#').upper()
    s_hex_clean = secondary['hex'].lstrip('#').upper()
    
    theme_dirs = [
        os.path.expanduser("~/.config/omarchy/themes/shinsekai"),
        os.path.expanduser("~/.local/state/omarchy/current/theme")
    ]
    
    # 1. Update chromium.theme
    rgb_str = f"{primary['r']},{primary['g']},{primary['b']}\n"
    
    # 2. Update colors.toml (clean white general text + dynamic wallpaper accent for cursor/prompts/highlights)
    colors_toml = f"""accent = "{primary['hex']}"
cursor = "{secondary['hex']}"
foreground = "#f8fafc"
background = "#090d16"
selection_foreground = "#090d16"
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

    # 3. Update SwayOSD (Volume, Brightness, CapsLock UI)
    swayosd_css = f"""/* Shinsekai SwayOSD Volume & Brightness UI */
@define-color background-color #090d16;
@define-color border-color {primary['hex']};
@define-color label #f8fafc;
@define-color image {primary['hex']};
@define-color progress {primary['hex']};

window {{
  border-radius: 14px;
  border: 2px solid @border-color;
  background-color: alpha(@background-color, 0.92);
  box-shadow: 0 8px 30px rgba(0,0,0,0.6);
  padding: 10px;
}}
label  {{ color: @label; }}
image  {{ color: @image; }}
progressbar {{ border-radius: 12px; }}
progress {{ background-color: @progress; border-radius: 12px; }}
"""

    # 4. Update foot.ini
    foot_ini = f"""[colors-dark]
foreground=f8fafc
background=090d16
selection-foreground=090d16
selection-background={p_hex_clean.lower()}

cursor=090d16 {s_hex_clean.lower()}

regular0=090d16
regular1=ef4444
regular2=10b981
regular3=f59e0b
regular4={p_hex_clean.lower()}
regular5={s_hex_clean.lower()}
regular6=06b6d4
regular7=e2e8f0

bright0=334155
bright1=f87171
bright2=34d399
bright3=fbbf24
bright4={p_hex_clean.lower()}
bright5={s_hex_clean.lower()}
bright6=67e8f9
bright7=ffffff
"""

    # 5. Update Starship prompt
    starship_toml = f"""add_newline = true
command_timeout = 200
format = "[$directory$git_branch$git_status]($style)$character"

[character]
error_symbol = "[✗](bold #ef4444)"
success_symbol = "[❯](bold {primary['hex']})"

[directory]
truncation_length = 2
truncation_symbol = "…/"
repo_root_style = "bold {primary['hex']}"
repo_root_format = "[$repo_root]($repo_root_style)[$path]($style)[$read_only]($read_only_style) "

[git_branch]
format = "[$branch]($style) "
style = "italic {secondary['hex']}"

[git_status]
format     = '[$all_status]($style)'
style      = "{primary['hex']}"
ahead      = "⇡${{count}} "
diverged   = "⇕⇡${{ahead_count}}⇣${{behind_count}} "
behind     = "⇣${{count}} "
conflicted = " "
up_to_date = " "
untracked  = "? "
modified   = " "
stashed    = ""
staged     = ""
renamed    = ""
deleted    = ""
"""

    # 6. Update Walker launcher CSS
    walker_css = f"""@define-color background #090d16;
@define-color foreground #f8fafc;
@define-color selected-background {primary['hex']};
@define-color selected-foreground #090d16;
@define-color border {primary['hex']};

#window {{
  background-color: transparent;
}}

#box {{
  background-color: alpha(@background, 0.94);
  border: 2px solid @border;
  border-radius: 14px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.7);
  padding: 16px;
}}

#search {{
  background-color: #0f172a;
  border: 1px solid alpha({primary['hex']}, 0.4);
  border-radius: 8px;
  color: @foreground;
  padding: 10px;
}}

#item:selected {{
  background-color: @selected-background;
  color: @selected-foreground;
  border-radius: 8px;
}}
"""

    # 7. Update Lock Screen Tokens (Hyprlock & Omarchy Shell Lock)
    shell_lock_toml = f"""text             = "#f8fafc"
placeholder      = "#64748b"
text-error       = "#ef4444"
border           = "#1e293b"
border-active    = "{primary['hex']}"
border-error     = "#ef4444"
"""

    hyprlock_conf = f"""# Shinsekai (新世界) Dynamic Lock Screen
$color           = rgb(090D16)
$inner_color     = rgba(9, 13, 22, 0.88)
$outer_color     = rgb({p_hex_clean})
$accent_color    = rgb({s_hex_clean})
$font_color      = rgb(F8FAFC)
$placeholder_color = rgba(248, 250, 252, 0.50)
$check_color     = rgb({s_hex_clean})

background {{
    blur_passes = 3
    blur_size   = 8
    vibrancy    = 0.90
    vibrancy_darkness = 0.25
}}
"""

    # Write configs across directories
    for d in theme_dirs:
        if os.path.exists(d):
            with open(os.path.join(d, "chromium.theme"), "w") as f:
                f.write(rgb_str)
            with open(os.path.join(d, "colors.toml"), "w") as f:
                f.write(colors_toml)
            with open(os.path.join(d, "swayosd.css"), "w") as f:
                f.write(swayosd_css)
            with open(os.path.join(d, "foot.ini"), "w") as f:
                f.write(foot_ini)
            with open(os.path.join(d, "starship.toml"), "w") as f:
                f.write(starship_toml)
            with open(os.path.join(d, "walker.css"), "w") as f:
                f.write(walker_css)
            with open(os.path.join(d, "shell.lock.toml"), "w") as f:
                f.write(shell_lock_toml)
            with open(os.path.join(d, "hyprlock.conf"), "w") as f:
                f.write(hyprlock_conf)

            # Keep shell.toml in sync if present
            shell_toml_path = os.path.join(d, "shell.toml")
            if os.path.exists(shell_toml_path):
                try:
                    with open(shell_toml_path, "r") as sf:
                        st_content = sf.read()
                    st_content = re.sub(r'(\[lock\][^\[]*?border-active\s*=\s*")[^"]*(")', rf'\g<1>{primary["hex"]}\g<2>', st_content)
                    with open(shell_toml_path, "w") as sf:
                        sf.write(st_content)
                except Exception:
                    pass

    # Also update user live configs
    user_swayosd = os.path.expanduser("~/.config/swayosd/style.css")
    if os.path.exists(os.path.dirname(user_swayosd)):
        with open(user_swayosd, "w") as f:
            f.write(swayosd_css)

    user_starship = os.path.expanduser("~/.config/starship.toml")
    with open(user_starship, "w") as f:
        f.write(starship_toml)

    # 8. Update Hyprland Look & Feel
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
    theme_dir = os.path.expanduser("~/.config/omarchy/themes/shinsekai")
    with open(os.path.join(theme_dir, "hyprland.lua"), "w") as f:
        f.write(hypr_lua)
        
    looknfeel_path = os.path.expanduser("~/.config/hypr/looknfeel.lua")
    with open(looknfeel_path, "w") as f:
        f.write(hypr_lua)

    # 9. Broadcast to Top Bar / QuickShell via IPC
    colors_payload = base64.b64encode(colors_toml.encode('utf-8')).decode('utf-8')
    subprocess.run(f"omarchy-shell -q shell applyTheme '{colors_payload}' '' >/dev/null 2>&1", shell=True)

    # 10. Update Browser, Terminal, Templates & Hyprland
    subprocess.run("omarchy-theme-set-browser >/dev/null 2>&1", shell=True)
    subprocess.run("brave --refresh-platform-policy --no-startup-window >/dev/null 2>&1 &", shell=True)
    subprocess.run("chromium --refresh-platform-policy --no-startup-window >/dev/null 2>&1 &", shell=True)
    subprocess.run("omarchy-theme-set-templates >/dev/null 2>&1", shell=True)
    subprocess.run("omarchy-theme-set-foot >/dev/null 2>&1", shell=True)
    subprocess.run("omarchy-restart-terminal >/dev/null 2>&1", shell=True)
    subprocess.run("hyprctl reload >/dev/null 2>&1", shell=True)
    
    print(f"[Shinsekai Dynamic] Synchronized All UI & Lockscreen: {os.path.basename(image_path)} -> Primary: {primary['hex']} | Secondary: {secondary['hex']}", flush=True)

if __name__ == "__main__":
    img = sys.argv[1] if len(sys.argv) > 1 else None
    apply_dynamic_theme(img)
