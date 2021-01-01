---
title: "DAY_06"
author: "kisehyun"
date: '2020 11 30 '
output: html_document
---



#### **lapply** = 결과를 **리스트**로 반환 **열방향**으로 함수를 처리


```r
a = c(1,2,3)
lapply(a, FUN = function(x){x ^ 3}) # 열 방향으로 함수 적용
```

```
## [[1]]
## [1] 1
## 
## [[2]]
## [1] 8
## 
## [[3]]
## [1] 27
```

```r
class(lapply(a, FUN = function(x){x ^ 3})) # 자료 구조 확인
```

```
## [1] "list"
```

```r
unlist(lapply(a, FUN = function(x){x ^ 3})) # unlist하면 벡터형으로 반환
```

```
## [1]  1  8 27
```


#### **sapply** = 결과를 **벡터 혹은 행렬**로 반환 **열방향**으로 함수 적용

```r
data(iris)
sapply(iris, class)
```

```
## Sepal.Length  Sepal.Width Petal.Length  Petal.Width      Species 
##    "numeric"    "numeric"    "numeric"    "numeric"     "factor"
```


```r
sapply(iris, summary)
```

```
## $Sepal.Length
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##   4.300   5.100   5.800   5.843   6.400   7.900 
## 
## $Sepal.Width
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##   2.000   2.800   3.000   3.057   3.300   4.400 
## 
## $Petal.Length
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##   1.000   1.600   4.350   3.758   5.100   6.900 
## 
## $Petal.Width
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##   0.100   0.300   1.300   1.199   1.800   2.500 
## 
## $Species
##     setosa versicolor  virginica 
##         50         50         50
```

#### **vapply** = **sapply**와 유사하지만 출력결과 형태 사용자 **직접 지정** 가능


```r
t = c(1:100)
fivenum(t)
```

```
## [1]   1.0  25.5  50.5  75.5 100.0
```

```r
t2 = list(t)
vapply(t2, fivenum, c('Min' = 0, 'Q1' = 0, 'Median' = 0, 'Q3' = 0, 'Max' = 0))
```

```
##         [,1]
## Min      1.0
## Q1      25.5
## Median  50.5
## Q3      75.5
## Max    100.0
```

#### **mapply** = **sapply**의 확장 버전으로 **다수 요소** 한번에 적용


```r
rep(1,4)
```

```
## [1] 1 1 1 1
```

```r
mapply(rep, c(1:4), c(4:1))
```

```
## [[1]]
## [1] 1 1 1 1
## 
## [[2]]
## [1] 2 2 2
## 
## [[3]]
## [1] 3 3
## 
## [[4]]
## [1] 4
```

#### **tapply** = 각**그룹별**로 함수 적용**tapply(data, index, function)**에서 **index**는 데이터 **그룹핑** 변수


```r
library(googleVis)
library(plyr)
```


```r
data(Fruits)
head(Fruits)
```

```
##     Fruit Year Location Sales Expenses Profit       Date
## 1  Apples 2008     West    98       78     20 2008-12-31
## 2  Apples 2009     West   111       79     32 2009-12-31
## 3  Apples 2010     West    89       76     13 2010-12-31
## 4 Oranges 2008     East    96       81     15 2008-12-31
## 5 Bananas 2008     East    85       76      9 2008-12-31
## 6 Oranges 2009     East    93       80     13 2009-12-31
```


```r
tapply(Fruits$Sales, Fruits$Fruit, mean)
```

```
##   Apples  Bananas  Oranges 
## 99.33333 86.66667 95.66667
```

```r
tapply(Fruits$Sales, Fruits$Location == 'West', mean) # 지역이 West인 지역의 판매량 평균 산출
```

```
##    FALSE     TRUE 
## 91.16667 99.33333
```
### **dplyr**

#### **adply**는 **배열, 행렬, 데이터 프레임**을 입력 받고 함수 적용 후 **데이터프레임**으로 반환
#### **adply(data, margins, function)**

```r
adply(iris, 1, function(row){ifelse(row$Petal.Length < 1.5 & row$Species == 'setosa', '1', '0')}) # 변수명 지정 x
```

```
##     Sepal.Length Sepal.Width Petal.Length Petal.Width    Species V1
## 1            5.1         3.5          1.4         0.2     setosa  1
## 2            4.9         3.0          1.4         0.2     setosa  1
## 3            4.7         3.2          1.3         0.2     setosa  1
## 4            4.6         3.1          1.5         0.2     setosa  0
## 5            5.0         3.6          1.4         0.2     setosa  1
## 6            5.4         3.9          1.7         0.4     setosa  0
## 7            4.6         3.4          1.4         0.3     setosa  1
## 8            5.0         3.4          1.5         0.2     setosa  0
## 9            4.4         2.9          1.4         0.2     setosa  1
## 10           4.9         3.1          1.5         0.1     setosa  0
## 11           5.4         3.7          1.5         0.2     setosa  0
## 12           4.8         3.4          1.6         0.2     setosa  0
## 13           4.8         3.0          1.4         0.1     setosa  1
## 14           4.3         3.0          1.1         0.1     setosa  1
## 15           5.8         4.0          1.2         0.2     setosa  1
## 16           5.7         4.4          1.5         0.4     setosa  0
## 17           5.4         3.9          1.3         0.4     setosa  1
## 18           5.1         3.5          1.4         0.3     setosa  1
## 19           5.7         3.8          1.7         0.3     setosa  0
## 20           5.1         3.8          1.5         0.3     setosa  0
## 21           5.4         3.4          1.7         0.2     setosa  0
## 22           5.1         3.7          1.5         0.4     setosa  0
## 23           4.6         3.6          1.0         0.2     setosa  1
## 24           5.1         3.3          1.7         0.5     setosa  0
## 25           4.8         3.4          1.9         0.2     setosa  0
## 26           5.0         3.0          1.6         0.2     setosa  0
## 27           5.0         3.4          1.6         0.4     setosa  0
## 28           5.2         3.5          1.5         0.2     setosa  0
## 29           5.2         3.4          1.4         0.2     setosa  1
## 30           4.7         3.2          1.6         0.2     setosa  0
## 31           4.8         3.1          1.6         0.2     setosa  0
## 32           5.4         3.4          1.5         0.4     setosa  0
## 33           5.2         4.1          1.5         0.1     setosa  0
## 34           5.5         4.2          1.4         0.2     setosa  1
## 35           4.9         3.1          1.5         0.2     setosa  0
## 36           5.0         3.2          1.2         0.2     setosa  1
## 37           5.5         3.5          1.3         0.2     setosa  1
## 38           4.9         3.6          1.4         0.1     setosa  1
## 39           4.4         3.0          1.3         0.2     setosa  1
## 40           5.1         3.4          1.5         0.2     setosa  0
## 41           5.0         3.5          1.3         0.3     setosa  1
## 42           4.5         2.3          1.3         0.3     setosa  1
## 43           4.4         3.2          1.3         0.2     setosa  1
## 44           5.0         3.5          1.6         0.6     setosa  0
## 45           5.1         3.8          1.9         0.4     setosa  0
## 46           4.8         3.0          1.4         0.3     setosa  1
## 47           5.1         3.8          1.6         0.2     setosa  0
## 48           4.6         3.2          1.4         0.2     setosa  1
## 49           5.3         3.7          1.5         0.2     setosa  0
## 50           5.0         3.3          1.4         0.2     setosa  1
## 51           7.0         3.2          4.7         1.4 versicolor  0
## 52           6.4         3.2          4.5         1.5 versicolor  0
## 53           6.9         3.1          4.9         1.5 versicolor  0
## 54           5.5         2.3          4.0         1.3 versicolor  0
## 55           6.5         2.8          4.6         1.5 versicolor  0
## 56           5.7         2.8          4.5         1.3 versicolor  0
## 57           6.3         3.3          4.7         1.6 versicolor  0
## 58           4.9         2.4          3.3         1.0 versicolor  0
## 59           6.6         2.9          4.6         1.3 versicolor  0
## 60           5.2         2.7          3.9         1.4 versicolor  0
## 61           5.0         2.0          3.5         1.0 versicolor  0
## 62           5.9         3.0          4.2         1.5 versicolor  0
## 63           6.0         2.2          4.0         1.0 versicolor  0
## 64           6.1         2.9          4.7         1.4 versicolor  0
## 65           5.6         2.9          3.6         1.3 versicolor  0
## 66           6.7         3.1          4.4         1.4 versicolor  0
## 67           5.6         3.0          4.5         1.5 versicolor  0
## 68           5.8         2.7          4.1         1.0 versicolor  0
## 69           6.2         2.2          4.5         1.5 versicolor  0
## 70           5.6         2.5          3.9         1.1 versicolor  0
## 71           5.9         3.2          4.8         1.8 versicolor  0
## 72           6.1         2.8          4.0         1.3 versicolor  0
## 73           6.3         2.5          4.9         1.5 versicolor  0
## 74           6.1         2.8          4.7         1.2 versicolor  0
## 75           6.4         2.9          4.3         1.3 versicolor  0
## 76           6.6         3.0          4.4         1.4 versicolor  0
## 77           6.8         2.8          4.8         1.4 versicolor  0
## 78           6.7         3.0          5.0         1.7 versicolor  0
## 79           6.0         2.9          4.5         1.5 versicolor  0
## 80           5.7         2.6          3.5         1.0 versicolor  0
## 81           5.5         2.4          3.8         1.1 versicolor  0
## 82           5.5         2.4          3.7         1.0 versicolor  0
## 83           5.8         2.7          3.9         1.2 versicolor  0
## 84           6.0         2.7          5.1         1.6 versicolor  0
## 85           5.4         3.0          4.5         1.5 versicolor  0
## 86           6.0         3.4          4.5         1.6 versicolor  0
## 87           6.7         3.1          4.7         1.5 versicolor  0
## 88           6.3         2.3          4.4         1.3 versicolor  0
## 89           5.6         3.0          4.1         1.3 versicolor  0
## 90           5.5         2.5          4.0         1.3 versicolor  0
## 91           5.5         2.6          4.4         1.2 versicolor  0
## 92           6.1         3.0          4.6         1.4 versicolor  0
## 93           5.8         2.6          4.0         1.2 versicolor  0
## 94           5.0         2.3          3.3         1.0 versicolor  0
## 95           5.6         2.7          4.2         1.3 versicolor  0
## 96           5.7         3.0          4.2         1.2 versicolor  0
## 97           5.7         2.9          4.2         1.3 versicolor  0
## 98           6.2         2.9          4.3         1.3 versicolor  0
## 99           5.1         2.5          3.0         1.1 versicolor  0
## 100          5.7         2.8          4.1         1.3 versicolor  0
## 101          6.3         3.3          6.0         2.5  virginica  0
## 102          5.8         2.7          5.1         1.9  virginica  0
## 103          7.1         3.0          5.9         2.1  virginica  0
## 104          6.3         2.9          5.6         1.8  virginica  0
## 105          6.5         3.0          5.8         2.2  virginica  0
## 106          7.6         3.0          6.6         2.1  virginica  0
## 107          4.9         2.5          4.5         1.7  virginica  0
## 108          7.3         2.9          6.3         1.8  virginica  0
## 109          6.7         2.5          5.8         1.8  virginica  0
## 110          7.2         3.6          6.1         2.5  virginica  0
## 111          6.5         3.2          5.1         2.0  virginica  0
## 112          6.4         2.7          5.3         1.9  virginica  0
## 113          6.8         3.0          5.5         2.1  virginica  0
## 114          5.7         2.5          5.0         2.0  virginica  0
## 115          5.8         2.8          5.1         2.4  virginica  0
## 116          6.4         3.2          5.3         2.3  virginica  0
## 117          6.5         3.0          5.5         1.8  virginica  0
## 118          7.7         3.8          6.7         2.2  virginica  0
## 119          7.7         2.6          6.9         2.3  virginica  0
## 120          6.0         2.2          5.0         1.5  virginica  0
## 121          6.9         3.2          5.7         2.3  virginica  0
## 122          5.6         2.8          4.9         2.0  virginica  0
## 123          7.7         2.8          6.7         2.0  virginica  0
## 124          6.3         2.7          4.9         1.8  virginica  0
## 125          6.7         3.3          5.7         2.1  virginica  0
## 126          7.2         3.2          6.0         1.8  virginica  0
## 127          6.2         2.8          4.8         1.8  virginica  0
## 128          6.1         3.0          4.9         1.8  virginica  0
## 129          6.4         2.8          5.6         2.1  virginica  0
## 130          7.2         3.0          5.8         1.6  virginica  0
## 131          7.4         2.8          6.1         1.9  virginica  0
## 132          7.9         3.8          6.4         2.0  virginica  0
## 133          6.4         2.8          5.6         2.2  virginica  0
## 134          6.3         2.8          5.1         1.5  virginica  0
## 135          6.1         2.6          5.6         1.4  virginica  0
## 136          7.7         3.0          6.1         2.3  virginica  0
## 137          6.3         3.4          5.6         2.4  virginica  0
## 138          6.4         3.1          5.5         1.8  virginica  0
## 139          6.0         3.0          4.8         1.8  virginica  0
## 140          6.9         3.1          5.4         2.1  virginica  0
## 141          6.7         3.1          5.6         2.4  virginica  0
## 142          6.9         3.1          5.1         2.3  virginica  0
## 143          5.8         2.7          5.1         1.9  virginica  0
## 144          6.8         3.2          5.9         2.3  virginica  0
## 145          6.7         3.3          5.7         2.5  virginica  0
## 146          6.7         3.0          5.2         2.3  virginica  0
## 147          6.3         2.5          5.0         1.9  virginica  0
## 148          6.5         3.0          5.2         2.0  virginica  0
## 149          6.2         3.4          5.4         2.3  virginica  0
## 150          5.9         3.0          5.1         1.8  virginica  0
```


```r
adply(iris, 1, function(row){data.frame(setosa_PL1.5 = c(ifelse(row$Petal.Length < 1.5 & row$Species == 'setosa', '1', '0')))})
```

```
##     Sepal.Length Sepal.Width Petal.Length Petal.Width    Species setosa_PL1.5
## 1            5.1         3.5          1.4         0.2     setosa            1
## 2            4.9         3.0          1.4         0.2     setosa            1
## 3            4.7         3.2          1.3         0.2     setosa            1
## 4            4.6         3.1          1.5         0.2     setosa            0
## 5            5.0         3.6          1.4         0.2     setosa            1
## 6            5.4         3.9          1.7         0.4     setosa            0
## 7            4.6         3.4          1.4         0.3     setosa            1
## 8            5.0         3.4          1.5         0.2     setosa            0
## 9            4.4         2.9          1.4         0.2     setosa            1
## 10           4.9         3.1          1.5         0.1     setosa            0
## 11           5.4         3.7          1.5         0.2     setosa            0
## 12           4.8         3.4          1.6         0.2     setosa            0
## 13           4.8         3.0          1.4         0.1     setosa            1
## 14           4.3         3.0          1.1         0.1     setosa            1
## 15           5.8         4.0          1.2         0.2     setosa            1
## 16           5.7         4.4          1.5         0.4     setosa            0
## 17           5.4         3.9          1.3         0.4     setosa            1
## 18           5.1         3.5          1.4         0.3     setosa            1
## 19           5.7         3.8          1.7         0.3     setosa            0
## 20           5.1         3.8          1.5         0.3     setosa            0
## 21           5.4         3.4          1.7         0.2     setosa            0
## 22           5.1         3.7          1.5         0.4     setosa            0
## 23           4.6         3.6          1.0         0.2     setosa            1
## 24           5.1         3.3          1.7         0.5     setosa            0
## 25           4.8         3.4          1.9         0.2     setosa            0
## 26           5.0         3.0          1.6         0.2     setosa            0
## 27           5.0         3.4          1.6         0.4     setosa            0
## 28           5.2         3.5          1.5         0.2     setosa            0
## 29           5.2         3.4          1.4         0.2     setosa            1
## 30           4.7         3.2          1.6         0.2     setosa            0
## 31           4.8         3.1          1.6         0.2     setosa            0
## 32           5.4         3.4          1.5         0.4     setosa            0
## 33           5.2         4.1          1.5         0.1     setosa            0
## 34           5.5         4.2          1.4         0.2     setosa            1
## 35           4.9         3.1          1.5         0.2     setosa            0
## 36           5.0         3.2          1.2         0.2     setosa            1
## 37           5.5         3.5          1.3         0.2     setosa            1
## 38           4.9         3.6          1.4         0.1     setosa            1
## 39           4.4         3.0          1.3         0.2     setosa            1
## 40           5.1         3.4          1.5         0.2     setosa            0
## 41           5.0         3.5          1.3         0.3     setosa            1
## 42           4.5         2.3          1.3         0.3     setosa            1
## 43           4.4         3.2          1.3         0.2     setosa            1
## 44           5.0         3.5          1.6         0.6     setosa            0
## 45           5.1         3.8          1.9         0.4     setosa            0
## 46           4.8         3.0          1.4         0.3     setosa            1
## 47           5.1         3.8          1.6         0.2     setosa            0
## 48           4.6         3.2          1.4         0.2     setosa            1
## 49           5.3         3.7          1.5         0.2     setosa            0
## 50           5.0         3.3          1.4         0.2     setosa            1
## 51           7.0         3.2          4.7         1.4 versicolor            0
## 52           6.4         3.2          4.5         1.5 versicolor            0
## 53           6.9         3.1          4.9         1.5 versicolor            0
## 54           5.5         2.3          4.0         1.3 versicolor            0
## 55           6.5         2.8          4.6         1.5 versicolor            0
## 56           5.7         2.8          4.5         1.3 versicolor            0
## 57           6.3         3.3          4.7         1.6 versicolor            0
## 58           4.9         2.4          3.3         1.0 versicolor            0
## 59           6.6         2.9          4.6         1.3 versicolor            0
## 60           5.2         2.7          3.9         1.4 versicolor            0
## 61           5.0         2.0          3.5         1.0 versicolor            0
## 62           5.9         3.0          4.2         1.5 versicolor            0
## 63           6.0         2.2          4.0         1.0 versicolor            0
## 64           6.1         2.9          4.7         1.4 versicolor            0
## 65           5.6         2.9          3.6         1.3 versicolor            0
## 66           6.7         3.1          4.4         1.4 versicolor            0
## 67           5.6         3.0          4.5         1.5 versicolor            0
## 68           5.8         2.7          4.1         1.0 versicolor            0
## 69           6.2         2.2          4.5         1.5 versicolor            0
## 70           5.6         2.5          3.9         1.1 versicolor            0
## 71           5.9         3.2          4.8         1.8 versicolor            0
## 72           6.1         2.8          4.0         1.3 versicolor            0
## 73           6.3         2.5          4.9         1.5 versicolor            0
## 74           6.1         2.8          4.7         1.2 versicolor            0
## 75           6.4         2.9          4.3         1.3 versicolor            0
## 76           6.6         3.0          4.4         1.4 versicolor            0
## 77           6.8         2.8          4.8         1.4 versicolor            0
## 78           6.7         3.0          5.0         1.7 versicolor            0
## 79           6.0         2.9          4.5         1.5 versicolor            0
## 80           5.7         2.6          3.5         1.0 versicolor            0
## 81           5.5         2.4          3.8         1.1 versicolor            0
## 82           5.5         2.4          3.7         1.0 versicolor            0
## 83           5.8         2.7          3.9         1.2 versicolor            0
## 84           6.0         2.7          5.1         1.6 versicolor            0
## 85           5.4         3.0          4.5         1.5 versicolor            0
## 86           6.0         3.4          4.5         1.6 versicolor            0
## 87           6.7         3.1          4.7         1.5 versicolor            0
## 88           6.3         2.3          4.4         1.3 versicolor            0
## 89           5.6         3.0          4.1         1.3 versicolor            0
## 90           5.5         2.5          4.0         1.3 versicolor            0
## 91           5.5         2.6          4.4         1.2 versicolor            0
## 92           6.1         3.0          4.6         1.4 versicolor            0
## 93           5.8         2.6          4.0         1.2 versicolor            0
## 94           5.0         2.3          3.3         1.0 versicolor            0
## 95           5.6         2.7          4.2         1.3 versicolor            0
## 96           5.7         3.0          4.2         1.2 versicolor            0
## 97           5.7         2.9          4.2         1.3 versicolor            0
## 98           6.2         2.9          4.3         1.3 versicolor            0
## 99           5.1         2.5          3.0         1.1 versicolor            0
## 100          5.7         2.8          4.1         1.3 versicolor            0
## 101          6.3         3.3          6.0         2.5  virginica            0
## 102          5.8         2.7          5.1         1.9  virginica            0
## 103          7.1         3.0          5.9         2.1  virginica            0
## 104          6.3         2.9          5.6         1.8  virginica            0
## 105          6.5         3.0          5.8         2.2  virginica            0
## 106          7.6         3.0          6.6         2.1  virginica            0
## 107          4.9         2.5          4.5         1.7  virginica            0
## 108          7.3         2.9          6.3         1.8  virginica            0
## 109          6.7         2.5          5.8         1.8  virginica            0
## 110          7.2         3.6          6.1         2.5  virginica            0
## 111          6.5         3.2          5.1         2.0  virginica            0
## 112          6.4         2.7          5.3         1.9  virginica            0
## 113          6.8         3.0          5.5         2.1  virginica            0
## 114          5.7         2.5          5.0         2.0  virginica            0
## 115          5.8         2.8          5.1         2.4  virginica            0
## 116          6.4         3.2          5.3         2.3  virginica            0
## 117          6.5         3.0          5.5         1.8  virginica            0
## 118          7.7         3.8          6.7         2.2  virginica            0
## 119          7.7         2.6          6.9         2.3  virginica            0
## 120          6.0         2.2          5.0         1.5  virginica            0
## 121          6.9         3.2          5.7         2.3  virginica            0
## 122          5.6         2.8          4.9         2.0  virginica            0
## 123          7.7         2.8          6.7         2.0  virginica            0
## 124          6.3         2.7          4.9         1.8  virginica            0
## 125          6.7         3.3          5.7         2.1  virginica            0
## 126          7.2         3.2          6.0         1.8  virginica            0
## 127          6.2         2.8          4.8         1.8  virginica            0
## 128          6.1         3.0          4.9         1.8  virginica            0
## 129          6.4         2.8          5.6         2.1  virginica            0
## 130          7.2         3.0          5.8         1.6  virginica            0
## 131          7.4         2.8          6.1         1.9  virginica            0
## 132          7.9         3.8          6.4         2.0  virginica            0
## 133          6.4         2.8          5.6         2.2  virginica            0
## 134          6.3         2.8          5.1         1.5  virginica            0
## 135          6.1         2.6          5.6         1.4  virginica            0
## 136          7.7         3.0          6.1         2.3  virginica            0
## 137          6.3         3.4          5.6         2.4  virginica            0
## 138          6.4         3.1          5.5         1.8  virginica            0
## 139          6.0         3.0          4.8         1.8  virginica            0
## 140          6.9         3.1          5.4         2.1  virginica            0
## 141          6.7         3.1          5.6         2.4  virginica            0
## 142          6.9         3.1          5.1         2.3  virginica            0
## 143          5.8         2.7          5.1         1.9  virginica            0
## 144          6.8         3.2          5.9         2.3  virginica            0
## 145          6.7         3.3          5.7         2.5  virginica            0
## 146          6.7         3.0          5.2         2.3  virginica            0
## 147          6.3         2.5          5.0         1.9  virginica            0
## 148          6.5         3.0          5.2         2.0  virginica            0
## 149          6.2         3.4          5.4         2.3  virginica            0
## 150          5.9         3.0          5.1         1.8  virginica            0
```
