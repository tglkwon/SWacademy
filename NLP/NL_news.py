from os import listdir

path = '../Data collecting/news'
def fileids(path, ext='txt'):
    path = path if path[-1] == '/' else path+'/'
    fileList = list()
    for fileName in listdir(path):
        if fileName.endswith(ext):
            fileList.append(path+fileName)
    return fileList

corpus = list()
for filePath in fileids(path):
    with open(filePath, encoding='utf8') as fp:
        corpus.append(fp.read())

from nltk.tokenize import sent_tokenize
from konlpy.tag import Okt

posTagger = Okt()
textList = list()
for doc in corpus:
    sentList = list()
    for sent in sent_tokenize(doc):
        sentList.append(posTagger.pos(sent))
    textList.append(sentList)

# len(set([_[0]+'/'+_[1] for _ in textList])), sum([len(_) for _ in textList])