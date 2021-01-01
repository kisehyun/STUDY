---
title: "DAY_03"
author: "kisehyun"
date: '2020 11 26 '
output: html_document
---



# **통계분석**

## 1. 데이터 샘플링
#### **R**을 활용하여 **샘플링**을 진행할 때는 **sample** 함수 사용
**sample(x, size, replace = FALSE, prop = NULL)** replace : 복원 추출 여부, prob : 데이터 뽑을 때 가중치

### Q) iris 데이터 7:3으로 나누기(단순 임의 추출)

```r
idx = sample(1:nrow(iris), nrow(iris) * .7, replace = FALSE) # w
train = iris[idx,]
test = iris[-idx,]
```


```r
dim(iris) # 행의 개수 = 150
```

```
## [1] 150   6
```


```r
nrow(train) # 학습 데이터 150 * 0.7 = 105
```

```
## [1] 105
```

```r
nrow(test) # 테스트 데이터 150 * 0.3 = 45
```

```
## [1] 45
```

#### 층화 임의 추출
**strata(data, stratenames = NULL, size, method, pik, description)**를 활용해 층화 임의 추출 가능.
**getdata(data, m)**를 활용해 표본추출을 통해 얻어진 데이터 출력 가능

### Q) iris에서 setosa 20개, versicolor 15개, versinica 15개 층화 임의 추출

```r
sam = strata(iris, 'Species', size = c(20, 15, 15), method = 'srswor')
head(sam)
```

```
##    Species ID_unit Prob Stratum
## 2   setosa       2  0.4       1
## 3   setosa       3  0.4       1
## 6   setosa       6  0.4       1
## 8   setosa       8  0.4       1
## 9   setosa       9  0.4       1
## 10  setosa      10  0.4       1
```


```r
iris_sam = getdata(iris, sam) # 샘플링된 데이터 확인
head(iris_sam)
```

```
##    Sepal.Length Sepal.Width Petal.Length Petal.Width     SL_new Species ID_unit Prob Stratum
## 2           4.9         3.0          1.4         0.2 0.16666667  setosa       2  0.4       1
## 3           4.7         3.2          1.3         0.2 0.11111111  setosa       3  0.4       1
## 6           5.4         3.9          1.7         0.4 0.30555556  setosa       6  0.4       1
## 8           5.0         3.4          1.5         0.2 0.19444444  setosa       8  0.4       1
## 9           4.4         2.9          1.4         0.2 0.02777778  setosa       9  0.4       1
## 10          4.9         3.1          1.5         0.1 0.16666667  setosa      10  0.4       1
```

```r
table(iris_sam$Species) # Species 변수에 대한 테이블 생성
```

```
## 
##     setosa versicolor  virginica 
##         20         15         15
```

## **2. T-검정(T-test)**

#### **일표본 t검정** : **단일 모집단**에서 **연속형 변수**의 **평균값**을 **특정 기준값**과 비교할 때 사용

#### **정규성 검정**이 전제가 되어야 한다. **Q-Q plot**을 이용하거나 **샤피로-윌크 검정**을 이용한다. 
**샤피로-윌크 검정**은 **shapiro.test(data)**를 이용한다. 만약 **정규성을 만족하지 않는 경우** **wilcox.test 함수**를 이용해 **T-검정**을 수행한다.

**t.test(x, alternative = c('two.sided', 'less', 'greater'), mu = 0)**
**wilcox.test(x, alternative = c('two.sided','less','greater'), mu = 0)**

### Q) MASS패키지의 cats 데이터 활용해 고양이들의 평균 몸무게가 2.6kg인지 아닌지 통계적 검정 수행하고 결과 해석(양측검정, 유의수준 0.05)

```r
shapiro.test(cats$Bwt)
```

```
## 
## 	Shapiro-Wilk normality test
## 
## data:  cats$Bwt
## W = 0.95188, p-value = 6.731e-05
```

p-value가 유의수준보다 작기 때문에 귀무가설(정규성을 만족한다.)을 기각한다. 이후 **wilcox.test**를 수행한다.

```r
wilcox.test(cats$Bwt, mu = 2.6, alternative = 'two.sided')
```

```
## 
## 	Wilcoxon signed rank test with continuity correction
## 
## data:  cats$Bwt
## V = 5607, p-value = 0.02532
## alternative hypothesis: true location is not equal to 2.6
```

**같은가**에 대한 문제이기 때문에 **양측검정(alternative = 'two.sided')**을 수행한다. **p-value**가 유의수준 보다 작기 때문에 고양이들의 평균 몸무게는 2.6kg가 아니라는 결론을 내릴 수 있다.

#### **대응표본 t-검정(paired sample T-test)** : **단일 모집단**에 대해 **두 번**의 처리를 가했을 때 **평균의 차이** 비교

### Q) 10명 환자 대상 수면영양제 복용 전/후 수면시간 차이 측정하여 영양제 효과 있는지 판단(단측검정으로 수면시간이 더 늘어났는지 검정)


```r
data = data.frame(before = c(7,3,4,5,2,1,6,6,5,4),
                  after = c(8,4,5,6,2,3,6,8,6,5))
data
```

```
##    before after
## 1       7     8
## 2       3     4
## 3       4     5
## 4       5     6
## 5       2     2
## 6       1     3
## 7       6     6
## 8       6     8
## 9       5     6
## 10      4     5
```


```r
t.test(data$before, data$after, alternative = 'less', paired = TRUE)
```

```
## 
## 	Paired t-test
## 
## data:  data$before and data$after
## t = -4.7434, df = 9, p-value = 0.0005269
## alternative hypothesis: true difference in means is less than 0
## 95 percent confidence interval:
##        -Inf -0.6135459
## sample estimates:
## mean of the differences 
##                      -1
```

차이가 있는지 비교하기 때문에 **단측검정**
t통계량은 -4.7434, 자유도는 10-1= 9, p-value는 유의수준 보다 작게 나타나 복용 전/후의 수면 시간 차이는 통계적으로 유의하며 영양제를 복용한 후 수면시간이 늘었다고 할 수 있다.

#### **독립표본 t-검정(independent sample T-test)** : **두개의 독립된 모집단의 평균 비교**

t-검정 수행하기 전 **등분산 검정**필요. **var.test(x, y, alternative)**

### Q) cats 데이터 활용해 성별에 따른 몸무게의 평균이 다른지 검정 수행하고 해석

```r
var.test(Bwt ~ Sex, cats)
```

```
## 
## 	F test to compare two variances
## 
## data:  Bwt by Sex
## F = 0.3435, num df = 46, denom df = 96, p-value = 0.0001157
## alternative hypothesis: true ratio of variances is not equal to 1
## 95 percent confidence interval:
##  0.2126277 0.5803475
## sample estimates:
## ratio of variances 
##          0.3435015
```

**p-value**가 유의수준(0.05) 보다 작기 떄문에 귀무가설을 기각한다. 즉 등분산 가정을 만족한다고 할 수 없다.
이후 **var.equal = FALSE**로 지정하고 독립t-검정 수행

```r
t.test(Bwt ~ Sex, data = cats, alternative = 'two.sided', var.equal = FALSE)
```

```
## 
## 	Welch Two Sample t-test
## 
## data:  Bwt by Sex
## t = -8.7095, df = 136.84, p-value = 8.831e-15
## alternative hypothesis: true difference in means is not equal to 0
## 95 percent confidence interval:
##  -0.6631268 -0.4177242
## sample estimates:
## mean in group F mean in group M 
##        2.359574        2.900000
```

**p-value**가 유의수준 보다 매우 작고 **t-통계량**은 -8.7095, **자유도**는는 136.84로 귀무가설을 기각한다.

## **3. 교차분석**

### **명목척도** 혹은 **순서척도**와 같은 **범주형 자료**들 간의 **상호 연관성** 파악
### **카이제곱 통계량**을 이용해서 **적합성 검정, 독립성 검정, 동질성 검정**에 사용된다.
### **교차분석**은 각 셀의 **관찰빈도**와 **기대빈도**간의 차이를 검정

#### **적합성 검정**은 **chisq.teset(x, y, p)**를 활용한다.

### Q) survey 데이터를 활용해 W.Hnd 변수에 대한 분할표 생성하고 아래의 가설에 대한 적합도 검정 수행하라.
### H0 : 왼손잡이 20%, 오른손잡이 80%이다.


```r
data(survey, package = 'MASS')
str(survey)
```

```
## 'data.frame':	237 obs. of  12 variables:
##  $ Sex   : Factor w/ 2 levels "Female","Male": 1 2 2 2 2 1 2 1 2 2 ...
##  $ Wr.Hnd: num  18.5 19.5 18 18.8 20 18 17.7 17 20 18.5 ...
##  $ NW.Hnd: num  18 20.5 13.3 18.9 20 17.7 17.7 17.3 19.5 18.5 ...
##  $ W.Hnd : Factor w/ 2 levels "Left","Right": 2 1 2 2 2 2 2 2 2 2 ...
##  $ Fold  : Factor w/ 3 levels "L on R","Neither",..: 3 3 1 3 2 1 1 3 3 3 ...
##  $ Pulse : int  92 104 87 NA 35 64 83 74 72 90 ...
##  $ Clap  : Factor w/ 3 levels "Left","Neither",..: 1 1 2 2 3 3 3 3 3 3 ...
##  $ Exer  : Factor w/ 3 levels "Freq","None",..: 3 2 2 2 3 3 1 1 3 3 ...
##  $ Smoke : Factor w/ 4 levels "Heavy","Never",..: 2 4 3 2 2 2 2 2 2 2 ...
##  $ Height: num  173 178 NA 160 165 ...
##  $ M.I   : Factor w/ 2 levels "Imperial","Metric": 2 1 NA 2 2 1 1 2 2 2 ...
##  $ Age   : num  18.2 17.6 16.9 20.3 23.7 ...
```

```r
table(survey$W.Hnd) # 분할표 출력
```

```
## 
##  Left Right 
##    18   218
```


```r
df = table(survey$W.Hnd) # 분할표 별도로 저장
chisq.test(df, p = c(.2, .8))
```

```
## 
## 	Chi-squared test for given probabilities
## 
## data:  df
## X-squared = 22.581, df = 1, p-value = 2.015e-06
```

카이제곱 수행 결과 **p-value**가 유의수준 보다 작으므로 **귀무가설**을 기각한다.

#### **독립성 검정**은 **두 범주형 변수** 사이의 관계가 독립인지 아닌지 검정
#### **독립성 검정**은 **chisq.test**에 **xtabs(formula, data)**을 활용해 검정한다.

### Q) survey 데이터로 사용하는 손과 운동의 빈도가 서로 독립인지 검정
### H0 : W.Hnd와 Exer은 독립이다.


```r
table(survey$W.Hnd, survey$Exer)
```

```
##        
##         Freq None Some
##   Left     7    3    8
##   Right  107   21   90
```


```r
chisq.test(xtabs(~ W.Hnd + Exer, data = survey)) # chisq.test(table(survey$W.Hnd, survey$Exer))와 동일
```

```
## Warning in chisq.test(xtabs(~W.Hnd + Exer, data = survey)): Chi-squared approximation may be incorrect
```

```
## 
## 	Pearson's Chi-squared test
## 
## data:  xtabs(~W.Hnd + Exer, data = survey)
## X-squared = 1.2065, df = 2, p-value = 0.547
```

**p-values**가 유의수준 보다 크기 때문에 귀무가설을 기각하지 않는다. 따라서 두 변수간의 빈도는 서로 독립이다.

#### **동질성 검정**은 **모집단**에서 추출한 임의 개수의 범주화된 집단의 **분포**가 서로 동일한지 검정

## **4. 분산분석(ANOVA)**

### **분산분석**은 두 개 이상의 집단 간 평균 비교

#### **일원배치 분산분석**은 **하나**의 범주형 변수의 영향을 알아보는 방법
#### **F-검정 통계량**을 이용한다.

#### **aov(formula, data)**을 활용한다.
#### **TukeyHSD(x, conf.level = .95)** 를 활용해 사후 분석 시행(어떤 집단들끼리 차이가 있는지)

### Q) iris로 Species별로 Sepal.Width 평균이 같은지 or 차이가 있는지 확인


```r
result = aov(Sepal.Width ~ Species, data = iris)
summary(result)
```

```
##              Df Sum Sq Mean Sq F value Pr(>F)    
## Species       2  11.35   5.672   49.16 <2e-16 ***
## Residuals   147  16.96   0.115                   
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```
**p-value**가 매우 작으므로 귀무가설을 기각한다.

```r
TukeyHSD(result)
```

```
##   Tukey multiple comparisons of means
##     95% family-wise confidence level
## 
## Fit: aov(formula = Sepal.Width ~ Species, data = iris)
## 
## $Species
##                        diff         lwr        upr     p adj
## versicolor-setosa    -0.658 -0.81885528 -0.4971447 0.0000000
## virginica-setosa     -0.454 -0.61485528 -0.2931447 0.0000000
## virginica-versicolor  0.204  0.04314472  0.3648553 0.0087802
```

세 집단간 비교에 대해서 모두 p-value가 유의수준 보다 작으므로 귀무가설을 모두 기각한다.
즉 모든 종들에 대해 꽃받침 포 평균은 유의한 차이가 있다.

#### **이원배치 분산분석**은 **반응값**에 대해 두 개의 **범주형 변수**의 영향을 알아보는 분석
#### **교호작용**도 반드시 진행 되어야 함.
#### **상호작용효과 시각화**는 **interaction.plot(x.factor, trace.factor, response)**

### Q) mtcars데이터로 am과 cyl에 따라 mpg 평균에 유의미한 차이가 존재하는지 분석


```r
data('mtcars')
str(mtcars)
```

```
## 'data.frame':	32 obs. of  11 variables:
##  $ mpg : num  21 21 22.8 21.4 18.7 18.1 14.3 24.4 22.8 19.2 ...
##  $ cyl : num  6 6 4 6 8 6 8 4 4 6 ...
##  $ disp: num  160 160 108 258 360 ...
##  $ hp  : num  110 110 93 110 175 105 245 62 95 123 ...
##  $ drat: num  3.9 3.9 3.85 3.08 3.15 2.76 3.21 3.69 3.92 3.92 ...
##  $ wt  : num  2.62 2.88 2.32 3.21 3.44 ...
##  $ qsec: num  16.5 17 18.6 19.4 17 ...
##  $ vs  : num  0 0 1 1 0 1 0 1 1 1 ...
##  $ am  : num  1 1 1 0 0 0 0 0 0 0 ...
##  $ gear: num  4 4 4 3 3 3 3 4 4 4 ...
##  $ carb: num  4 4 1 1 2 1 4 2 2 4 ...
```


```r
mtcars$cyl = as.factor(mtcars$cyl)
mtcars$am = as.factor(mtcars$am)
car = mtcars[,c('cyl','am','mpg')]
car_aov = aov(mpg ~ cyl + am + am:cyl,data = car) # aov(mpg ~ am*cyl)과 동일
summary(car_aov)
```

```
##             Df Sum Sq Mean Sq F value   Pr(>F)    
## cyl          2  824.8   412.4  44.852 3.73e-09 ***
## am           1   36.8    36.8   3.999   0.0561 .  
## cyl:am       2   25.4    12.7   1.383   0.2686    
## Residuals   26  239.1     9.2                     
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```

**cyl**의 **p-value**는 유의수준 보다 작아 **실린더 개수에 따른 주행거리 평균간 차이는 존재하지 않는다**는 귀무가설 기각한다.
**am**의 **p-value**는 유의수준 보다 크므로 **am 종류에 따른 주행 거리 평균간 차이는 존재하지 않는다**는 귀무가설 기각하지 않는다.
**cyl과 am**의 상호작용 결과는 p-value가 유의수준보다 크므로 귀무가설을 기각하지 않는다.

```r
interaction.plot(car$cyl, car$am, car$mpg, col = c('red', 'blue'))
```

![plot of chunk unnamed-chunk-60](figure/unnamed-chunk-60-1.png)
두 직선이 교차하지 않기 때문에 상호작용이 존재하지 않는다고 할 수 있다.

## **5. 상관분석**

#### **피어슨** : 두 **연속형 자료**가 모두 **정규성**을 따를 때 사용
#### **스피어만** : **순서 및 순위**형태의 데이터
#### **켄달** : X가 커질 떄 Y도 커지는 비율

### q) airquality 데이터로 4가지 변수 상관계수


```r
str(airquality)
```

```
## 'data.frame':	153 obs. of  6 variables:
##  $ Ozone  : int  41 36 12 18 NA 28 23 19 8 NA ...
##  $ Solar.R: int  190 118 149 313 NA NA 299 99 19 194 ...
##  $ Wind   : num  7.4 8 12.6 11.5 14.3 14.9 8.6 13.8 20.1 8.6 ...
##  $ Temp   : int  67 72 74 62 56 66 65 59 61 69 ...
##  $ Month  : int  5 5 5 5 5 5 5 5 5 5 ...
##  $ Day    : int  1 2 3 4 5 6 7 8 9 10 ...
```


```r
air = airquality[,c(1:4)]
str(air)
```

```
## 'data.frame':	153 obs. of  4 variables:
##  $ Ozone  : int  41 36 12 18 NA 28 23 19 8 NA ...
##  $ Solar.R: int  190 118 149 313 NA NA 299 99 19 194 ...
##  $ Wind   : num  7.4 8 12.6 11.5 14.3 14.9 8.6 13.8 20.1 8.6 ...
##  $ Temp   : int  67 72 74 62 56 66 65 59 61 69 ...
```


```r
cor(air, use = 'pairwise.complete.obs', method = 'pearson')
```

```
##              Ozone     Solar.R        Wind       Temp
## Ozone    1.0000000  0.34834169 -0.60154653  0.6983603
## Solar.R  0.3483417  1.00000000 -0.05679167  0.2758403
## Wind    -0.6015465 -0.05679167  1.00000000 -0.4579879
## Temp     0.6983603  0.27584027 -0.45798788  1.0000000
```


```r
cor(air, use = 'pairwise.complete.obs', method = 'kendall')
```

```
##              Ozone      Solar.R          Wind       Temp
## Ozone    1.0000000 0.2403194214 -0.4283602915  0.5862988
## Solar.R  0.2403194 1.0000000000  0.0006785596  0.1442337
## Wind    -0.4283603 0.0006785596  1.0000000000 -0.3222418
## Temp     0.5862988 0.1442336719 -0.3222417514  1.0000000
```


```r
cor(air, use = 'pairwise.complete.obs', method = 'spearman')
```

```
##              Ozone       Solar.R          Wind       Temp
## Ozone    1.0000000  0.3481864700 -0.5901551241  0.7740430
## Solar.R  0.3481865  1.0000000000 -0.0009773325  0.2074275
## Wind    -0.5901551 -0.0009773325  1.0000000000 -0.4465408
## Temp     0.7740430  0.2074275160 -0.4465407773  1.0000000
```


```r
pairs(cor(air, use = 'pairwise.complete.obs'))
```

![plot of chunk unnamed-chunk-66](figure/unnamed-chunk-66-1.png)


```r
cor.test(air$Ozone, air$Wind, method = 'pearson')
```

```
## 
## 	Pearson's product-moment correlation
## 
## data:  air$Ozone and air$Wind
## t = -8.0401, df = 114, p-value = 9.272e-13
## alternative hypothesis: true correlation is not equal to 0
## 95 percent confidence interval:
##  -0.7063918 -0.4708713
## sample estimates:
##        cor 
## -0.6015465
```

## **6. 회귀분석**

### Q) Cars93데이터 활용하여 enginesize 독립변수, price 종속변수로 단순선형회귀분석


```r
str(Cars93)
```

```
## 'data.frame':	93 obs. of  27 variables:
##  $ Manufacturer      : Factor w/ 32 levels "Acura","Audi",..: 1 1 2 2 3 4 4 4 4 5 ...
##  $ Model             : Factor w/ 93 levels "100","190E","240",..: 49 56 9 1 6 24 54 74 73 35 ...
##  $ Type              : Factor w/ 6 levels "Compact","Large",..: 4 3 1 3 3 3 2 2 3 2 ...
##  $ Min.Price         : num  12.9 29.2 25.9 30.8 23.7 14.2 19.9 22.6 26.3 33 ...
##  $ Price             : num  15.9 33.9 29.1 37.7 30 15.7 20.8 23.7 26.3 34.7 ...
##  $ Max.Price         : num  18.8 38.7 32.3 44.6 36.2 17.3 21.7 24.9 26.3 36.3 ...
##  $ MPG.city          : int  25 18 20 19 22 22 19 16 19 16 ...
##  $ MPG.highway       : int  31 25 26 26 30 31 28 25 27 25 ...
##  $ AirBags           : Factor w/ 3 levels "Driver & Passenger",..: 3 1 2 1 2 2 2 2 2 2 ...
##  $ DriveTrain        : Factor w/ 3 levels "4WD","Front",..: 2 2 2 2 3 2 2 3 2 2 ...
##  $ Cylinders         : Factor w/ 6 levels "3","4","5","6",..: 2 4 4 4 2 2 4 4 4 5 ...
##  $ EngineSize        : num  1.8 3.2 2.8 2.8 3.5 2.2 3.8 5.7 3.8 4.9 ...
##  $ Horsepower        : int  140 200 172 172 208 110 170 180 170 200 ...
##  $ RPM               : int  6300 5500 5500 5500 5700 5200 4800 4000 4800 4100 ...
##  $ Rev.per.mile      : int  2890 2335 2280 2535 2545 2565 1570 1320 1690 1510 ...
##  $ Man.trans.avail   : Factor w/ 2 levels "No","Yes": 2 2 2 2 2 1 1 1 1 1 ...
##  $ Fuel.tank.capacity: num  13.2 18 16.9 21.1 21.1 16.4 18 23 18.8 18 ...
##  $ Passengers        : int  5 5 5 6 4 6 6 6 5 6 ...
##  $ Length            : int  177 195 180 193 186 189 200 216 198 206 ...
##  $ Wheelbase         : int  102 115 102 106 109 105 111 116 108 114 ...
##  $ Width             : int  68 71 67 70 69 69 74 78 73 73 ...
##  $ Turn.circle       : int  37 38 37 37 39 41 42 45 41 43 ...
##  $ Rear.seat.room    : num  26.5 30 28 31 27 28 30.5 30.5 26.5 35 ...
##  $ Luggage.room      : int  11 15 14 17 13 16 17 21 14 18 ...
##  $ Weight            : int  2705 3560 3375 3405 3640 2880 3470 4105 3495 3620 ...
##  $ Origin            : Factor w/ 2 levels "USA","non-USA": 2 2 2 2 2 1 1 1 1 1 ...
##  $ Make              : Factor w/ 93 levels "Acura Integra",..: 1 2 4 3 5 6 7 9 8 10 ...
```


```r
summary(lm(Price ~ EngineSize, data = Cars93))
```

```
## 
## Call:
## lm(formula = Price ~ EngineSize, data = Cars93)
## 
## Residuals:
##     Min      1Q  Median      3Q     Max 
## -13.684  -4.627  -1.795   2.592  39.429 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)    
## (Intercept)   4.6692     2.2390   2.085   0.0398 *  
## EngineSize    5.5629     0.7828   7.107 2.59e-10 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 7.789 on 91 degrees of freedom
## Multiple R-squared:  0.3569,	Adjusted R-squared:  0.3499 
## F-statistic: 50.51 on 1 and 91 DF,  p-value: 2.588e-10
```


```r
par(mfrow = c(2,3))
plot(lm(Price ~ EngineSize, data = Cars93), which = c(1:6))
```

![plot of chunk unnamed-chunk-70](figure/unnamed-chunk-70-1.png)

#### **예측**을 할 때는 **predict.lm(object, newdata, interval = c('none', 'confidence', 'prediction'), level)**을 사용한다.

### Q) Cars93 활용해서 5개 행 랜덤으로 뽑아 Price 예측하고 예측시 interval 인자값 조정하며 결과 비교


```r
car_lm = lm(Price ~ EngineSize, data = Cars93)
set.seed(1126) # 시드 고정
idx = sample(1:nrow(Cars93), 5) # 전체 행에서 랜덤으로 5개 추출
idx
```

```
## [1] 87 13 22 93 16
```


```r
test = Cars93[idx,]
predict.lm(car_lm, test, interval = 'none') # 점추정(none)
```

```
##       87       13       22       93       16 
## 18.02025 16.90766 23.02689 18.02025 25.80836
```


```r
predict.lm(car_lm, test, interval = 'confidence') # 점추정(confidence)
```

```
##         fit      lwr      upr
## 87 18.02025 16.36284 19.67765
## 13 16.90766 15.14623 18.66909
## 22 23.02689 21.14536 24.90842
## 93 18.02025 16.36284 19.67765
## 16 25.80836 23.42653 28.19019
```


```r
predict.lm(car_lm, test, interval = 'prediction') # 점추정(prediction / 회귀계수의 불확실성과 오차항 함께 감안하여 예측)
```

```
##         fit       lwr      upr
## 87 18.02025  2.460666 33.57982
## 13 16.90766  1.336654 32.47866
## 22 23.02689  7.441846 38.61194
## 93 18.02025  2.460666 33.57982
## 16 25.80836 10.155035 41.46169
```


**범주형변수** 처리 - 더미화


```r
iris_lm = lm(Petal.Length ~ Sepal.Length + Sepal.Width + Petal.Width + Species, data = iris)
summary(iris_lm)
```

```
## 
## Call:
## lm(formula = Petal.Length ~ Sepal.Length + Sepal.Width + Petal.Width + 
##     Species, data = iris)
## 
## Residuals:
##      Min       1Q   Median       3Q      Max 
## -0.78396 -0.15708  0.00193  0.14730  0.65418 
## 
## Coefficients:
##                   Estimate Std. Error t value Pr(>|t|)    
## (Intercept)       -1.11099    0.26987  -4.117 6.45e-05 ***
## Sepal.Length       0.60801    0.05024  12.101  < 2e-16 ***
## Sepal.Width       -0.18052    0.08036  -2.246   0.0262 *  
## Petal.Width        0.60222    0.12144   4.959 1.97e-06 ***
## Speciesversicolor  1.46337    0.17345   8.437 3.14e-14 ***
## Speciesvirginica   1.97422    0.24480   8.065 2.60e-13 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.2627 on 144 degrees of freedom
## Multiple R-squared:  0.9786,	Adjusted R-squared:  0.9778 
## F-statistic:  1317 on 5 and 144 DF,  p-value: < 2.2e-16
```

자동으로 **더미화**가 되어 결과가 출력된 것을 알 수 있다.

#### **최적회귀방정식** 선택
#### **step(object, scope, direction, k)**을 이용해 단계선택법 수행

### Q) Cars93 데이터로 후진제거법 활용


```r
lm_result = lm(Price ~ EngineSize + Horsepower + RPM + Width + Length + Weight, data = Cars93)
step(lm_result, direction = 'backward')
```

```
## Start:  AIC=322.11
## Price ~ EngineSize + Horsepower + RPM + Width + Length + Weight
## 
##              Df Sum of Sq    RSS    AIC
## - EngineSize  1      1.69 2556.1 320.17
## - RPM         1     19.71 2574.1 320.82
## <none>                    2554.4 322.11
## - Length      1    119.55 2674.0 324.36
## - Weight      1    209.73 2764.2 327.45
## - Width       1    585.01 3139.4 339.29
## - Horsepower  1    720.84 3275.3 343.22
## 
## Step:  AIC=320.17
## Price ~ Horsepower + RPM + Width + Length + Weight
## 
##              Df Sum of Sq    RSS    AIC
## - RPM         1     49.36 2605.5 319.95
## <none>                    2556.1 320.17
## - Length      1    140.92 2697.0 323.16
## - Weight      1    208.09 2764.2 325.45
## - Width       1    593.56 3149.7 337.59
## - Horsepower  1   1476.65 4032.8 360.57
## 
## Step:  AIC=319.95
## Price ~ Horsepower + Width + Length + Weight
## 
##              Df Sum of Sq    RSS    AIC
## <none>                    2605.5 319.95
## - Length      1    132.02 2737.5 322.54
## - Weight      1    279.31 2884.8 327.42
## - Width       1    562.10 3167.6 336.12
## - Horsepower  1   1898.74 4504.2 368.86
```

```
## 
## Call:
## lm(formula = Price ~ Horsepower + Width + Length + Weight, data = Cars93)
## 
## Coefficients:
## (Intercept)   Horsepower        Width       Length       Weight  
##   53.005861     0.129653    -1.480623     0.152968     0.007339
```
