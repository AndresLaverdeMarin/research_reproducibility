library(tidyverse)
library(sysfonts)
library(showtext)

font_add("Roboto-Regular", "slides/fonts/Roboto-Regular.ttf")
font_add("Roboto-Bold", "slides/fonts/Roboto-Bold.ttf")
font_add("Roboto-Italic", "slides/fonts/Roboto-Italic.ttf")
font_add("Roboto-BoldItalic", "slides/fonts/Roboto-BoldItalic.ttf")

showtext_auto()

scale_data = tibble(score = seq(2, 10, length.out = 200))

scale_score_p = ggplot(scale_data, aes(x = 1, y = score, fill = score)) +
  geom_tile(width = 0.12) +
  scale_fill_gradientn(
    colours = c("#FE0000", "#FFC702", "#32CB00"),
    limits = c(2, 10)
  ) +
  scale_y_continuous(
    breaks = c(2, 6, 10),
    labels = c("2", "6", "10")
  ) +
  annotate("text", x = 1.08, y = 10, label = "High", hjust = 0, size = 10/3, family = "Roboto-Regular") +
  annotate("text", x = 1.08, y = 6, label = "Medium", hjust = 0, size = 10/3, family = "Roboto-Regular") +
  annotate("text", x = 1.08, y = 2, label = "Low", hjust = 0, size = 10/3, family = "Roboto-Regular") +
  labs(
    x = NULL,
    y = "Total transparency score",
    title = "Total transparency score"
  ) +
  coord_cartesian(xlim = c(0.9, 1.45), clip = "off") +
  theme_minimal(base_size = 10) +
  theme(
    legend.position = "none",
    axis.text.x = element_blank(),
    axis.ticks.x = element_blank(),
    panel.grid = element_blank(),
    plot.title = element_text(hjust = 0, family = "Roboto-Bold"),
    axis.title.y = element_blank(),
    text = element_text(family = "Roboto-Regular")# horizontal on top
  )

# Save plot
ggsave("slides/images/scale_score_p.svg", scale_score_p, width = 7.5,   # 7.5 cm for narrow column
       height = 5, 
       units = "cm", dpi = 300,
       device = svglite::svglite,
       )
