def findNorm(u):
    squaringVectors=0
    for i in u:
        squaringVectors+= eval(i)*eval(i)
    normOfU=squaringVectors**0.5
    return normOfU

