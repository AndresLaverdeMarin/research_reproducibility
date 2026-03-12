library(tidyverse)
library(showtext)

# Load Roboto font from Google Fonts
sysfonts::font_add_google(name = "Roboto", family = "roboto")

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
  annotate("text", x = 1.08, y = 10, label = "High transparency", hjust = 0, size = 10/3) +
  annotate("text", x = 1.08, y = 6, label = "Medium transparency", hjust = 0, size = 10/3) +
  annotate("text", x = 1.08, y = 2, label = "Low transparency", hjust = 0, size = 10/3) +
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
    plot.title = element_text(hjust = 0, face = "bold"),
    axis.title.y = element_blank(),
    text = element_text(family = "Roboto")# horizontal on top
  )

# Save plot
ggsave("slides/images/scale_score_p.svg", scale_score_p,width = 7.5,   # 7.5 cm for narrow column
       height = 7, 
       units = "cm")
