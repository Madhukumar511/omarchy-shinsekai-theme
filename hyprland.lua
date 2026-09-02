local active_border_color = { colors = { "rgba(ff6d00ee)", "rgba(00b0ffee)", "rgba(ff2a55ee)" }, angle = 45 }
local inactive_border_color = "rgba(111722aa)"

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
    },
    shadow = {
      enabled = true,
      range = 20,
      render_power = 3,
      color = "rgba(ff6d0033)",
    },
  },
  animations = {
    enabled = true,
    bezier = {
      "animeEase, 0.05, 0.9, 0.1, 1.05",
    },
    animation = {
      "windows, 1, 4, animeEase, popin 80%",
      "windowsOut, 1, 4, default, popin 80%",
      "border, 1, 8, default",
      "fade, 1, 4, default",
      "workspaces, 1, 5, animeEase, slide",
    },
  },
  group = {
    col = {
      border_active = active_border_color,
      border_inactive = inactive_border_color,
    },
  },
})
