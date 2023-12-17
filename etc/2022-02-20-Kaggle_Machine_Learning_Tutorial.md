---
layout: post
title: "Kaggle Machine Learning Tutorial 따라해보기"
subtitle: "Kaggle에서 제공하는 machine learning tutorial을 따라해보자"
date: 2022-02-20
author: "Lee Je Hee"
URL: "/2022/02/20/Kaggle_Machine_Learning_Tutorial/"
tags:
 - Kaggle
 - Machine Learning
 - Tutorial
---
[Kaggle의 "intro to machine learning"]( https://www.kaggle.com/learn/intro-to-machine-learning) 은 강의와 복습문제로 이루어져 있다.\
복습은 개인 컴퓨터 내에서 코드를 구현할 필요가 없이, 웹페이지 내 Kaggle Notebooks을 이용하여 풀어볼 수 있다는 장점이 있다.\
강의에서 소개하는 소요 시간은 총 3시간이며, 코딩에 익숙한 사람이라면 하루 안에 끝낼 수 있다고 생각한다.
## 1강: How Models Work
Machine learning 모델에는 다양한 종류가 있으며, 그 중 하나는 ‘**Decision tree**’ 모델이다.\
이번 tutorial은 decision tree 모델을 대상으로 이루어진다.

Machine learning을 공부할 때 모델과 관련되서는 다음과 같은 용어들에 익숙해져야한다.
- 데이터를 던져주고 모델을 훈련시키는 것을 ‘**fitting**’ 혹은 ‘**training**’이라고 한다.
- 모델을 ‘fit’하기 위하여 던져주는 데이터를 ‘**training data**’라고 한다.
- ‘Decision tree’에서 질문의 단계를 많이 두는 것을 ‘**deep**’해지는 과정이라고 한다.
- ‘Decision tree’에서 최종적으로 나온 결과를 ‘**leap**’이라고 한다.

## 2강: Basic Data Exploration
Machine learning을 위해서는 Python 안에 데이터 frame을 작성해야한다.\
데이터 frame 작성은 ‘**Pandas**’를 활용한다.

강의에서 사용하는 데이터는 [아이오와주 멜버른의 부동산 데이터](https://www.kaggle.com/dansbecker/melbourne-housing-snapshot)이다.\
다음의 명령어를 통해 해당 csv 파일을 불러온 뒤, 요약된 정보를 확인해보자.

`pd.read_scv(<파일>)` : 파일을 불러온다.\
`데이터.describe()` : pandas 파일의 요약을 본다.
```python
import pandas as pd

# save filepath to variable for easier access
melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'

# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path) 

# print a summary of the data in Melbourne data
print(melbourne_data.describe())
```
실제 csv 파일의 내용과 `.describe()` 함수를 통해 불러와지는 내용을 비교해봤다.

![](/img/2022_02/describe_function.png)
`데이터.describe()` 함수를 이용하는 경우 행의 이름이 바뀜을 알 수 있다.\
이 함수는 파일의 내용을 요약해주며, 각 행의 내용은 아래와 같다.
-   **count**: column이 가진 row의 갯수
-   **mean**: 평균값
-   **std**: 평균편차
-   **min~max**: 최소값 ~ 최대값

## 3강: Your First Machine Learning Model
데이터셋 파일을 열는 것을 배웠으니, 이제 파일에서 여러가지 내용을 출력해보자.\
먼저 데이터셋에서 어떤 column들이 있는지 출력해보자.\

`데이터.columns` : column 리스트를 출력
```python
print(melbourne_data.columns)
```

```python
# 실행결과
Index(['Suburb', 'Address', 'Rooms', 'Type', 'Price', 'Method', 'SellerG', 'Date', 'Distance', 'Postcode', 'Bedroom2', 'Bathroom', 'Car', 'Landsize', 'BuildingArea', 'YearBuilt', 'CouncilArea', 'Lattitude', 'Longtitude', 'Regionname', 'Propertycount'], dtype='object')
```
우리가 이런 엑셀파일로 된 데이터를 다룰 때, 모든 칸들이 항상 채워져 있는 것은 아니다.\
때로는 데이터 내에 빈칸들이 존재한다.\
이런 빈칸들을 ‘**결측값**’이라고 부른다.

만약 결측값이 있는 부분은 모델학습에서 제외하고 싶다면, 다음의 함수를 통해 제거할 수 있다.

`데이터.dropna(axis=)`: 결측값이 있는 **행** 또는 **열**을 제거

![pandas](https://t1.daumcdn.net/cfile/tistory/23572A36584C06AE03)

```python
melbourne_data = melbourne_data.dropna(axis=0)
```

이번 머신러닝 모델에서는 여러 조건에 따른 부동산의 ‘가격’을 leap으로 삼으려고 한다.\
이 data frame에서 ‘가격’은 1차원적인 데이터 집합으로 이루어져 있다.\
Python의 list와 비슷하게 data frame에서는 데이터 집합을 ‘**series**’라고 부른다.\
데이터 테이블 뒤에 `.<column 이름>`을 적어주면 그 column을 지정할 수 있다.

```python
y = melbourne_data.Price
```

부동산 ‘가격’을 결정하는 요소로는 ‘방’, ‘화장실’, ‘토지크기’, ‘위도’, ‘경도’를 삼으려고 한다.\
이렇게 머신러닝에서 결과값(y)을 얻기 위해 변수(X)로 삼는 것들을 ‘**features**’라고 부른다.

보통 한 column이 한 개의 feature가 된다.\
데이터 테이블에 `[feature1, feature2, ...]`과 같은 형태로 여러 features를 지정할 수 있다.

```python
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

X = melbourne_data[melbourne_features]
```

여기까지 우리는 데이터를 열고, 데이터 내용을 확인하고, 필요한 경우 일부 데이터는 솎아내며, 내가 원하는 데이터만 지정하는 방법을 배웠다.\
머신러닝을 위한 데이터가 준비됐다면 이제는 머신러닝에 대해서 공부해볼 차례다.

머신러닝은 4가지 단계를 거쳐서 완성된다.

1.  **define**: 머신러닝의 모델의 종류 선정 (ex. decision tree)
2.  **fit**: 주어진 데이터에서 패턴을 찾아서 모델을 훈련시킴
3.  **predict**: 새로운 데이터에서 모델을 활용해 예상결과를 출력
4.  **evaluate**: 모델의 예측결과가 얼마나 정확한지 평가

머신러닝을 위해서는 python 라이브러리 중 머신러닝에 특화된 sklearn을 사용한다.\
또한 decision tree 모델을 활용하므로, `DecisionTreeRegressor` 모듈을 불러온다.

**Decision tree 모델을 세울 때는 random seed 값을 설정해야한다.**\
해당 seed값은 나중에라도 동일한 데이터에 대해 수행하면 동일한 모델이 만들어지게된다.\
Random seed값의 의미는 데이터 중 몇 %를 모델훈련에 사용할지...라고 들었다.\
이제 세워진 머신러닝 모델에 훈련용 데이터를 넣고, `.fit()` 기능을 통해 모델을 학습시킨다.

```python
from sklearn.tree import DecisionTreeRegressor

melbourne_model = DecisionTreeRegressor(random_state=1)

melbourne_model.fit(X, y)
```

잠시 후 훈련이 끝나면 임의의 데이터를 삽입하여 예측된 결과를 둘러본다.\
이번 임의의 데이터로는 기존에 잡아놨던 X값들 중 head에 해당되는 값들을 사용했다.

```python
print(melbourne_model.predict(X.head()))
```

```python
#실행결과
[1035000. 1465000. 1600000. 1876000. 1636000.]
```

## 4강: Model Validation
머신러닝 모델을 통해 데이터를 만들었으면, 데이터의 quality를 평가해야 한다.\
훈련시킨 머신러닝 모델의 quality는 **예측 정확성(predictive accuracy)** 의 상대값에 따른다.\
예측 정확도를 평가할 때는 다음과 같은 점을 주의해야한다.

-   **훈련에 사용했던 데이터를 평가에 사용하면 안된다.**
-   예측한 값 중에는 '**잘 예측한 것**'과 '**잘못 예측한 것**'이 섞여있다.

멜버른 부동산 데이터를 예시로 생각해보자.\
멜버른 A번지의 집의 실제 가격이 있고, 우리가 훈련시킨 모델에서 예측한 가격이 있다.\
이때 **오차값**은 ‘실제 값’ - ‘예측 값’ 이 되며, 음수도 양수도 될 수 있다.\
따라서 이를 **절대값**으로 계산해 예측정확성을 확인한다.\
정리하자면,

- 모든 예측값과 실제값의 데이터를 얻고
- 절대 오차값까지 얻은 다음
- 이를 평균으로 나타내면 **MAE(Mean Absolute Error, 평균절대오차)**가 된다.

이제 코드를 통하여 모델을 훈련 및 예측정확성 평가를 수행해보겠다.\
먼저 7개의 조건에 따른 부동산 가격을 훈련시켜 모델을 만든다.

```python
# Data Loading Code Hidden Here
import pandas as pd

# Load data
melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 
# Filter rows with missing price values
filtered_melbourne_data = melbourne_data.dropna(axis=0)
# Choose target and features
y = filtered_melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 
                        'YearBuilt', 'Lattitude', 'Longtitude']
X = filtered_melbourne_data[melbourne_features]

from sklearn.tree import DecisionTreeRegressor
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(X, y)
```

이번에는 ‘훈련에 사용했던 데이터’를 사용하여 가격을 예측한 다음,\
얼마나 오류가 있는지 보기 위해 `mean_absolute_error()` 기능을 사용해 평균절대오차를 본다.

```python
from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(X)
print(mean_absolute_error(y, predicted_home_prices))
```

```python
#실행결과
434.71594577146544
```

### ‘훈련에 사용했던 데이터’를 모델 평가에 사용하면 안되는 이유
예를 들어 현재 멜버른의 모든 고급주택은 ‘초록색 문’을 가졌다고 가정해보자.\
이 데이터로 훈련된 모델은 ‘초록색 문을 가질 수록 고급주택이다’라고 판단한다.\
그리고 훈련에 사용했던 데이터를 가지고 머신러닝 모델을 평가하면,\
‘**초록색 문을 가지면 고급주택이다**’라는 명제가 마치 정확한 예측처럼 보이게 된다.

하지만 만약 이 모델에다가 미국 전역의 부동산 데이터에 넣으면?\
**미국 전역의 초록색 문이 달린 모든 주택을 고급주택이라고 판단할테니 모델의 예측도가 형편없었다는 사실을 알게된다.**

따라서 우연히 만들어진 편견을 버리기 위해 모델의 평가는 훈련과 상관없는 데이터를 사용해야 한다.\
가장 빠른 방법으로는 갖고있는 데이터를 **훈련용**과 **평가용**으로 미리 나누어 놓는 것이다.

scikit-learn 라이브러리는 test용 데이터를 미리 구분해주는 `train_test_split()` 기능이 있다.\
다음의 코드를 통하여 훈련용 데이터로만 모델을 훈련시켜보자.

```python
from sklearn.model_selection import train_test_split

# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.

train_X, val_X, train_y, val_y = train_test_splitX, y, random_state = 0)

# Define model
melbourne_model = DecisionTreeRegressor()

# Fit model
melbourne_model.fit(train_X, train_y)

# get predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
```

이제 얼마나 오류가 있는지 보기 위해 `mean_absolute_error()` 기능을 사용해 평균절대오차를 본다.

```python
print(mean_absolute_error(val_y, val_predictions))
```

```python
#실행결과
258930.03550677857
```

훈련 데이터에 포함된 부분으로 검사할 때에는 400 정도의 값이었으나,\
훈련에 포함되지 않은 데이터로 검사하자 258930으로 평균절대오차가 커졌다.

## 5강: Underfitting and Overfitting
[Decision tree 설명서](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html)를 읽어보면, 굉장히 다양한 옵션이 달려있다는 사실을 알 수 있다.\
그 중 가장 중요한 옵션은 바로 **tree’s depth**이다.

1강에서 봤듯이 tree's depth는 tree model의 복잡도를 결정한다.\
실제로 depth 단계가 10 이상인 경우도 흔한데, 이럴 경우 2^10(=1024)개의 leaves를 가지는 것과 같다.\
이를 튜토리얼의 주택 데이터에 대입해서 생각해보면,\
depth 10 단계에서는 주택 데이터가 1024개의 그룹으로 나뉠 수 있다는 것이다.

그러나 모든 주택들이 1024개의 기준에 따라서 동일하게 나눠지지는 않을 것이다.
어떤 그룹에는 많은 주택들이 해당될 것이고, 어떤 그룹에는 적은 주택들이 해당될 것이다. 

특히 적은 주택들만이 포함된 그룹은 예측에 문제가 될 수 있다.\
적은 표본들의 특징들을 뽑아내다보니 예측값이 아니라 주택들의 데이터값에 가깝게 되어버리고,\
새로운 데이터에 대해서 분류가 어려워질 수 있다.

위와 같은 상황을 **overfitting**이라고 부른다.\
완성된 모델이 훈련데이터의 값에 너무 특이적으로 완성되어서,\
새로운 데이터로 모델을 시험하면 예측이 부정확한 것이다.

반대로 depth 단계가 너무 얇아지는 상황을 생각해보자.\
수 많은 주택들을 2~4개의 그룹으로 나눈다면 당연히 그 그룹들은 제대로된 분류가 아닐 것이다.\
이 또한 새로운 데이터로 모델을 시험하면 예측이 부정확할 것이다.\
이를 **underfitting**이라고 한다.

따라서 모델이 신뢰할 수 있으려면 overfitting과 underfitting 그 사이의 중간지점에서 적절한 신뢰도를 가져야 한다.
![](/img/2022_02/graph.bmp)
validation값이 가장 낮은 부분이 바로 이상적인 부분이다

이제 decision tree 구조에서 overfitting인지 underfitting인지 모델을 평가하는 validation 과정을 수행해보겠다.\
Tree depth를 조절하는 방법은 다양하며, 그 중 하나는 `max_leaf_nodes`를 활용하는 방법이다.\
Validation에 앞서 먼저 모델을 훈련시킨다.
```python
# Data Loading Code Runs At This Point
import pandas as pd
    
# Load data
melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)

# Filter rows with missing values
filtered_melbourne_data = melbourne_data.dropna(axis=0)

# Choose target and features
y = filtered_melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
X = filtered_melbourne_data[melbourne_features]

from sklearn.model_selection import train_test_split

# split data into training and validation data, for both features and target
train_X, val_X, train_y, val_y = train_test_split(X, y,random_state = 0)
```

이제  `max_leaf_nodes` 값을 받아서 MAE(평균절대오차값)을 돌려주는 함수를 만들어본다.

```python
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)
```

이제 해당 함수를 이용해서 노드값이 5, 50, 500, 5000일 때를 비교해볼 수 있다.

```python
# compare MAE with differing values of max_leaf_nodes
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d \t\t Mean Absolute Error: %d" %(max_leaf_nodes, my_mae))
```

```python
#실행결과
Max leaf nodes: 5  		     Mean Absolute Error:  347380
Max leaf nodes: 50           Mean Absolute Error:  258171
Max leaf nodes: 500  		 Mean Absolute Error:  243495
Max leaf nodes: 5000  		 Mean Absolute Error:  254983
```

MAE 값이 가장 낮았던 노드값 500일 때의 MAE값이 가작 적으므로 적절한 값임을 알 수 있다.

## 6강: Random Forests
Leaf가 많아지면 overfitting이 발생하고, leaf가 적어지면 uderfitting이 발생한다.\
이는 머신러닝에서 피할 수 없는 요소이다.\
따라서 여러 모델들이 이런 문제를 해결하고자 노력했고,\
우리는 그 중 하나인 **Random forest**에 대하여 알아볼 것이다.

Random forest는 여러 tree 사용하여 예측값의 평균을 내준다.\
기본 파라미터들만 사용하여도 decision tree를 단독으로 사용한 것보다 좋은 결과를 내준다.\
Random forest는 `RandomForestRegressor` 클래스를 DecisionTreeRegressor 대신 사용하면 된다.\
다음의 예시를 통하여 직접 사용해보자.
```python
import pandas as pd
    
# Load data
melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 
# Filter rows with missing values
melbourne_data = melbourne_data.dropna(axis=0)
# Choose target and features
y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 
                        'YearBuilt', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]

from sklearn.model_selection import train_test_split

# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X, val_X, train_y, val_y = train_test_split(X, y,random_state = 0)
```

```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
melb_preds = forest_model.predict(val_X)
print(mean_absolute_error(val_y, melb_preds))
```

```python
#실행결과
191669.7536453626
```

## 7강: Machine Learning Competitions
마지막으로 Kaggle에서 열리는 competition에 실제로 참여해보자.\
마지막 강의인만큼 Kaggle Notebooks로 올라온 7강 실습 페이지의 코드를 찬찬히 뜯어보기로 했다.

먼저 필요한 라이브러리들을 불러온다.
```python
# Import helpful libraries
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
```

'train.csv' 파일을 `.read_csv()` 기능으로 불러온다.\
구하고자 하는 결과값 y는 주택의 가격인 'SalePrice'열로 정했다.

```Python
# Load the data, and separate the target
iowa_file_path = '../input/train.csv'
home_data = pd.read_csv(iowa_file_path)
y = home_data.SalePrice
```

결과값 y를 구하기 위한 변수들 X 로는 7가지의 열들을 골랐다.

```Python
# Create X (After completing the exercise, you can return to modify this line!)
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
```

7개의 변수들을 `<데이터>[<변수 리스트>]`로 지정하고, `.head()` 기능으로 점검한다.

```Python
# Select columns corresponding to features, and preview the data
X = home_data[features]
X.head()
```

`train_test_split()`를 이용하여 훈련에 사용할 데이터 train_X, train_y와 예측 정확도 검사에 필요한 데이터 val_X, val_y로 구분한다.

```python
# Split into validation and training data
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
```

`RandomForestRegressor()`를 이용하여 random forest 모델을 하나 만든다.\
해당 모델을 `.fit()`을 이용하여 fitting한다.\
Fitting이 끝난 모델에 대하여 `.predict()`에다 미리 준비한 데이터(모델 훈련에 사용되지 않은 데이터) val_X를 이용하여 예측값을 낸다.\
`mean_absolute_error()`를 이용하여 예측값과 실제 val_y값을 비교한다.

```Python
# Define a random forest model
rf_model = RandomForestRegressor(random_state=1)
rf_model.fit(train_X, train_y)
rf_val_predictions = rf_model.predict(val_X)
rf_val_mae = mean_absolute_error(rf_val_predictions, val_y)

print("Validation MAE for Random Forest Model: {:,.0f}".format(rf_val_mae))
```

``` Python
#실행결과
Validation MAE for Random Forest Model: 21,857
```

### 이제 위의 모델보다 더 정확한 예측을 할 수 있는 모델을 만들어보자
```python
# To improve accuracy, create a new Random Forest model which you will train on all training data
rf_model_on_full_data = RandomForestRegressor(random_state=0)

# fit rf_model_on_full_data on all data from the training data
rf_model_on_full_data.fit(X, y)
```
실습에서 요구한대로 주어진 데이터를 모두 모델 훈련에 사용하기 위하여 'random_state'를 0으로 설정하였다.\
또한 요구에 맞게 fitting도 전체 데이터 X, y를 사용했다.

```Python
# path to file you will use for predictions
test_data_path = '../input/test.csv'

# read test data file using pandas
test_data = pd.read_csv(test_data_path)

# create test_X which comes from test_data but includes only the columns you used for prediction.
# The list of columns is stored in a variable called features
test_X = test_data[features]

# make predictions which we will submit. 
test_preds = rf_model_on_full_data.predict(test_X)
```
이렇게해서 competition에 등록할 데이터 'test_preds'를 만들었다.\
여기까지만 수행하여도 인증서를 다음과 같이 받을 수 있다.

![](/img/2022_02/Kaggle_certification.png)
더 진행하면 kaggle notebook의 결과를 저장하고, 그 결과를 competition에 제출할 수 있다.

![](/img/2022_02/rank.png)

보아하니 다른 모델을 사용하여 더 좋은 점수를 받은 사람들이 있다.

이번 포스트를 통하여 처음으로 machine learning을 공부하고 실습해봤다.\
직접 모델을 구축하는 과정을 따라가보니 꽤나 재미있었다.\
앞으로도 더 많은 수업을 찾아보고 공부해봐야겠다.