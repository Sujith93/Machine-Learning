#H0 no association
#

#H0: Variable A and Variable B are independent. 
#HA: Variable A and Variable B are not independent.(some relationship)

# rejecting the null hypothesis when the P-value is less than the significance level.
# p < 0.05 Thus, we conclude that there is a relationship between variables 

?chisq.test

library(MASS)
head(survey)
View(survey)
summary(survey)
nrow(survey)  # 237


table(survey$Exer,survey$Smoke)
addmargins(table(survey$Exer,survey$Smoke))

chisq.test(survey$Exer,survey$Smoke)
#p=.4828 
#failed to reject H0  (there is no relationship)

