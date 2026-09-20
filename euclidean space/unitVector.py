from lib import norm
def findUnitVector(u):
    unitVectors = []
    normOfU = norm.findNorm(u)
    print(normOfU)
    for i in u:
        unitVectors.append((1/normOfU )* i)
    print(unitVectors)
    return unitVectors
    # extra , check check check to see if length of u is 1 or not