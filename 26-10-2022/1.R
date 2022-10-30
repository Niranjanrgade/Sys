data('ToothGrowth')
view(ToothGrowth)
f_tg <- filter(ToothGrowth, dose==0.5)
view(f_tg)
arrange(f_tg, len)

f_tg <- ToothGrowth %>%
  filter(dose==0.5) %>% 
  group_by(supp) %>%
  arrange(len)