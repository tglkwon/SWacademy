from struct import pack, unpack
from Inverted_TDM import fileids, featureExtractor, featureSelection
from math import log,sqrt

path = '../Data collecting/news'
D = fileids(path)

queryVL = sqrt(sum(map(lambda row: row[1]**2, queryVector.items())))

candidates = dict()
for t, w1 in queryVector.items():
    df, pos = weightTDM[t]
    with open('weightPOST.dat', 'rb') as fp:
        i = 0
        while i < df:
            fp.seek(pos+(i*8))
            docID, w2 = unpack('if', fp.read(8))

            if docID not in candidates:
                candidates[docID] = 0.0

            candidates[docID] += w1*w2  # 내적

            i += 1



for docID, ip in candidates.items():
    candidates[docID] = ip/(queryVL*sqrt(docLength[docID]))