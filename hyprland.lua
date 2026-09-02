-- Komorebi Anime Theme - Glowing Neon Gradient Borders & Spring Physics
local active_border_color = { colors = { "rgba(ff3388ee)", "rgba(ff6d00ee)", "rgba(00f0ffee)", "rgba(b344ffee)" }, angle = 45 }
local inactive_border_color = "rgba(0f172a88)"

hl.config({
  general = {
    gaps_in = 6,
    gaps_out = 12,
    border_size = 2,
    col = {
      active_border = active_border_color,
      inactive_border = inactive_border_color,
    },
  },
  decoration = {
    rounding = 12,
    active_opacity = 0.94,
    inactive_opacity = 0.85,
    dim_inactive = true,
    dim_strength = 0.15,
    blur = {
      enabled = true,
      size = 8,
      passes = 3,
      new_optimizations = true,
      xray = false,
      ignore_opacity = false,
      noise = 0.015,
      contrast = 0.95,
      brightness = 0.85,
      popups = true,
    },
    shadow = {
      enabled = true,
      range = 25,
      render_power = 4,
      color = "rgba(ff338844)",
      color_inactive = "rgba(00000066)",
    },
  },
  animations = {
    enabled = true,
    bezier = {
      "animeSpring, 0.34, 1.56, 0.64, 1",
      "animeSmooth, 0.16, 1, 0.3, 1",
    },
    animation = {
      "windows, 1, 5, animeSpring, popin 75%",
      "windowsOut, 1, 4, default, popin 80%",
      "windowsMove, 1, 5, animeSmooth",
      "border, 1, 10, default",
      "fade, 1, 4, default",
      "workspaces, 1, 5, animeSmooth, slide",
    },
  },
  group = {
    col = {
      border_active = active_border_color,
      border_inactive = inactive_border_color,
    },
  },
})
