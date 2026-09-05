def findUnitVector(u):
    normOfU =None
    squaringVectors=0
    unitVectors = []
    for i in u:
        squaringVectors+= i*i
    normOfU=squaringVectors**0.5
    for i in u:
        unitVectors.append((1/normOfU )* i)
    return unitVectors
    # extra , check check check to see if length of u is 1 or not\