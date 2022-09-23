from konlpy.tag import Kkma
from konlpy.utils import pprint
# kkma = Kkma()
# pprint(kkma.sentences(u'네, 안녕하세요. 반갑습니다.'))
# pprint(kkma.nouns(u'질문이나 건의사항은 깃헙 이슈 트래커에 남겨주세요.'))
# pprint(kkma.pos(u'오류보고는 실행환경, 에러메세지와함께 설명을 최대한상세히!^^'))

from konlpy.tag import Okt
pprint(Okt().pos('아버지가 방에 들어가신다.'))

from konlpy.corpus import kobill, kolaw # 의사회의록, 헌법
corpus = kolaw.open(kolaw.fileids()[0]).read()

from nltk.tokenize import sent_tokenize, word_tokenize
print(len(corpus.splitlines()), len(sent_tokenize(corpus)))

print(len(word_tokenize(corpus)))

from nltk.text import Text
t = Text(word_tokenize(corpus))
print(t.vocab().B(), t.vocab().N())

from nltk.corpus import gutenberg
emma = Text(word_tokenize(gutenberg.open(gutenberg.fileids()[0]).read()))
list(zip(t.vocab().most_common(10), emma.vocab().most_common(10)))
print(t.vocab().most_common(10))

kol = Text(Okt().pos(corpus))
list(zip(t.vocab().most_common(10), kol.vocab().most_common(10)))

print(t.vocab().B(), kol.vocab().B())


from konlpy.tag import Hannanum, Komoran
ma1 = Kkma()
ma2 = Hannanum()
ma3 = Komoran()
ma4 = Okt()

list(zip(ma1.tagset, ma2.tagset, ma3.tagset, ma4.tagset)), \
    len(ma1.tagset), len(ma2.tagset), len(ma3.tagset), len(ma4.tagset)
