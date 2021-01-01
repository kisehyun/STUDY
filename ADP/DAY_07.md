---
title: "DAY_07"
author: "kisehyun"
date: '2020 12 1 '
output: html_document
---



# **시각화**

## **산점도**

#### **plot(x, y, xlab, ylab, main, pch, cex, col, xlim, ylim, type)**


```r
data(Cars93)
data(iris)
plot(Cars93$Length, Cars93$Weight, main = 'Cars93', xlab = 'Length', ylab = 'Weight', xlim = c(130, 230), ylim = c(1600, 4400), pch = '*', cex = 1.3, col = 'red')
```

![plot of chunk unnamed-chunk-1](figure/unnamed-chunk-1-1.png)

## **그래프 서식**
#### **par(mfrow = c(nr, nc))**


```r
par(mfrow = c(1,2))
plot(Cars93$Length, Cars93$Weight, main = 'Cars93', col = 'red', pch = '*', cex = 1.2)
plot(Cars93$Length, Cars93$Price, main = 'Cars93', col = 'blue', pch = '#', cex = .8)
```

![plot of chunk unnamed-chunk-2](figure/unnamed-chunk-2-1.png)

## **그래프**

#### **plot** 함수로 **빈 좌표평면**을 생성한 후 그려야함
#### **points(x, y = NULL, pch, cex, col)** = **점그래프**

```r
data(iris)
plot(NULL, type = 'n', xlim = c(0, 7), ylim = c(0,3),xlab = 'Petal.Length', ylab = 'Petal.Width') # type = 'n'은 빈 그래프 생성
points(iris$Petal.Length, iris$Petal.Width, cex = .5)
```

![plot of chunk unnamed-chunk-3](figure/unnamed-chunk-3-1.png)

#### **lines(x, y = NULL, lty, lwd, col,...)** = **선그래프**

```r
plot(cars, main = 'Stopping Distance versus Speed', pch = '*', col = 'blue', cex = 1.5)
lines(lowess(cars), col = 'red', lty = 9, lwd = 2)
```

![plot of chunk unnamed-chunk-4](figure/unnamed-chunk-4-1.png)

#### **abline(a = NULL, b = NULL, h = NULL, v = NULL, coef = NULL, reg = NULL,...)**= **직선그래프**

```r
plot(cars, main = 'Cars Data')
abline(v = median(cars$speed), lty = 3, col = 'red')
abline(h = median(cars$dist), lty = 5, col = 'blue')
```

![plot of chunk unnamed-chunk-5](figure/unnamed-chunk-5-1.png)

#### **curve(expr, from = NULL, to = NULL,...)**은 **곡선 그래프**이다. 

```r
curve(dnorm(x, mean = 0, sd = 1), from = -3, to = 3, xla = 'x', ylab = 'density', main=  'curve of dnorm')
```

![plot of chunk unnamed-chunk-6](figure/unnamed-chunk-6-1.png)

#### **막대그래프**는 **barplot(height, names.arg, space, horiz, ....)**


```r
barplot(table(Cars93$Origin), ylim = c(1,50), xlab = 'Origin', ylab = 'Count', main = 'Origin of Cars93')
```

![plot of chunk unnamed-chunk-7](figure/unnamed-chunk-7-1.png)


```r
barplot(table(Cars93$Origin, Cars93$Cylinders), beside = F, ylim = c(0,60), legend = T)
```

![plot of chunk unnamed-chunk-8](figure/unnamed-chunk-8-1.png)


```r
barplot(table(Cars93$Origin, Cars93$Cylinders), beside = T, ylim = c(0,60), legend = T)
```

![plot of chunk unnamed-chunk-9](figure/unnamed-chunk-9-1.png)

#### **히스토그램** **hist(x, mian, xlab, ylab, breaks, freq, col)**


```r
hist(Cars93$Price, col = 'skyblue', breaks = 30)
```

![plot of chunk unnamed-chunk-10](figure/unnamed-chunk-10-1.png)

#### **파이차트** : **pie(x, labels, col, lty, main)**


```r
pie(table(Cars93$Cylinders), main = '실린더 파이 차트')
```

![plot of chunk unnamed-chunk-11](figure/unnamed-chunk-11-1.png)

#### **산점도 행렬** : **pairs(formula, data, subset...)**

```r
pairs(~Sepal.Length + Sepal.Width + Petal.Length + Petal.Width, data = iris, col = c('red','green','blue')[iris$Species],
      pch = c('*','#','+'))
```

![plot of chunk unnamed-chunk-12](figure/unnamed-chunk-12-1.png)
