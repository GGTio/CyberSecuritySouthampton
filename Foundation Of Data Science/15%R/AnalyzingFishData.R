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
hist(mydata$V1,main="Distribution of the hours of catch(10)", xlab = "Day time",breaks = 10)
hist(mydata$V1,main="Distribution of the hours of catch(24)", xlab = "Day time",breaks = 24)
hist(mydata$V1,main="Distribution of the hours of catch(48)", xlab = "Day time",breaks = 48)
hist(mydata$V2,main="Distribution of the hours of catch(10)", xlab = "Day time",breaks = 10)
hist(mydata$V2,main="Distribution of the hours of catch(24)", xlab = "Day time",breaks = 24)
hist(mydata$V2,main="Distribution of the hours of catch(48)", xlab = "Day time",breaks = 48)

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
plot(mydata$V1,mydata$V2,main="Distribution of catches during the day", xlab = "Daytime (h.%h)", ylab = "Size of the catch(kg)")
boxplot(mydata$V1,mydata$V2)
#corelation
cor(mydata$V1,mydata$V2)

#multiple datasets
plot(mydata$V1,mydata$V2,pch=1,col=1,main="Distribution",xlab="daytime(h)",ylab="size(kg)",xlim=c(0,30),ylim=c(0,5))
points(10.0,4.0,col=4,pch=4)

#adding a legend
legend(25.5,1,c("Original","special"),col=c(1,4),pch=c(1,4))

#multiple plots
plot(mydata$V1,mydata$V2,pch=1,col=1,main="Distribution",xlab="daytime(h)",ylab="size(kg)",xlim=c(0,24),ylim=c(0,5),xaxt="n")
axis(1,seq(0,24,1))
abline(21.0,add=TRUE)
hist(mydata$V1,main="Distribution of the hours of catch", xlab = "Day time",breaks = 48)

#density plots
smoothScatter(mydata$V1,mydata$V2,xlab = "Daytime",ylab = "Weights")
grid(4,3)

#density of prob
d = density(mydata$V1)
e = density(mydata$V2)

plot(d)
plot(e)


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

library(e1071) 
skewness(mydata$V1)
skewness(mydata$V2)

kurtosis(mydata$V1)
kurtosis(mydata$V2)

#PROJECT
#Part 1
#distributions
#Time of catches
hist(mydata$V1,main = "Distribution of the times of catch",xlab = "Daytime (hours)",xaxt="n", ylab = "Count",breaks=c(seq(0,25.2,2.8)),col = "lightgrey")
axis(1,at=c(seq(0,24,4)))
boxplot(mydata$V1,horizontal = TRUE,add = TRUE, axes = FALSE, at=2.5)
#.abline(v = median(mydata$V1), col = 2)
abline(v = mean(mydata$V1), col = 3)
abline(v = mean(mydata$V1)+sd(mydata$V1), col = 4)
abline(v = mean(mydata$V1)-sd(mydata$V1), col = 4)
legend(16,35,c("mean","std deviation"),col=c(3,4),lty=c(1,1))

me = mean(mydata$V1)
std = sd(mydata$V1)
size = 200
err =  1.96*std/sqrt(size)

right = me+err
left = me-err

md = mean(mydata$V2)
stdd = sd(mydata$V2)
erro =  1.96*stdd/sqrt(size)

right2 = md+erro
left2 = md-erro

#Weights of catches
hist(mydata$V2,main = "Distribution of the sizes of catch",xlab = "Weight of catches (kg)",axes = FALSE, ylab = "Count",breaks=c(seq(0,4.88,0.61)),col = "lightgrey")
axis(1,at=c(seq(0,4.5,0.25)))
axis(2,at=c(seq(0.0,45,2.5)))
boxplot(mydata$V2,horizontal = TRUE,add = TRUE, axes = FALSE, at=2.5)
#abline(v = median(mydata$V2), col = 2)
abline(v = mean(mydata$V2), col = 3)
abline(v = mean(mydata$V2)+sd(mydata$V2), col = 4)
abline(v = mean(mydata$V2)-sd(mydata$V2), col = 4)

legend(3.25,44.5,c("mean","std deviation"),col=c(3,4),lty=c(1,1))


#densities
par(mar=c(5, 4, 4, 8) + 0.1)
hist(mydata$V1,main="Kernel density estimation for the times of catch",xlab="Daytime (hours)",breaks=c(0,seq(2.8,26,2.8)),xlim = c(0,24),axes = FALSE,col="lightblue")
axis(1,at=c(seq(0,24,4)))
axis(2,at=c(seq(0,35,5)))
par(new = T)
plot(d,type="l",col="red",main="",xlim=c(0,24),xlab = "",ylab = "",axes=FALSE)
axis(4,at=c(seq(0,0.06,0.01)))
mtext("Density", side=4, line=3)
legend(16.5,0.049,c("density"),col=(2),lty=c(1,1))

par(mar=c(5, 4, 4, 8) + 0.1)
hist(mydata$V2,main="Kernel density estimation for the weight of catches",xlab="Daytime (hours)",breaks=c(seq(0,4.88,0.61)),xlim = c(0,5),axes=FALSE,col="lightblue")
axis(1,at=c(seq(0,4.5,0.5)))
axis(2,at=c(seq(0,40,5)))
par(new = T)
plot(e,type="l",col="red",main="",xlim=c(0,5),xlab = "",ylab = "",axes=FALSE)
axis(4,at=c(seq(0,0.35,0.05)))
mtext("Density", side=4, line=3)

#Part2
n = cut(mydata$V1,breaks = 0:24,labels = 0:23)
n1 = cut(mydata$V1,breaks = 0:10,labels = 0:9)
n2 = cut(mydata$V1,breaks = 11:24,labels = 11:23)
plot(n1,mydata$V2,col=2,xaxt="n",xlim = c(0,24),add=TRUE)
abline(h=median(mydata$V2))
axis(1,seq(0,24,1))
plot(n2,mydata$V2,add=TRUE,col=3,xlim = c(0,24))

final = rbind(n1,n2)


n = cut(mydata$V1,breaks = 0:24)
plot(n,mydata$V2,xaxt="n",col=4,main="Correlation between Time of catch and weight")
axis(1,seq(0,24,1))
getwd()

