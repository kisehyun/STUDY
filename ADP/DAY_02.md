---
title: "DAY_02"
author: "kisehyun"
date: '2020 11 23 '
output: html_document
---


# 모의고사 3회 1번 문항

## 1. 통계분석 (사용 데이터 : Carseats)                  



### Q1) Urban변수에 따른 Sales의 차이가 있는지를 통계적으로 검증하기 위한 통계분석을 수행하고, 결과를 해석하시오. 
### (데이터는 정규성을 만족한다고 가정하고 유의수준 0.05 하에서 검정)



```r
data("Carseats")
car = Carseats
str(car)
```

```
## 'data.frame':	400 obs. of  11 variables:
##  $ Sales      : num  9.5 11.22 10.06 7.4 4.15 ...
##  $ CompPrice  : num  138 111 113 117 141 124 115 136 132 132 ...
##  $ Income     : num  73 48 35 100 64 113 105 81 110 113 ...
##  $ Advertising: num  11 16 10 4 3 13 0 15 0 0 ...
##  $ Population : num  276 260 269 466 340 501 45 425 108 131 ...
##  $ Price      : num  120 83 80 97 128 72 108 120 124 124 ...
##  $ ShelveLoc  : Factor w/ 3 levels "Bad","Good","Medium": 1 2 3 3 1 1 3 2 3 3 ...
##  $ Age        : num  42 65 59 55 38 78 71 67 76 76 ...
##  $ Education  : num  17 10 12 14 13 16 15 10 10 17 ...
##  $ Urban      : Factor w/ 2 levels "No","Yes": 2 2 2 2 2 1 2 2 1 1 ...
##  $ US         : Factor w/ 2 levels "No","Yes": 2 2 2 2 1 2 1 2 1 2 ...
```


```r
head(car)
```

```
##   Sales CompPrice Income Advertising Population Price ShelveLoc Age Education Urban  US
## 1  9.50       138     73          11        276   120       Bad  42        17   Yes Yes
## 2 11.22       111     48          16        260    83      Good  65        10   Yes Yes
## 3 10.06       113     35          10        269    80    Medium  59        12   Yes Yes
## 4  7.40       117    100           4        466    97    Medium  55        14   Yes Yes
## 5  4.15       141     64           3        340   128       Bad  38        13   Yes  No
## 6 10.81       124    113          13        501    72       Bad  78        16    No Yes
```


```r
### 결측값 확인
sum(is.na(car))
```

```
## [1] 0
```

### Urban 변수에 따라 Sales의 차이가 존재하는가 ? -> 독립표본 t-test


```r
var.test(Sales ~ Urban, data = car, alternative = 'two.sided')
```

```
## 
## 	F test to compare two variances
## 
## data:  Sales by Urban
## F = 0.9787, num df = 117, denom df = 281, p-value = 0.9072
## alternative hypothesis: true ratio of variances is not equal to 1
## 95 percent confidence interval:
##  0.7276615 1.3423111
## sample estimates:
## ratio of variances 
##          0.9786966
```
#### t-test 전에는 등분산성 만족하는지 확인하기 위해 등분산 검정 수행
등분산 검정 결과 유의확률이 0.9072로 매우 높아 귀무가설을 기각하지 않는다. 즉 두 집단은 등분산 가정을 만족한다고 볼 수 있다.


```r
t.test(Sales ~ Urban, data = car, alternative = 'two.sided', var.equal = TRUE)
```

```
## 
## 	Two Sample t-test
## 
## data:  Sales by Urban
## t = 0.30765, df = 398, p-value = 0.7585
## alternative hypothesis: true difference in means is not equal to 0
## 95 percent confidence interval:
##  -0.5140440  0.7047797
## sample estimates:
##  mean in group No mean in group Yes 
##          7.563559          7.468191
```

독립표본 t-test 수행 결과 검정통계량은 0.30765이고 p-value는 0.7585로 귀무가설을 기가할 수 없다. 즉 두 집단간의 차이는 통계적으로 유의하지 않다고 결론 내릴 수 있다.

### Sales 변수와 CompPrice, Income, Advertising, Population, Price, Age, Education 변수 간의 상관관계 분석


```r
## 1. Sales와 CompPrice 분석
cor(car$Sales, car$CompPrice)
```

```
## [1] 0.06407873
```

```r
cor.test(car$Sales, car$CompPrice)
```

```
## 
## 	Pearson's product-moment correlation
## 
## data:  car$Sales and car$CompPrice
## t = 1.281, df = 398, p-value = 0.2009
## alternative hypothesis: true correlation is not equal to 0
## 95 percent confidence interval:
##  -0.03418779  0.16111814
## sample estimates:
##        cor 
## 0.06407873
```

상관계수는 약 0.064로 두 변수간 상관성이거의 존재하지 않는다. p-value는 0.05 보다 크기 때문에 두 변수간 상관관계는 통계적으로 유의하지 않다.


```r
## 2. Sales와 Adversiting 분석
cor(car$Sales, car$Advertising)
```

```
## [1] 0.2695068
```

```r
cor.test(car$Sales, car$Advertising)
```

```
## 
## 	Pearson's product-moment correlation
## 
## data:  car$Sales and car$Advertising
## t = 5.5832, df = 398, p-value = 4.378e-08
## alternative hypothesis: true correlation is not equal to 0
## 95 percent confidence interval:
##  0.1761088 0.3580956
## sample estimates:
##       cor 
## 0.2695068
```

상관계수는 0.269로 두 변수간의 상관관계는 거의 존재하지 않는다. p-value도 유의수준보다 크기 때문에 두 변수간의 상관관계는 통계적으로 유의하지 않는다.


```r
## 3. Sales와 Income 분석
cor(car$Sales, car$Income)
```

```
## [1] 0.151951
```

```r
cor.test(car$Sales, car$Income)
```

```
## 
## 	Pearson's product-moment correlation
## 
## data:  car$Sales and car$Income
## t = 3.067, df = 398, p-value = 0.00231
## alternative hypothesis: true correlation is not equal to 0
## 95 percent confidence interval:
##  0.05471445 0.24633258
## sample estimates:
##      cor 
## 0.151951
```
두 변수간의 상관관계는 0.151로 매우 낮았으며 p-value가 0.05보다 작아 두 변수간의 상관관계는 통계적으로는 유의하다고 볼 수 있다.


```r
## 4. Sales와 Population 분석
cor(car$Sales, car$Population)
```

```
## [1] 0.05047098
```

```r
cor.test(car$Sales, car$Population)
```

```
## 
## 	Pearson's product-moment correlation
## 
## data:  car$Sales and car$Population
## t = 1.0082, df = 398, p-value = 0.314
## alternative hypothesis: true correlation is not equal to 0
## 95 percent confidence interval:
##  -0.04781737  0.14779132
## sample estimates:
##        cor 
## 0.05047098
```
두 변수간의 상관계수는 0.05로 매우 낮은 수준이었으며 p-value가 0.3으로 유의수준 보다 높아 두 변수간의 상관관계는 통계적으로 유의하다고 볼 수 없다.


```r
## 5. Sales와 Price 분석
cor(car$Sales, car$Price)
```

```
## [1] -0.4449507
```

```r
cor.test(car$Sales, car$Price)
```

```
## 
## 	Pearson's product-moment correlation
## 
## data:  car$Sales and car$Price
## t = -9.912, df = 398, p-value < 2.2e-16
## alternative hypothesis: true correlation is not equal to 0
## 95 percent confidence interval:
##  -0.5203026 -0.3627240
## sample estimates:
##        cor 
## -0.4449507
```

두 변수간의 상관계수는 -0.444로 다소 약한 음의 상관관계를 가진다고 할 수 있으며 p-value가 0.05보다 작아 두 변수간의 상관관계는 통계적으로 유의하다고 할 수 있다.


```r
## 6. Sales와 Age 분석
cor(car$Sales, car$Age)
```

```
## [1] -0.2318154
```

```r
cor.test(car$Sales, car$Age)
```

```
## 
## 	Pearson's product-moment correlation
## 
## data:  car$Sales and car$Age
## t = -4.7542, df = 398, p-value = 2.789e-06
## alternative hypothesis: true correlation is not equal to 0
## 95 percent confidence interval:
##  -0.3225359 -0.1368749
## sample estimates:
##        cor 
## -0.2318154
```
두 변수간의 상관계수는 -0.231로 상관관계는 거의 존재하지 않는다고 볼 수 있으며 p-value가 0.05 보다 작으므로 두 변수간의 상관관계는 통계적으로 유의하다고 볼 수 있다.


```r
## 7. Sales 와 Education 분석
cor(car$Sales, car$Education)
```

```
## [1] -0.05195524
```

```r
cor.test(car$Sales, car$Education)
```

```
## 
## 	Pearson's product-moment correlation
## 
## data:  car$Sales and car$Education
## t = -1.0379, df = 398, p-value = 0.2999
## alternative hypothesis: true correlation is not equal to 0
## 95 percent confidence interval:
##  -0.14924665  0.04633251
## sample estimates:
##         cor 
## -0.05195524
```
두 변수의 상관계수는 -0.051로 두 변수간의 상관관계는 존재하지 않는다고 볼 수 있으며 p-value가 0.05보다 높아 두 변수간의 상관관계는 통계적으로 유의하지 않다고 볼 수 있다.

#### 상관계수 행렬

```r
cor(car[,-c(7,10,11)])
```

```
##                   Sales   CompPrice       Income  Advertising   Population       Price          Age    Education
## Sales        1.00000000  0.06407873  0.151950979  0.269506781  0.050470984 -0.44495073 -0.231815440 -0.051955242
## CompPrice    0.06407873  1.00000000 -0.080653423 -0.024198788 -0.094706516  0.58484777 -0.100238817  0.025197050
## Income       0.15195098 -0.08065342  1.000000000  0.058994706 -0.007876994 -0.05669820 -0.004670094 -0.056855422
## Advertising  0.26950678 -0.02419879  0.058994706  1.000000000  0.265652145  0.04453687 -0.004557497 -0.033594307
## Population   0.05047098 -0.09470652 -0.007876994  0.265652145  1.000000000 -0.01214362 -0.042663355 -0.106378231
## Price       -0.44495073  0.58484777 -0.056698202  0.044536874 -0.012143620  1.00000000 -0.102176839  0.011746599
## Age         -0.23181544 -0.10023882 -0.004670094 -0.004557497 -0.042663355 -0.10217684  1.000000000  0.006488032
## Education   -0.05195524  0.02519705 -0.056855422 -0.033594307 -0.106378231  0.01174660  0.006488032  1.000000000
```

```r
plot(car[,-c(7,10,11)])
```

![plot of chunk unnamed-chunk-13](figure/unnamed-chunk-13-1.png)

### 종속변수를 Sales, 독립변수를 CompPrice, Income, Age, Advertising, Population, Price, Education으로 설정하고 후진제거법 활용하여 추정된 회귀식 자것ㅇ


```r
step(lm(Sales ~ Price + Income + Age + Education + CompPrice + Advertising + Population, data = car), direction = 'backward')
```

```
## Start:  AIC=533.5
## Sales ~ Price + Income + Age + Education + CompPrice + Advertising + 
##     Population
## 
##               Df Sum of Sq    RSS    AIC
## - Population   1      0.12 1458.7 531.53
## - Education    1      4.32 1462.9 532.68
## <none>                     1458.6 533.50
## - Income       1     51.03 1509.6 545.25
## - Age          1    208.48 1667.0 584.94
## - Advertising  1    278.65 1737.2 601.43
## - CompPrice    1    533.98 1992.5 656.28
## - Price        1   1247.94 2706.5 778.78
## 
## Step:  AIC=531.53
## Sales ~ Price + Income + Age + Education + CompPrice + Advertising
## 
##               Df Sum of Sq    RSS    AIC
## - Education    1      4.21 1462.9 530.68
## <none>                     1458.7 531.53
## - Income       1     51.29 1510.0 543.35
## - Age          1    208.51 1667.2 582.97
## - Advertising  1    295.91 1754.6 603.41
## - CompPrice    1    540.75 1999.4 655.66
## - Price        1   1250.06 2708.7 777.11
## 
## Step:  AIC=530.68
## Sales ~ Price + Income + Age + CompPrice + Advertising
## 
##               Df Sum of Sq    RSS    AIC
## <none>                     1462.9 530.68
## - Income       1     53.02 1515.9 542.92
## - Age          1    209.00 1671.9 582.10
## - Advertising  1    298.27 1761.2 602.91
## - CompPrice    1    539.21 2002.1 654.20
## - Price        1   1249.81 2712.7 775.70
```

```
## 
## Call:
## lm(formula = Sales ~ Price + Income + Age + CompPrice + Advertising, 
##     data = car)
## 
## Coefficients:
## (Intercept)        Price       Income          Age    CompPrice  Advertising  
##     7.10919     -0.09254      0.01309     -0.04497      0.09390      0.13061
```

```r
car_lm = lm(Sales ~ CompPrice + Income + Advertising + Price + Age, data = car)
summary(car_lm)
```

```
## 
## Call:
## lm(formula = Sales ~ CompPrice + Income + Advertising + Price + 
##     Age, data = car)
## 
## Residuals:
##     Min      1Q  Median      3Q     Max 
## -4.9071 -1.3081 -0.1892  1.1495  4.6980 
## 
## Coefficients:
##              Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  7.109190   0.943940   7.531 3.46e-13 ***
## CompPrice    0.093904   0.007792  12.051  < 2e-16 ***
## Income       0.013092   0.003465   3.779 0.000182 ***
## Advertising  0.130611   0.014572   8.963  < 2e-16 ***
## Price       -0.092543   0.005044 -18.347  < 2e-16 ***
## Age         -0.044971   0.005994  -7.503 4.20e-13 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 1.927 on 394 degrees of freedom
## Multiple R-squared:  0.5403,	Adjusted R-squared:  0.5345 
## F-statistic: 92.62 on 5 and 394 DF,  p-value: < 2.2e-16
```

후진제거법을 이용한 결과 변수들의 유의확률이 모두 작아 통계적으로 유의함을 알 수 잇다. 하지만 모형의 결정계수는 0.5403이며 수정된 결정계수는 0.5345로 전체 데이터의 약 53%를 설명하고 있어 다소 낮은 설명력을 가진다고 할 수 있다.

또한 모형의 F-통계량의 p-value는 0.05 보다 작으므로 유의수준 0.05하에서 모형이 통계적으로 유의한 것을 알 수 있다.

회귀분석 결과 추정된 회귀식은 y = 7.109 + 0.0939 * CompPrice + 0.01309 * Income + 0.13061 * Advertising - 0.09254* Price - 0.04997 * Age 이다.
