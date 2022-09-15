
# 220913
매트랩은 state machine이라는 방식으로 작동한다. 논문 그림용으로 만든 언어라 기본 dpi가 72px이다.
```
import matplotlib.pyplot as plt
#import matplotlib.pylab as plt
plt.plot([1,2,3],[4,5,6])
plt.title('title')
plt.figure(figsize=(5,5))
plt.axes((0,0,1,1))
plt.title('sun')
plt.axes((0.5,0.5,.5,.5))
plt.title('sun')

```
state machine 특징
1. 변수를 지정하지 않는다. 하나의 셀에서 가장 가까운 애?가 변수가 된다
2. 가장 기본으로 정해지는 변수 plt.figure()
    안보이는 432*288자리 공간을 만든다

set, get을 accessor라고 부른다.
class에서 외부에서 값을 주는 경우 set, 그 값을 호출하는 경우 get이라 부른다.


## 재귀적 함수, 함수형 프로그래밍
```
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return fibonacci(n-1) + fibonacci(n-2)
```

flow control
for, while, or, if, elif, else, try except, finally 등을
최소화하는 방향으로 코드를 작성한다.
구문을 가능한 간단하게 쓴다.

### encapsulation 캡슐화
외부에서 함수 내부의 값이나 계산을 조정할 수 없어서 결과를 믿을 수 있다.
### 결합성
수학적 함수 처럼 서로 다른 함수를 결합해서 사용가능하다.
### comprehension 
데이터를 동시에 만들거나 연산시킬 때 쓴다
```
temp = []
for i in range(10000):
    temp.append(i+3)
#앞과 뒤의 코드 결과가 같다. 뒤가 실행 속도도 빠르다
[i+3 for i in range(10000)]     
# if문도 가능하다
[i+3 for i in range(10000) if i%2==0] 
[i if i%2==0 else 0 for i in range(10000)]

# for와 if를 중첩해서도 쓸 수 있다.
[(i,j) for i in range(100) for j in range(6,10)]
```

#### list comprehension, set comprehension, dictionary
[],{},{:}
- 메모리에 모든 데이터를 올리고 계산하기에 빠르다. 대신 메모리의 성능에 영향을 받는다
#### generator: iterator와 개념이 비슷하다
()
- Lazy :데이터를 필요할 때마다 불러와서 연산하여 메모리 성능을 덜 탄다. 대용량 파일 등을 처리 가능하다
전체 데이터 또는 결과를 한 번에 볼 수가 없어서 이전 결과나 특정 결과를 그때그때 볼 수 없다.
```
def x():
    yield 1
    yield 2
    yield 3
    yield from [1,'a', 3]
    
t = x()
t => generator
next(t) => yield가 나온다
```

class를 이용하여 generator를 duck typing(overriding)할 수 있다.

tail recursion elimiation : 함수형 언어에서 재귀함수를 빠르게 한번에 계산하는 방법.
일반적인 언어에서는 구현되어 있지 않아서 보통 직접 만들어쓴다

## reduce: 여러개의 값을 하나로 누적시키는거
## accumulation : 중간 결과를 계산하는 방법. 다 모으면 reduce와 같아진다.

reduce_sum : 1 + 2 + 3 + 4 + 5
                3 + 3 + 4 + 5
                 6 + 4 + 5
각 부분을 따로 연산하여 합칠 수 있다. ex) mapReduce()
분할 정복 : dividal conquer

# map : 머신러닝에서 쓰기에 빠르고 명확하다
```
map(lambda x:x+1, [1,2,3,4,5])
```

# 220914
## callable : 괄호를 붙일 수 있다.
1. 클래스
2. 함수, lambda
람다는 식으로 축약되어 하나의 값이다.
3. __call()__ : 객체 또는 인스턴스를 ()를 붙일 수 있게 만들어준다. => 함수처럼 사용하기 위한 방법
```
class A:
    #def __call__(self): # 이 부분이 없으면 콜이 안된다.
        pass

a = A()
a() => TypeError : callable 하지 않다.
```
중첩된 함수를 통해 clojure라는 기법을 쓴다. 중첩된 함수에 인자를 넘겨준다.
```
def x(m):
    def y(n):
        return m+n
    return y
    
x(3)(1)  => 4
```
파이선에서 clojure 생성하는 방법
```
class A:
    def __init__(self, m):
        self.m = m
    def __call__(self, n):
        return self.m+n
```

## static methods of instances
클래스 내부에 스태틱 메소드를 정의하면 내 클래스와 상관없는 클래스를 내 이름으로 접근할 수 있게 한다.
프로그래밍에 실수를 줄이고 구조화하기 쉽다.

## descrypter : accessor(get, set)를 관리하는 애
파이선의 get, set, delete는 원래 제약없이 사용할 수 있다.
functional programming, objective programming의 중요요소인 encalsulation을 활용하기 위해 디스크립터를 사용한다.

descrypter를 만드는 3가지 방법
1. descrypt
```
class A:
    def __init__(self):
        self.x = 0
    def __get__(self, a, b):
        print('get')
        return self.x
    def __set__(self, a, b):
        print('set')
        self.x = b      # b가 value
    
    
class B:
    x = A()
    
b = B()
b.x => 1  => __get__이 실행됨   
```
2. property
```
class A:
    def __init__(self):
        self.x = 0
    def g(self):
        print('get')
        return 1
    def s(self, x):
        self.x = x
        print('set')
    def d(self):
        print('del')
    y = property(g,s,d)
    
a = A()
a.y => get 1
a.y = 2 => set 2
a.d
```
3. property decorator
```
class A:
    def __init__(self):
        self._x = 0
    @property
    def x(self):
        return self._x
        
    @x.setter
    def x(self, a):
        self._x = a

a = A()
a.x => 0 @property는 callable하지 못하게 한다. 함수나 클래스를 변수처럼 쓰게 만드는 기법. 프레임워크에 함수 내부를 변형 못하게 함
a.x = 4
a.x => 4
```

## operator overloading
```
class B:
    def __mul__(self, a):
        return 0
        
b = B()
b * 3   => 0
```


# 220915
## method : class 내에서 function의 역할을 하는 것
```
class A:
    @classmethod
    def x(cls): # classmethod의 매개변수는 관례상 cls로 쓴다.
        cls.y = 1
    def xx(self):
        self.yy = 1
       
        
a = A()
print(A.y, a.y, a.yy)        
```
# Lazy Evaluation : 실행할 때마다 필요한 값을 메모리에 그때그때 올린다.
iterator, generator (tuple comprehension과 함수 내부에 yield를 사용하는 법 2가지가 있다)
iterator
```
a = [1,2,3,4,5]
b = iter(a)
next(b)
next(b)
list(b) => [3,4,5]
```

## iterator protocol
iterator는 iterable하고 next를 할 수 있어야 한다. 즉, \_\_iter__, \_\_next__를 무조건 만들어야 한다.
```
class A:
    def __str__(self):  # print()하면 실행되는 것
        return '1'
    def __repr__(self): # 이름을 부르면 실행되는 것
        return '2'

a = A()

print('next' in dir(A))
```
# Operator
```
from operator import add, sub, multiply, divid
add(1,2)
```
# Higher-Order function : 함수에 함수를 인자로 넣고 함수를 리턴하는 것 (map, filter, reduce)
## map : 모든 iterable에 같은 함수의 연산을 한다
``` 
b = list(map(lambda x:x+1, [1,2,3,4,5]))
next(b)

import seaborn as sns
iris = sns.load_daataset('iris')
temp = [i+1 for i in iris.sepal_length]

iris.sepal_length.map(lambda x:x+1)
```
## filter : 원하는 데이터만 걸러낸다.
```
b = filter(lambda x:x>2, [1,2,3,41])
[i for i in [1,2,3,4] if i>2]
```
## reduce
```
from functools import reduce
reduce(lambda x,y:x+y, [1,2,3,4,5])
=> 15
list(accumulate([1,2,3,4,5], lambda x,y:x+y))
=> [1,3,6,10,15]

list(map(lambda x,y:x+y, [1,2,3,4,5], [2,3,4,5,6]))
```
## 위의 3가지 함수들은 동시실행이 가능하다. gpu연산을 기대할 수 있다. reduce는 조건이 좀 붙는다.

## zip
```
list(zip((1,2,3),(4,5,6,7)))
=> [(1,4), (2,5), (3,6)]
# 짧은 거 기준으로 묶는다
# 긴거 기준으로 묶는 방법
from itertools import zip_longest
```
## enumerate
```
list(enumerate([1,2,3,4,5,6]))
=> [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6)]

for i,j in enumerate([1,2,3]):
    print(i,j)
    
=> 0 1 / 1 2 / 2 3
```

