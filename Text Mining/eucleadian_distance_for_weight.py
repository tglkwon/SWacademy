from struct import pack, unpack
from Inverted_TDM import fileids, featureExtractor, featureSelection
from math import log, sqrt
from konlpy.tag import Komoran

ma = Komoran()

path = '../Data collecting/news'
D = fileids(path)

fp = open('globalPOST.dat', 'wb')
fp.close()

globalTDM = dict()
for i, file in enumerate(D):
    # 단어 : 빈도
    localTDM = featureSelection(featureExtractor(file))

    with open('globalPOST.dat', 'ab') as fp:
        for k, v in localTDM.items():
            if k in globalTDM:
                pos = globalTDM[k]
                postData = (i, v, pos)
                newpos = fp.tell()
                fp.write(pack('iii', *postData))
                globalTDM[k] = newpos
            else:
                postData = (i, v, -1)
                pos = fp.tell()
                fp.write(pack('iii', *postData))
                globalTDM[k] = pos
len(globalTDM)

fp = open('globalPOST.dat', 'wb')
fp.close()

globalCollection = dict()
for i, file in enumerate(D):
    localTDM = featureSelection(featureExtractor(file))
    globalCollection[i] = max(localTDM.values())

    with open('globalPOST.dat', 'ab') as fp:
        for k, v in localTDM.items():
            if k in globalTDM:
                pos = globalTDM[k]
                postData = (i, v, pos)
                newpos = fp.tell()
                fp.write(pack('iii', *postData))
                globalTDM[k] = newpos
            else:
                postData = (i, v, -1)
                pos = fp.tell()
                fp.write(pack('iii', *postData))
                globalTDM[k] = pos

