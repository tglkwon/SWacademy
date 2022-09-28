# 220927
# empirical law : 경험적 법칙
# zipf's Law : 단어의 반복도는 반복도 랭킹의 역순에 비례한다?

f = 1/k^s * 1/sigma(1/n^s)
언어 종류에 상관없이 모든 텍스트(코퍼스)는 Zipf의 법칙을 따른다
빈도의 역순 = 순위의 역순
빈도만 가지고 전처리해 필요한 데이터만 모을 수 있다.
(한국어 - 조사 - 형식형태소/의존형태소)

# Heap's Law : 한 문서 안의 각 단어의 수를 문서의 길이에 대한 함수로 나타낸 것

V(n) = K* n^beta <=>  M = k* T^b

# N-Gram : 형태소 단위들의 조합(sequence)에서 나오는 의미를 찾기 위한 분석
contiguous sequence of n items from a given sample of text or speech

다음 단어를 예측하기 위함
P(xi|xi-(n-i)...xi-1)
P(A,B) = P(B|A)*P(A) # Bayes' theorem
Bi-gram

# 220928
- Feature (Unigram -> collocation) : Zipf
- tokenizing (쌍 ->)

wordDictionary = []
Out of Voca.  신조어 문제

Branch-Entropy, Cohesion Score => Tokenizer / unsupervised
Hamming, Leveinshitien => Edit Distance

현실적으로 오탈자, 잘못쓴거, 비속어, 띄어쓰기 안한거 => 등을 해결하기 위해 쓰는게 WPM

# Entropy : H(X) : 불확실성
X -> Y : 앞, 뒤로 2가지 경우일 때, 0.5, 0.5
0.2, 0.8로 확률이 바뀌면 불확실성이 낮아졌다고 표현한다

$$
H(X) = - sigma(n,X) { P(X) * log(P(X)) }
P(X) = 0 과 1에서 0인 표준정규분포
$$

# Cohesion Score
$$
CS = sqrt(P(X1)P(X2)...)
$$

# WPM : Word Piece Model : 하나의 단어를 내부 단어들로 분리하는  단어 분리 모델
byte pair encoding : 가장 높은 빈도의 단어 쌍을 찾는 알고리즘

# 음절 <- 자음/모음 <- 초성/중성/종성
```
ord('가'), ord('나'), ord('다')
44032 45208 45796
```

# 220928
유클리디안 distance
## Rochhio distance 
X           C1
A-----------B
## 멘하탄 distance
A
-|-|-|-|-|-|-
-|-|-|-|-|-|-
-|-|-|-|-|-|-B
D = |A-B|

## Haaming distace, 리헨슈타인
[True, True, False] XOR [False, False, False]

비교하는 두 단어의 길이가 같아야하는 단점이 있다.
중간에 글자가 추가되거나 삭제되면, 나머지 글자들도 False가 뜬다.
=> 리벤슈타인 distance가 이 단점을 해결함

## Levenshtein Distance
A:aaaaaa
B:bbbb
fn(A,B)
    if len(A) == 0, then len(B)
    if len(B) == 0, then len(A)
    if A[0] == B[0] then fn(A[1:], B[1:])
    else 1 + min (추가, 삭제, 수정)

# Text Normalization
punctucation 등을 처리할 때 처리하는 순서나 방법을 고려해야 한다.

## Stopwords : 불용어, 분석, 모델링 등에는 필요하지 않는 문법적인 단어나 대상을 가르키는 말 등
생각해봐야 할 점 : 'To be or not to be.' -> 이거 다 날아감
우리말에서는 조사
장점 : 불용어를 제거하면 complexity를 줄일 수 있다. 압축된 공간으로 x들을 표현
고유어(Feature)를 줄일 수 있고, Zipf의 고빈도 불용어 들을 제거할 수 있다.
비속어 처리 등에 이용할 수 있다.

# 이제까지의 내용
비정형데이터(텍스트) 수집 - DB저장
문자경계인식 - tokenizer(segmentation) - normalize + stopwords/조사+어미+욕+단어
            Feature Extraction
        구두점 기반, 감정표현, 정규식, stem추출, lemmatization(형태소 추출)
                                Branch-Entropy, Cohesion Score, Collocation - Bigram
                                BPE(WPM-SPM)                     
빈도, 길이, 품사 등을 기준으로 => 적절히 complexity를 줄일 수 있다.
