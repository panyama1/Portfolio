## The following program visualizes data by using the R programming language with inspections.csv and violations.csv.

## Reading in the data and having a peek
library(tidyverse)

inspections <- read_csv("../input/inspections.csv")
violations <- read_csv("../input/violations.csv")

all <- inspections %>%
  inner_join(violations, by="serial_number")

glimpse(all)

## Transform `activity_date` column
library(lubridate)

all <- all %>%
  mutate(activity_date = ymd(activity_date),
         activity_month = ceiling_date(activity_date, "month"))
         
options(repr.plot.width = 8, repr.plot.height = 6)

all %>%
  group_by(activity_month) %>%
  summarise(n_violations = n()) %>%
  ggplot(aes(activity_month, n_violations)) + 
    geom_line() + 
      scale_x_date(date_breaks="3 months",date_labels = "%b-%y") + 
      theme(axis.text.x = element_text(angle = 45)) + 
      labs(title="Monthly count of health code violations")
      
## Get the top ten health code violation descriptions
top_10_violations <- names(sort(table(all$violation_description), decreasing = T)[1:10])

### Get the month of the violations
all <- all %>% mutate(month = month(activity_month, label = T))

monthly_violations <- all %>%
    filter(violation_description %in% top_10_violations) %>%
    group_by(violation_description, month) %>%
    summarise(monthly_violation_count = n())

## Visualize the data
options(repr.plot.width = 10, repr.plot.height = 6)

library(viridis)
ggplot(monthly_violations, aes(x = month, 
                               y = str_wrap(violation_description,40),
        fill = monthly_violation_count)) + 
    geom_tile() +
    scale_fill_viridis(name = "Number of Violations") +
    labs(y = "Violation Description",
       x = "Month of Violation",
       title = "Monthly trends of the top ten health code violations") + 
    theme(axis.text.x = element_text(angle = 45), legend.position = "none")
    
## Aggregate the data by ZIP Code
violations_by_zip <- all %>% 
  group_by(facility_zip) %>%
  summarise(n_violations = n())
  
## Write the data to a CSV file which will be accessible from the "Output" tab of the Kernel
write.csv(violations_by_zip, "violations_by_zip.cs", row.names=F)
