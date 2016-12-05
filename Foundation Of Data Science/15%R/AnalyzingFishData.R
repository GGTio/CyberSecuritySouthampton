mydata = read.table("fish.txt")
summary(mydata)

quantile(mydata$V1)
quantile(mydata$V2)

#chart
stripchart(mydata$V1)
stripchart(mydata$V2)

#chart with stacked boxes
stripchart(mydata$V1, method="stack")
stripchart(mydata$V2, method="stack")

#chart with dispersed values
stripchart(mydata$V1, method="jitter")
stripchart(mydata$V2, method="jitter")

#title for last plot
title("test title", xlab = "x def")

#title inside plot
stripchart(mydata$V1,main='test A', xlab = 'test B', ylab = 'test C')

#histogram
hist(mydata$V1,main="Distribution of the hours of catch", xlab = "Day time")

#histogram with differents breaks
hist(mydata$V1,main="Distribution of the hours of catch", xlab = "Day time",breaks = 10)
hist(mydata$V1,main="Distribution of the hours of catch", xlab = "Day time",breaks = 24)
hist(mydata$V1,main="Distribution of the hours of catch", xlab = "Day time",breaks = 48)
hist(mydata$V2,main="Distribution of the hours of catch", xlab = "Day time",breaks = 10)
hist(mydata$V2,main="Distribution of the hours of catch", xlab = "Day time",breaks = 24)
hist(mydata$V2,main="Distribution of the hours of catch", xlab = "Day time",breaks = 48)

#histogram with limited scope
hist(mydata$V1,main="Distribution of the hours of catch", xlab = "Day time",breaks = 48,xlim=c(0,10))
hist(mydata$V2,main="Distribution of the hours of catch", xlab = "Day time",breaks = 48,xlim=c(2,3))

#boxplot
boxplot(mydata$V1,main='Summary visualization')
boxplot(mydata$V2)

#combination of plots
hist(mydata$V1,main="Distribution of the hours of catch", xlab = "Day time",breaks = 48)
boxplot(mydata$V1,horizontal = TRUE,add = TRUE, axes = FALSE, at = 3)
stripchart(mydata$V1,add = TRUE, method="stack")

#plots of 2 variables combined (x,y)
plot(mydata$V1,mydata$V2,main="Distribution of catches", xlab = "Daytime (h.%h)", ylab = "Size of the catch(kg)")
boxplot(mydata$V1,mydata$V2)
#corelation
cor(mydata$V1,mydata$V2)

#multiple datasets
plot(mydata$V1,mydata$V2,pch=1,col=1,main="Distribution",xlab="daytime(h)",ylab="size(kg)",xlim=c(0,30),ylim=c(0,5))
points(10.0,4.0,col=4,pch=4)

#adding a legend
legend(25.5,1,c("Original","special"),col=c(1,4),pch=c(1,4))

#multiple plots
plot(mydata$V1,mydata$V2,pch=1,col=1,main="Distribution",xlab="daytime(h)",ylab="size(kg)",xlim=c(0,30),ylim=c(0,5))
hist(mydata$V1,main="Distribution of the hours of catch", xlab = "Day time",breaks = 48)

#density plots
smoothScatter(mydata$V1,mydata$V2)
grid(4,3)

#density of prob
d = density(mydata$V1)
e = density(mydata$V2)

plot(d)
plot(e)


hist(mydata$V1,main="Distribution of the hours of catch", xlab = "Day time",breaks = 200)
plot(lines(d,type="o"))

#MODE FUNCTION (value with the highest occurences)
getmode <- function(v) {
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v, uniqv)))]
}

#mode
getmode(mydata$V1)
getmode(mydata$V2)

#geometrical mean
exp(mean(log(mydata$V1)))
exp(mean(log(mydata$V2)))

#variations
var(mydata$V1)
var(mydata$V2)

#standard deviation
sd(mydata$V1)
sd(mydata$V2)

#IQR
IQR(mydata$V1)
IQR(mydata$V2)

#density
hist(mydata$V1,main="Kernel density estimation for the times of catch",xlab="Daytime (hours)",prob=TRUE,breaks=c(0,seq(2.8,26,2.8)),ylim = c(0,0.06),xlim = c(0,24),xaxt="n")
axis(1,at=c(seq(0,24,4)))
lines(d)
legend(15.2,0.06,c("N = 200","bandwidth = 1.764"))

hist(mydata$V2,main="Kernel density estimation for the weight of catches",xlab="Daytime (hours)",prob=TRUE,breaks=18,ylim = c(0,0.5),xlim = c(0,5),xaxt="n")
axis(1,at=c(seq(0,4.5,0.5)))
lines(e)
legend(0.5,0.5,c("N = 200","bandwidth = 0.3363"))


skewness(mydata$V1)
skewness(mydata$V2)

kurtosis(mydata$V1)
kurtosis(mydata$V2)

#PROJECT
#raw distributions
hist(mydata$V1,main = "Distribution of the times of catch",xlab = "Daytime (hours)",axes = FALSE, ylab = "Count",breaks=c(seq(0,25.2,2.8)),prob =TRUE)
axis(1,at=c(seq(0.0,24.0,4)))
axis(2,at=c(seq(0.0,35.0,5)))
boxplot(mydata$V1,horizontal = TRUE,add = TRUE, axes = FALSE, at=2.5)
lines(d)
hist(mydata$V2,main = "Distribution of the sizes of catch",xlab = "Weight of catches (kg)",axes = FALSE, ylab = "Count",breaks=c(seq(0,4.88,0.61)))
axis(1,at=c(seq(0,4.5,0.25)))
axis(2,at=c(seq(0.0,45,2.5)))
boxplot(mydata$V2,horizontal = TRUE,add = TRUE, axes = FALSE, at=2.5)

#boxplots of (x,y)
n = cut(mydata$V1,24)
plot(n,mydata$V2)
