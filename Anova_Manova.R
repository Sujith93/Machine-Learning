


#H0: All group means are equall mu1=mu2=mu3 .
#HA: At least one of the means is different .


# P<0.05 then we can reject the null hypohtesis(equal means).
#we require the P value to be less then .05 to be considered statistically significant.


#From this we can conclude that if your goal is to describe independent variable you only need 
#to do a regression on * variables, forgo gathering all the other variables.

#####################################################################################
#One way anova
#####################################################################################
data(iris)
str(iris)

#both numerical
aov1 <- aov(Sepal.Length ~ Sepal.Width, data = iris)
summary(aov1)



aov2 <- aov(Petal.Length ~ Petal.Width, data = iris)
summary(aov2)

#D-numeric,ID-factor
aov3 <- aov(Sepal.Length ~ Species, data = iris)
summary(aov3)

TukeyHSD(aov3)


#####################################################################################
#two way anova
#####################################################################################
aov2way <-
  aov(Petal.Width ~ Sepal.Length + Sepal.Width, data = iris)
summary(aov2way)

#####################################################################################
#three way anova
#####################################################################################
aov2way1 <-
  aov(Petal.Width ~ Sepal.Length + Sepal.Width + Petal.Length, data = iris)
summary(aov2way1)



aov2way2 <-
  aov(Petal.Width ~ Sepal.Length * Sepal.Width * Petal.Length, data = iris)
summary(aov2way2)



#####################################################################################
#Manova
#####################################################################################
#works for factors along with numeric
#alone factors won't work

manova <-
  manova(cbind(Species, Petal.Length) ~ Sepal.Length * Sepal.Width,
         data = iris)
summary(manova)




#Analysis of covariance (ANCOVA) combines features of both ANOVA and regression

