library(tidyverse)
library(skimr)
library(janitor)

df <- read_csv('hotel_bookings.csv')
head(df)
glimpse(df)
str(df)
summary(df)
colnames(df)
skim_without_charts(df)

trimmed_df <- df %>% select('hotel', 'is_canceled', 'lead_time')
view(trimmed_df)

trimmed_df %>% 
  select('hotel', 'is_canceled', 'lead_time') %>% 
  rename(hotel_type = hotel)

view(trimmed_df)
