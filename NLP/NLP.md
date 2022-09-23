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