---
title: "DAY_08"
author: "kisehyun"
date: '2020 12 6 '
output: html_document
---


# **연관분석**


```r
data(Groceries)
Groceries
```

```
## transactions in sparse format with
##  9835 transactions (rows) and
##  169 items (columns)
```

```r
inspect(Groceries[1:3]) # transaction 데이터 변환
```

```
##     items                                                   
## [1] {citrus fruit,semi-finished bread,margarine,ready soups}
## [2] {tropical fruit,yogurt,coffee}                          
## [3] {whole milk}
```


```r
rules = apriori(Groceries, parameter = list(support = .01, confidence = .3))
```

```
## Apriori
## 
## Parameter specification:
##  confidence minval smax arem  aval originalSupport maxtime support minlen maxlen target  ext
##         0.3    0.1    1 none FALSE            TRUE       5    0.01      1     10  rules TRUE
## 
## Algorithmic control:
##  filter tree heap memopt load sort verbose
##     0.1 TRUE TRUE  FALSE TRUE    2    TRUE
## 
## Absolute minimum support count: 98 
## 
## set item appearances ...[0 item(s)] done [0.00s].
## set transactions ...[169 item(s), 9835 transaction(s)] done [0.00s].
## sorting and recoding items ... [88 item(s)] done [0.00s].
## creating transaction tree ... done [0.00s].
## checking subsets of size 1 2 3 4 done [0.00s].
## writing ... [125 rule(s)] done [0.00s].
## creating S4 object  ... done [0.00s].
```

#### **최소 지지도는 0.01, 최소 신뢰도는 0.3**으로 지정, 총 125개의 규칙 생성**

```r
inspect(sort(rules, by = 'confidence'), decreasing = T)[1:5]
```

```
##       lhs                                         rhs                support    confidence coverage   lift     count
## [1]   {citrus fruit,root vegetables}           => {other vegetables} 0.01037112 0.5862069  0.01769192 3.029608 102  
## [2]   {tropical fruit,root vegetables}         => {other vegetables} 0.01230300 0.5845411  0.02104728 3.020999 121  
## [3]   {curd,yogurt}                            => {whole milk}       0.01006609 0.5823529  0.01728521 2.279125  99  
## [4]   {other vegetables,butter}                => {whole milk}       0.01148958 0.5736041  0.02003050 2.244885 113  
## [5]   {tropical fruit,root vegetables}         => {whole milk}       0.01199797 0.5700483  0.02104728 2.230969 118  
## [6]   {root vegetables,yogurt}                 => {whole milk}       0.01453991 0.5629921  0.02582613 2.203354 143  
## [7]   {other vegetables,domestic eggs}         => {whole milk}       0.01230300 0.5525114  0.02226741 2.162336 121  
## [8]   {yogurt,whipped/sour cream}              => {whole milk}       0.01087951 0.5245098  0.02074225 2.052747 107  
## [9]   {root vegetables,rolls/buns}             => {whole milk}       0.01270971 0.5230126  0.02430097 2.046888 125  
## [10]  {pip fruit,other vegetables}             => {whole milk}       0.01352313 0.5175097  0.02613116 2.025351 133  
## [11]  {tropical fruit,yogurt}                  => {whole milk}       0.01514997 0.5173611  0.02928317 2.024770 149  
## [12]  {other vegetables,yogurt}                => {whole milk}       0.02226741 0.5128806  0.04341637 2.007235 219  
## [13]  {other vegetables,whipped/sour cream}    => {whole milk}       0.01464159 0.5070423  0.02887646 1.984385 144  
## [14]  {root vegetables,rolls/buns}             => {other vegetables} 0.01220132 0.5020921  0.02430097 2.594890 120  
## [15]  {root vegetables,yogurt}                 => {other vegetables} 0.01291307 0.5000000  0.02582613 2.584078 127  
## [16]  {other vegetables,fruit/vegetable juice} => {whole milk}       0.01047280 0.4975845  0.02104728 1.947371 103  
## [17]  {butter}                                 => {whole milk}       0.02755465 0.4972477  0.05541434 1.946053 271  
## [18]  {curd}                                   => {whole milk}       0.02613116 0.4904580  0.05327911 1.919481 257  
## [19]  {yogurt,whipped/sour cream}              => {other vegetables} 0.01016777 0.4901961  0.02074225 2.533410 100  
## [20]  {root vegetables,other vegetables}       => {whole milk}       0.02318251 0.4892704  0.04738180 1.914833 228  
## [21]  {tropical fruit,other vegetables}        => {whole milk}       0.01708185 0.4759207  0.03589222 1.862587 168  
## [22]  {citrus fruit,yogurt}                    => {whole milk}       0.01026945 0.4741784  0.02165735 1.855768 101  
## [23]  {root vegetables,whole milk}             => {other vegetables} 0.02318251 0.4740125  0.04890696 2.449770 228  
## [24]  {domestic eggs}                          => {whole milk}       0.02999492 0.4727564  0.06344687 1.850203 295  
## [25]  {pork,other vegetables}                  => {whole milk}       0.01016777 0.4694836  0.02165735 1.837394 100  
## [26]  {other vegetables,pastry}                => {whole milk}       0.01057448 0.4684685  0.02257245 1.833421 104  
## [27]  {onions}                                 => {other vegetables} 0.01423488 0.4590164  0.03101169 2.372268 140  
## [28]  {pork,whole milk}                        => {other vegetables} 0.01016777 0.4587156  0.02216573 2.370714 100  
## [29]  {whole milk,whipped/sour cream}          => {other vegetables} 0.01464159 0.4542587  0.03223183 2.347679 144  
## [30]  {yogurt,rolls/buns}                      => {whole milk}       0.01555669 0.4526627  0.03436706 1.771563 153  
## [31]  {citrus fruit,other vegetables}          => {whole milk}       0.01301474 0.4507042  0.02887646 1.763898 128  
## [32]  {whipped/sour cream}                     => {whole milk}       0.03223183 0.4496454  0.07168277 1.759754 317  
## [33]  {pip fruit,whole milk}                   => {other vegetables} 0.01352313 0.4493243  0.03009659 2.322178 133  
## [34]  {root vegetables}                        => {whole milk}       0.04890696 0.4486940  0.10899847 1.756031 481  
## [35]  {tropical fruit,rolls/buns}              => {whole milk}       0.01098119 0.4462810  0.02460600 1.746587 108  
## [36]  {sugar}                                  => {whole milk}       0.01504830 0.4444444  0.03385867 1.739400 148  
## [37]  {hamburger meat}                         => {whole milk}       0.01474326 0.4434251  0.03324860 1.735410 145  
## [38]  {ham}                                    => {whole milk}       0.01148958 0.4414062  0.02602949 1.727509 113  
## [39]  {sliced cheese}                          => {whole milk}       0.01077783 0.4398340  0.02450432 1.721356 106  
## [40]  {root vegetables}                        => {other vegetables} 0.04738180 0.4347015  0.10899847 2.246605 466  
## [41]  {other vegetables,bottled water}         => {whole milk}       0.01077783 0.4344262  0.02480935 1.700192 106  
## [42]  {citrus fruit,whole milk}                => {other vegetables} 0.01301474 0.4266667  0.03050330 2.205080 128  
## [43]  {other vegetables,soda}                  => {whole milk}       0.01392984 0.4254658  0.03274021 1.665124 137  
## [44]  {frozen vegetables}                      => {whole milk}       0.02043721 0.4249471  0.04809354 1.663094 201  
## [45]  {tropical fruit,yogurt}                  => {other vegetables} 0.01230300 0.4201389  0.02928317 2.171343 121  
## [46]  {other vegetables,rolls/buns}            => {whole milk}       0.01789527 0.4200477  0.04260295 1.643919 176  
## [47]  {chicken}                                => {other vegetables} 0.01789527 0.4170616  0.04290798 2.155439 176  
## [48]  {whole milk,butter}                      => {other vegetables} 0.01148958 0.4169742  0.02755465 2.154987 113  
## [49]  {hamburger meat}                         => {other vegetables} 0.01382816 0.4159021  0.03324860 2.149447 136  
## [50]  {cream cheese }                          => {whole milk}       0.01647178 0.4153846  0.03965430 1.625670 162  
## [51]  {butter milk}                            => {whole milk}       0.01159126 0.4145455  0.02796136 1.622385 114  
## [52]  {margarine}                              => {whole milk}       0.02419929 0.4131944  0.05856634 1.617098 238  
## [53]  {hard cheese}                            => {whole milk}       0.01006609 0.4107884  0.02450432 1.607682  99  
## [54]  {whole milk,domestic eggs}               => {other vegetables} 0.01230300 0.4101695  0.02999492 2.119820 121  
## [55]  {chicken}                                => {whole milk}       0.01759024 0.4099526  0.04290798 1.604411 173  
## [56]  {white bread}                            => {whole milk}       0.01708185 0.4057971  0.04209456 1.588147 168  
## [57]  {beef}                                   => {whole milk}       0.02125064 0.4050388  0.05246568 1.585180 209  
## [58]  {tropical fruit,whole milk}              => {other vegetables} 0.01708185 0.4038462  0.04229792 2.087140 168  
## [59]  {tropical fruit}                         => {whole milk}       0.04229792 0.4031008  0.10493137 1.577595 416  
## [60]  {whipped/sour cream}                     => {other vegetables} 0.02887646 0.4028369  0.07168277 2.081924 284  
## [61]  {oil}                                    => {whole milk}       0.01128622 0.4021739  0.02806304 1.573968 111  
## [62]  {yogurt}                                 => {whole milk}       0.05602440 0.4016035  0.13950178 1.571735 551  
## [63]  {pip fruit}                              => {whole milk}       0.03009659 0.3978495  0.07564820 1.557043 296  
## [64]  {whole milk,yogurt}                      => {other vegetables} 0.02226741 0.3974592  0.05602440 2.054131 219  
## [65]  {whole milk,fruit/vegetable juice}       => {other vegetables} 0.01047280 0.3931298  0.02663955 2.031756 103  
## [66]  {onions}                                 => {whole milk}       0.01209964 0.3901639  0.03101169 1.526965 119  
## [67]  {hygiene articles}                       => {whole milk}       0.01281139 0.3888889  0.03294357 1.521975 126  
## [68]  {brown bread}                            => {whole milk}       0.02521607 0.3887147  0.06487036 1.521293 248  
## [69]  {other vegetables}                       => {whole milk}       0.07483477 0.3867578  0.19349263 1.513634 736  
## [70]  {whole milk,curd}                        => {yogurt}           0.01006609 0.3852140  0.02613116 2.761356  99  
## [71]  {pork}                                   => {whole milk}       0.02216573 0.3844797  0.05765125 1.504719 218  
## [72]  {yogurt,soda}                            => {whole milk}       0.01047280 0.3828996  0.02735130 1.498535 103  
## [73]  {sausage,other vegetables}               => {whole milk}       0.01016777 0.3773585  0.02694459 1.476849 100  
## [74]  {napkins}                                => {whole milk}       0.01972547 0.3766990  0.05236401 1.474268 194  
## [75]  {beef}                                   => {other vegetables} 0.01972547 0.3759690  0.05246568 1.943066 194  
## [76]  {pork}                                   => {other vegetables} 0.02165735 0.3756614  0.05765125 1.941476 213  
## [77]  {pastry}                                 => {whole milk}       0.03324860 0.3737143  0.08896797 1.462587 327  
## [78]  {butter milk}                            => {other vegetables} 0.01037112 0.3709091  0.02796136 1.916916 102  
## [79]  {frozen vegetables}                      => {other vegetables} 0.01779359 0.3699789  0.04809354 1.912108 175  
## [80]  {dessert}                                => {whole milk}       0.01372649 0.3698630  0.03711235 1.447514 135  
## [81]  {citrus fruit}                           => {whole milk}       0.03050330 0.3685504  0.08276563 1.442377 300  
## [82]  {fruit/vegetable juice}                  => {whole milk}       0.02663955 0.3684951  0.07229283 1.442160 262  
## [83]  {butter}                                 => {other vegetables} 0.02003050 0.3614679  0.05541434 1.868122 197  
## [84]  {long life bakery product}               => {whole milk}       0.01352313 0.3614130  0.03741739 1.414444 133  
## [85]  {citrus fruit,other vegetables}          => {root vegetables}  0.01037112 0.3591549  0.02887646 3.295045 102  
## [86]  {tropical fruit,whole milk}              => {yogurt}           0.01514997 0.3581731  0.04229792 2.567516 149  
## [87]  {berries}                                => {whole milk}       0.01179461 0.3547401  0.03324860 1.388328 116  
## [88]  {other vegetables,whipped/sour cream}    => {yogurt}           0.01016777 0.3521127  0.02887646 2.524073 100  
## [89]  {domestic eggs}                          => {other vegetables} 0.02226741 0.3509615  0.06344687 1.813824 219  
## [90]  {citrus fruit}                           => {other vegetables} 0.02887646 0.3488943  0.08276563 1.803140 284  
## [91]  {frankfurter}                            => {whole milk}       0.02053889 0.3482759  0.05897306 1.363029 202  
## [92]  {whole milk,soda}                        => {other vegetables} 0.01392984 0.3477157  0.04006101 1.797049 137  
## [93]  {cream cheese }                          => {other vegetables} 0.01372649 0.3461538  0.03965430 1.788977 135  
## [94]  {pip fruit}                              => {other vegetables} 0.02613116 0.3454301  0.07564820 1.785237 257  
## [95]  {tropical fruit,other vegetables}        => {root vegetables}  0.01230300 0.3427762  0.03589222 3.144780 121  
## [96]  {tropical fruit,other vegetables}        => {yogurt}           0.01230300 0.3427762  0.03589222 2.457146 121  
## [97]  {newspapers}                             => {whole milk}       0.02735130 0.3426752  0.07981698 1.341110 269  
## [98]  {tropical fruit}                         => {other vegetables} 0.03589222 0.3420543  0.10493137 1.767790 353  
## [99]  {sausage,whole milk}                     => {other vegetables} 0.01016777 0.3401361  0.02989324 1.757876 100  
## [100] {whole milk,whipped/sour cream}          => {yogurt}           0.01087951 0.3375394  0.03223183 2.419607 107  
## [101] {margarine}                              => {other vegetables} 0.01972547 0.3368056  0.05856634 1.740663 194  
## [102] {citrus fruit,whole milk}                => {yogurt}           0.01026945 0.3366667  0.03050330 2.413350 101  
## [103] {chocolate}                              => {whole milk}       0.01667514 0.3360656  0.04961871 1.315243 164  
## [104] {yogurt,rolls/buns}                      => {other vegetables} 0.01148958 0.3343195  0.03436706 1.727815 113  
## [105] {beef}                                   => {root vegetables}  0.01738688 0.3313953  0.05246568 3.040367 171  
## [106] {waffles}                                => {whole milk}       0.01270971 0.3306878  0.03843416 1.294196 125  
## [107] {white bread}                            => {other vegetables} 0.01372649 0.3260870  0.04209456 1.685268 135  
## [108] {frankfurter}                            => {rolls/buns}       0.01921708 0.3258621  0.05897306 1.771616 189  
## [109] {sausage}                                => {rolls/buns}       0.03060498 0.3257576  0.09395018 1.771048 301  
## [110] {curd}                                   => {yogurt}           0.01728521 0.3244275  0.05327911 2.325615 170  
## [111] {curd}                                   => {other vegetables} 0.01718353 0.3225191  0.05327911 1.666829 169  
## [112] {coffee}                                 => {whole milk}       0.01870869 0.3222417  0.05805796 1.261141 184  
## [113] {sugar}                                  => {other vegetables} 0.01077783 0.3183183  0.03385867 1.645119 106  
## [114] {sausage}                                => {whole milk}       0.02989324 0.3181818  0.09395018 1.245252 294  
## [115] {berries}                                => {yogurt}           0.01057448 0.3180428  0.03324860 2.279848 104  
## [116] {whole milk,pastry}                      => {other vegetables} 0.01057448 0.3180428  0.03324860 1.643695 104  
## [117] {whole milk,rolls/buns}                  => {other vegetables} 0.01789527 0.3159785  0.05663447 1.633026 176  
## [118] {whole milk,bottled water}               => {other vegetables} 0.01077783 0.3136095  0.03436706 1.620783 106  
## [119] {cream cheese }                          => {yogurt}           0.01240468 0.3128205  0.03965430 2.242412 122  
## [120] {dessert}                                => {other vegetables} 0.01159126 0.3123288  0.03711235 1.614164 114  
## [121] {yogurt}                                 => {other vegetables} 0.04341637 0.3112245  0.13950178 1.608457 427  
## [122] {bottled water}                          => {whole milk}       0.03436706 0.3109476  0.11052364 1.216940 338  
## [123] {other vegetables,whole milk}            => {root vegetables}  0.02318251 0.3097826  0.07483477 2.842082 228  
## [124] {berries}                                => {other vegetables} 0.01026945 0.3088685  0.03324860 1.596280 101  
## [125] {rolls/buns}                             => {whole milk}       0.05663447 0.3079049  0.18393493 1.205032 557
```

```
##                                            lhs                   rhs    support confidence
## [1]             {citrus fruit,root vegetables} => {other vegetables} 0.01037112  0.5862069
## [2]           {tropical fruit,root vegetables} => {other vegetables} 0.01230300  0.5845411
## [3]                              {curd,yogurt} =>       {whole milk} 0.01006609  0.5823529
## [4]                  {other vegetables,butter} =>       {whole milk} 0.01148958  0.5736041
## [5]           {tropical fruit,root vegetables} =>       {whole milk} 0.01199797  0.5700483
## [6]                   {root vegetables,yogurt} =>       {whole milk} 0.01453991  0.5629921
## [7]           {other vegetables,domestic eggs} =>       {whole milk} 0.01230300  0.5525114
## [8]                {yogurt,whipped/sour cream} =>       {whole milk} 0.01087951  0.5245098
## [9]               {root vegetables,rolls/buns} =>       {whole milk} 0.01270971  0.5230126
## [10]              {pip fruit,other vegetables} =>       {whole milk} 0.01352313  0.5175097
## [11]                   {tropical fruit,yogurt} =>       {whole milk} 0.01514997  0.5173611
## [12]                 {other vegetables,yogurt} =>       {whole milk} 0.02226741  0.5128806
## [13]     {other vegetables,whipped/sour cream} =>       {whole milk} 0.01464159  0.5070423
## [14]              {root vegetables,rolls/buns} => {other vegetables} 0.01220132  0.5020921
## [15]                  {root vegetables,yogurt} => {other vegetables} 0.01291307  0.5000000
## [16]  {other vegetables,fruit/vegetable juice} =>       {whole milk} 0.01047280  0.4975845
## [17]                                  {butter} =>       {whole milk} 0.02755465  0.4972477
## [18]                                    {curd} =>       {whole milk} 0.02613116  0.4904580
## [19]               {yogurt,whipped/sour cream} => {other vegetables} 0.01016777  0.4901961
## [20]        {root vegetables,other vegetables} =>       {whole milk} 0.02318251  0.4892704
## [21]         {tropical fruit,other vegetables} =>       {whole milk} 0.01708185  0.4759207
## [22]                     {citrus fruit,yogurt} =>       {whole milk} 0.01026945  0.4741784
## [23]              {root vegetables,whole milk} => {other vegetables} 0.02318251  0.4740125
## [24]                           {domestic eggs} =>       {whole milk} 0.02999492  0.4727564
## [25]                   {pork,other vegetables} =>       {whole milk} 0.01016777  0.4694836
## [26]                 {other vegetables,pastry} =>       {whole milk} 0.01057448  0.4684685
## [27]                                  {onions} => {other vegetables} 0.01423488  0.4590164
## [28]                         {pork,whole milk} => {other vegetables} 0.01016777  0.4587156
## [29]           {whole milk,whipped/sour cream} => {other vegetables} 0.01464159  0.4542587
## [30]                       {yogurt,rolls/buns} =>       {whole milk} 0.01555669  0.4526627
## [31]           {citrus fruit,other vegetables} =>       {whole milk} 0.01301474  0.4507042
## [32]                      {whipped/sour cream} =>       {whole milk} 0.03223183  0.4496454
## [33]                    {pip fruit,whole milk} => {other vegetables} 0.01352313  0.4493243
## [34]                         {root vegetables} =>       {whole milk} 0.04890696  0.4486940
## [35]               {tropical fruit,rolls/buns} =>       {whole milk} 0.01098119  0.4462810
## [36]                                   {sugar} =>       {whole milk} 0.01504830  0.4444444
## [37]                          {hamburger meat} =>       {whole milk} 0.01474326  0.4434251
## [38]                                     {ham} =>       {whole milk} 0.01148958  0.4414062
## [39]                           {sliced cheese} =>       {whole milk} 0.01077783  0.4398340
## [40]                         {root vegetables} => {other vegetables} 0.04738180  0.4347015
## [41]          {other vegetables,bottled water} =>       {whole milk} 0.01077783  0.4344262
## [42]                 {citrus fruit,whole milk} => {other vegetables} 0.01301474  0.4266667
## [43]                   {other vegetables,soda} =>       {whole milk} 0.01392984  0.4254658
## [44]                       {frozen vegetables} =>       {whole milk} 0.02043721  0.4249471
## [45]                   {tropical fruit,yogurt} => {other vegetables} 0.01230300  0.4201389
## [46]             {other vegetables,rolls/buns} =>       {whole milk} 0.01789527  0.4200477
## [47]                                 {chicken} => {other vegetables} 0.01789527  0.4170616
## [48]                       {whole milk,butter} => {other vegetables} 0.01148958  0.4169742
## [49]                          {hamburger meat} => {other vegetables} 0.01382816  0.4159021
## [50]                           {cream cheese } =>       {whole milk} 0.01647178  0.4153846
## [51]                             {butter milk} =>       {whole milk} 0.01159126  0.4145455
## [52]                               {margarine} =>       {whole milk} 0.02419929  0.4131944
## [53]                             {hard cheese} =>       {whole milk} 0.01006609  0.4107884
## [54]                {whole milk,domestic eggs} => {other vegetables} 0.01230300  0.4101695
## [55]                                 {chicken} =>       {whole milk} 0.01759024  0.4099526
## [56]                             {white bread} =>       {whole milk} 0.01708185  0.4057971
## [57]                                    {beef} =>       {whole milk} 0.02125064  0.4050388
## [58]               {tropical fruit,whole milk} => {other vegetables} 0.01708185  0.4038462
## [59]                          {tropical fruit} =>       {whole milk} 0.04229792  0.4031008
## [60]                      {whipped/sour cream} => {other vegetables} 0.02887646  0.4028369
## [61]                                     {oil} =>       {whole milk} 0.01128622  0.4021739
## [62]                                  {yogurt} =>       {whole milk} 0.05602440  0.4016035
## [63]                               {pip fruit} =>       {whole milk} 0.03009659  0.3978495
## [64]                       {whole milk,yogurt} => {other vegetables} 0.02226741  0.3974592
## [65]        {whole milk,fruit/vegetable juice} => {other vegetables} 0.01047280  0.3931298
## [66]                                  {onions} =>       {whole milk} 0.01209964  0.3901639
## [67]                        {hygiene articles} =>       {whole milk} 0.01281139  0.3888889
## [68]                             {brown bread} =>       {whole milk} 0.02521607  0.3887147
## [69]                        {other vegetables} =>       {whole milk} 0.07483477  0.3867578
## [70]                         {whole milk,curd} =>           {yogurt} 0.01006609  0.3852140
## [71]                                    {pork} =>       {whole milk} 0.02216573  0.3844797
## [72]                             {yogurt,soda} =>       {whole milk} 0.01047280  0.3828996
## [73]                {sausage,other vegetables} =>       {whole milk} 0.01016777  0.3773585
## [74]                                 {napkins} =>       {whole milk} 0.01972547  0.3766990
## [75]                                    {beef} => {other vegetables} 0.01972547  0.3759690
## [76]                                    {pork} => {other vegetables} 0.02165735  0.3756614
## [77]                                  {pastry} =>       {whole milk} 0.03324860  0.3737143
## [78]                             {butter milk} => {other vegetables} 0.01037112  0.3709091
## [79]                       {frozen vegetables} => {other vegetables} 0.01779359  0.3699789
## [80]                                 {dessert} =>       {whole milk} 0.01372649  0.3698630
## [81]                            {citrus fruit} =>       {whole milk} 0.03050330  0.3685504
## [82]                   {fruit/vegetable juice} =>       {whole milk} 0.02663955  0.3684951
## [83]                                  {butter} => {other vegetables} 0.02003050  0.3614679
## [84]                {long life bakery product} =>       {whole milk} 0.01352313  0.3614130
## [85]           {citrus fruit,other vegetables} =>  {root vegetables} 0.01037112  0.3591549
## [86]               {tropical fruit,whole milk} =>           {yogurt} 0.01514997  0.3581731
## [87]                                 {berries} =>       {whole milk} 0.01179461  0.3547401
## [88]     {other vegetables,whipped/sour cream} =>           {yogurt} 0.01016777  0.3521127
## [89]                           {domestic eggs} => {other vegetables} 0.02226741  0.3509615
## [90]                            {citrus fruit} => {other vegetables} 0.02887646  0.3488943
## [91]                             {frankfurter} =>       {whole milk} 0.02053889  0.3482759
## [92]                         {whole milk,soda} => {other vegetables} 0.01392984  0.3477157
## [93]                           {cream cheese } => {other vegetables} 0.01372649  0.3461538
## [94]                               {pip fruit} => {other vegetables} 0.02613116  0.3454301
## [95]         {tropical fruit,other vegetables} =>  {root vegetables} 0.01230300  0.3427762
## [96]         {tropical fruit,other vegetables} =>           {yogurt} 0.01230300  0.3427762
## [97]                              {newspapers} =>       {whole milk} 0.02735130  0.3426752
## [98]                          {tropical fruit} => {other vegetables} 0.03589222  0.3420543
## [99]                      {sausage,whole milk} => {other vegetables} 0.01016777  0.3401361
## [100]          {whole milk,whipped/sour cream} =>           {yogurt} 0.01087951  0.3375394
## [101]                              {margarine} => {other vegetables} 0.01972547  0.3368056
## [102]                {citrus fruit,whole milk} =>           {yogurt} 0.01026945  0.3366667
## [103]                              {chocolate} =>       {whole milk} 0.01667514  0.3360656
## [104]                      {yogurt,rolls/buns} => {other vegetables} 0.01148958  0.3343195
## [105]                                   {beef} =>  {root vegetables} 0.01738688  0.3313953
## [106]                                {waffles} =>       {whole milk} 0.01270971  0.3306878
## [107]                            {white bread} => {other vegetables} 0.01372649  0.3260870
## [108]                            {frankfurter} =>       {rolls/buns} 0.01921708  0.3258621
## [109]                                {sausage} =>       {rolls/buns} 0.03060498  0.3257576
## [110]                                   {curd} =>           {yogurt} 0.01728521  0.3244275
## [111]                                   {curd} => {other vegetables} 0.01718353  0.3225191
## [112]                                 {coffee} =>       {whole milk} 0.01870869  0.3222417
## [113]                                  {sugar} => {other vegetables} 0.01077783  0.3183183
## [114]                                {sausage} =>       {whole milk} 0.02989324  0.3181818
## [115]                                {berries} =>           {yogurt} 0.01057448  0.3180428
## [116]                      {whole milk,pastry} => {other vegetables} 0.01057448  0.3180428
## [117]                  {whole milk,rolls/buns} => {other vegetables} 0.01789527  0.3159785
## [118]               {whole milk,bottled water} => {other vegetables} 0.01077783  0.3136095
## [119]                          {cream cheese } =>           {yogurt} 0.01240468  0.3128205
## [120]                                {dessert} => {other vegetables} 0.01159126  0.3123288
## [121]                                 {yogurt} => {other vegetables} 0.04341637  0.3112245
## [122]                          {bottled water} =>       {whole milk} 0.03436706  0.3109476
## [123]            {other vegetables,whole milk} =>  {root vegetables} 0.02318251  0.3097826
## [124]                                {berries} => {other vegetables} 0.01026945  0.3088685
## [125]                             {rolls/buns} =>       {whole milk} 0.05663447  0.3079049
```

#### **lhs**를 샀을 때 **rhs**를 구매하는 규칙. apriori는 **중복 규칙**이 존재해 직접 구현해서 중복 가지를 없애야 한다.


```r
new_rules = function(rules){
  rule = is.subset(rules, rules, sparse = F)
  rule[lower.tri(rule, diag = T)] = NA
  col = colSums(rule, na.rm = T) >= 1
  p.rule = rules[!col]
  return(p.rule)
}
```


```r
params = list(supp = .001, conf = .5, minlen = 2)
rules = apriori(Groceries, parameter = params, appearance = list(default = 'lhs', rhs = 'soda'),
                control = list(verbose = F))
rules = new_rules(rules)
rules = sort(rules, decreasing = T, by = 'confidence')
inspect(rules[1:5])
```

```
##     lhs                                     rhs    support     confidence coverage    lift     count
## [1] {coffee,misc. beverages}             => {soda} 0.001016777 0.7692308  0.001321810 4.411303 10   
## [2] {sausage,bottled water,bottled beer} => {soda} 0.001118454 0.7333333  0.001525165 4.205442 11   
## [3] {sausage,white bread,shopping bags}  => {soda} 0.001016777 0.6666667  0.001525165 3.823129 10   
## [4] {rolls/buns,bottled water,chocolate} => {soda} 0.001321810 0.6500000  0.002033554 3.727551 13   
## [5] {pastry,misc. beverages}             => {soda} 0.001220132 0.6315789  0.001931876 3.621912 12
```
