-- Shinsekai Dynamic Anime Theme for Hyprland
local active_border_color = { colors = { "rgba(2cf535ee)", "rgba(b528e0ee)" }, angle = 45 }
local inactive_border_color = "rgba(0f172a66)"

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
    rounding = 10,
    active_opacity = 0.96,
    inactive_opacity = 0.88,
    dim_inactive = true,
    dim_strength = 0.12,
    blur = {
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
    },
    shadow = {
      enabled = true,
      range = 18,
      render_power = 3,
      color = "rgba(00000088)",
      color_inactive = "rgba(00000055)",
    },
  },
  animations = {
    enabled = true,
    bezier = {
      "shinsekaiEase, 0.16, 1, 0.3, 1",
    },
    animation = {
      "windows, 1, 4, shinsekaiEase, popin 85%",
      "windowsOut, 1, 3, default, popin 85%",
      "windowsMove, 1, 4, shinsekaiEase",
      "border, 1, 6, default",
      "fade, 1, 3, default",
      "workspaces, 1, 4, shinsekaiEase, slide",
    },
  },
  group = {
    col = {
      border_active = active_border_color,
      border_inactive = inactive_border_color,
    },
  },
})
