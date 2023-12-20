library(tidyverse)
library(ggthemes)
library(patchwork)
setwd("C:/Users/meala/Documents/R Data Work")

#AreaSD
set.seed(259)
AreaSD_hours <- rnorm(100, mean = 90, sd = 15)
AreaSD_Income <-  abs(AreaSD_hours * (rnorm(100, 120,10))) 
SD <- ggplot(data.frame(AreaSD_hours, AreaSD_Income), aes(x = AreaSD_hours, y = AreaSD_Income)) + 
                  geom_point(color="darkgreen")  + labs(title = "Area SD", x = "Hours", y = "Income")+theme_classic()

#AreaLA
set.seed(259)
AreaLA_hours <- rnorm(90, mean = 100, sd = 16)
AreaLA_Income <-  abs(AreaLA_hours * (rnorm(90, 100,8)))
LA<- ggplot(data.frame(AreaLA_hours, AreaLA_Income), aes(x = AreaLA_hours, y = AreaLA_Income)) + 
                  geom_point(color="darkblue")  + labs(title = "Area LA", x = "Hours", y = "Income")+theme_classic()


#AreaB
set.seed(259)
AreaB_hours <- rnorm(110, mean = 120, sd = 20)
AreaB_Income <- abs(AreaB_hours * (rnorm(110, 75,6)))
Berkeley <- ggplot(data.frame(AreaB_hours, AreaB_Income), aes(x = AreaB_hours, y = AreaB_Income)) + 
                  geom_point(color="darkorange")  + labs(title = "Area SF", x = "Hours", y = "Income")+theme_classic()


#Irvine
set.seed(259)
AreaI_hours <- rnorm(80, mean = 170, sd = 16)
AreaI_Income <-  abs(AreaI_hours * (rnorm(80, 50,5)))

Irvine <- ggplot(data.frame(AreaI_hours, AreaI_Income), aes(x = AreaI_hours, y = AreaI_Income)) + 
                  geom_point(color="darkred")  + labs(title = "Area Irvine", x = "Hours", y = "Income")+theme_classic()

#Riverside
set.seed(259)
AreaR_hours <- rnorm(75, mean = 190, sd = 14)
AreaR_Income <-  abs(AreaR_hours * (rnorm(65, 45,4)))
Riverside <- ggplot(data.frame(AreaR_hours, AreaR_Income), aes(x = AreaR_hours, y = AreaR_Income)) + 
                  geom_point(color="brown")  + labs(title = "Area Riverside", x = "Hours", y = "Income")+theme_classic()

#rm(list=ls())
#plot all the plots together
SD
LA
Berkeley
Irvine
Riverside

SD+LA + Berkeley + Irvine + Riverside + plot_layout(ncol = 2)

#make a function to run linear regression 

AreaSD <- lm(AreaSD_Income~AreaSD_hours)
summary(AreaSD)
AreaLA <- lm(AreaLA_Income~AreaLA_hours)
summary(AreaLA)
AreaB <- lm(AreaB_Income~AreaB_hours)
summary(AreaB)
AreaI <- lm(AreaI_Income~AreaI_hours)
summary(AreaI)
AreaR <- lm(AreaR_Income~AreaR_hours)
summary(AreaR)

AreaSD <- data.frame(Area = "AreaSD",Hours= AreaSD_hours,Income=AreaSD_Income)
AreaLA <- data.frame(Area = "AreaLA",Hours= AreaLA_hours,Income=AreaLA_Income)
AreaB <- data.frame(Area = "AreaB",Hours= AreaB_hours,Income=AreaB_Income)
AreaI <- data.frame(Area = "AreaI",Hours= AreaI_hours,Income=AreaI_Income)
AreaR <- data.frame(Area = "AreaR",Hours= AreaR_hours,Income=AreaR_Income)

All <- rbind(AreaSD,AreaLA,AreaB,AreaI,AreaR)
summary(lm(data=All, Income~Hours))

p <- ggplot(data=All, aes(x=Hours, y=Income)) + geom_point()+geom_point(color="pink")
p<- p + theme_classic()

p1 <- ggplot(data=All, aes(x=Hours, y=Income, color=Area)) + geom_point()+geom_smooth(method = "lm", se = FALSE, color = "red")
p1<- p1 + theme_classic()

p2 <- ggplot(data=All, aes(x=Hours, y=Income, color=Area)) + geom_point()+geom_smooth(method = "lm", se = FALSE)
p2<- p2 + theme_classic()

p+p1+p2

Area_reg <- lm(data=All, Income~Hours+Area)
summary(Area_reg)
