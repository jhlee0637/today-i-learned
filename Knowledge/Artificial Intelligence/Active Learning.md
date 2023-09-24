- Active Learning은 machine learning(ML) 모델을 훈련 시키기 위해 인간이 직접 데이터를 모두 라벨링 시키기 어렵다는 점을 해결하기 위해 만들어지 개념이다.
- 인간이 일부 데이터에 대하여 라벨링을 하고 제시하면, 모델이 나머지 데이터들을 평가하고, 이 중 라벨링이 필요하다고 판단되는 중요한 데이터는 다시 인간에게 건내준다.
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FY3XYy%2FbtqGishAHQX%2FOaVY0ywxxsd3yPwckOB81k%2Fimg.png">

# Three scienarios of Active Learning
### 1. Membership Query Synthesis
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FwDUQn%2FbtqGewyBhJH%2FddZ2JWK7n3mNPsK4N7Nr20%2Fimg.png">

-  학습모델이 주어진 데이터를 활용해서 약간 왜곡된 데이터 인스턴스를 생성한 후, 이에 대한 라벨링을 인간에게 요구한다.

### 2. Stream-Based Selective Sampling
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FuZHQk%2FbtqGh5trbmp%2FShGf5Y6wvONJzRlFBsDC6K%2Fimg.png">

- 학습모델이 주어진 데이터의 정보량을 평가하고, 라벨링이 필요하다고 판단되는 경우에만 인간에게 전달한다.
- 정보량을 평가할 때는 [[Query Strategy]]를 사용한다. 라벨링이 필요하다고 판단되는 경우는 query하고 아닌 것은 버린다.

### 3. Pool-Based Sampling
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbYge1J%2FbtqGishA6lv%2FUlUodeq23UIJYd1WNNnqWK%2Fimg.png">

- 가장 널리 사용된다.
- 라벨링 되지 않은 데이터가 매우 많을 때 사용한다.
- 학습모델이 주어진 데이터를 평가하고, 정보량이 가장 많은 데이터만 선택해서 인간에게 전달한다.
- 정보량을 평가할 때 버리는 instance가 존재하지 않는다.

참고: https://littlefoxdiary.tistory.com/52