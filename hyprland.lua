-- Shinsekai (新世界) Anime Theme for Hyprland
-- Glowing 3-tone Sakura Rose -> Sunset Violet -> Celestial Azure gradient borders
local active_border_color = { colors = { "rgba(f43f5eee)", "rgba(c084fcee)", "rgba(38bdf8ee)" }, angle = 45 }
local inactive_border_color = "rgba(0f172a88)"

hl.config({
  general = {
    gaps_in = 5,
    gaps_out = 10,
    border_size = 2,
    col = {
      active_border = active_border_color,
      inactive_border = inactive_border_color,
    },
  },
  decoration = {
    rounding = 12,
    active_opacity = 0.96,
    inactive_opacity = 0.88,
    dim_inactive = true,
    dim_strength = 0.12,
    blur = {
      enabled = true,
      size = 8,
      passes = 3,
      new_optimizations = true,
      xray = false,
      ignore_opacity = false,
      noise = 0.015,
      contrast = 0.97,
      brightness = 0.90,
      popups = true,
      popups_ignorealpha = 0.6,
    },
    shadow = {
      enabled = true,
      range = 22,
      render_power = 3,
      color = "rgba(090d16cc)",
      color_inactive = "rgba(00000055)",
    },
  },
  animations = {
    enabled = true,
    bezier = {
      "shinsekaiEase, 0.16, 1, 0.3, 1",
      "shinsekaiLinear, 0, 0, 1, 1",
    },
    animation = {
      "windows, 1, 4.5, shinsekaiEase, popin 85%",
      "windowsOut, 1, 3.5, shinsekaiEase, popin 85%",
      "windowsMove, 1, 4, shinsekaiEase",
      "border, 1, 6, default",
      "borderangle, 1, 40, shinsekaiLinear, loop",
      "fade, 1, 3, default",
      "workspaces, 1, 4.5, shinsekaiEase, slide",
    },
  },
  group = {
    col = {
      border_active = active_border_color,
      border_inactive = inactive_border_color,
    },
  },
})
