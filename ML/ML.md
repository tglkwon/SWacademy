# 220927
# 데이터의 종류
nominal : 이름
ordinal : 순서가 있는 (s, m, b 크기 등)
interval : 순서에 간격이 규칙적인(날짜, 시간 등)
Ratio : 비율, 절대 기준이 있는 데이터
후자로 갈 수록 정보가 많고 좋은 데이터이다.

양을 나타내는 데이터와 질을 나타내는 데이터가 있다.
discrete 
continuous

# 데이터 관련 정의
정답값 : class or target : class는 코딩시 문제 생길 수 있으므로 target : 보통 y로 표현(vector)
Feature : attributes, dimensions, columns : 보통 X로 표현(matrix형태라서)

## 딥러닝이 나오게 된 이유
전통적 알고리즘들은 빅데이터 영역에서 다뤄질 것을 전제 하지 않았기에 생각지 못했던 단점이 있었다.
어떤 전통적 알고리즘들이라도 성능이 어느 한계에서 수렴하는 듯한 현상
plateau in performance가 나타난다.
딥 러닝이 더 큰 빅데이터을 널어서 전통적 알고리즘의 성능을 추월하면서 각광받게 되었다.

## 차원의 저주
데이터의 차원이 증가할 수록, 학습에 필요한 데이터의 개수가 기하급수적으로 늘어나는 문제
데이터의 양이 부족하면 모델이 학습이 덜 되서 데이터의 전체 모집단의 데이터를 입력했는데 결과값의 편차가 커지는 
overfitting이 나타난다.


# feature selection : filter, wrapper, embedded
차원의 저주를 덜하게 하는 역할이 있다.

# 데이터의 품질을 측정하는 방법
## 충분성 : 데이터의 양이 학습하기에 충분한지 알 수있다. : 러닝커브를 이용한다.
## 대표성 : sampling noise : 우연에 의한 대표셩이 없는 데이터 : sampling bias가 생길 수 있다.
## 