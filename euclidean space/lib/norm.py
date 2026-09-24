def findNorm(u):
    squaringVectors=0
    for i in u:
        squaringVectors+= float(i)*float(i)
    normOfU=squaringVectors**0.5
    return normOfU

