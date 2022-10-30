library(tidyverse)
penguins %>% arrange(bill_length_mm)

penguins %>% arrange(-bill_length_mm)

penguins %>% 
  group_by(island) %>% 
  drop_na() %>% 
  summarize(mean_bill_length_mm = mean(bill_length_mm))

penguins %>%
  group_by(island) %>%
  drop_na() %>%
  summarise(min = min(bill_depth_mm))