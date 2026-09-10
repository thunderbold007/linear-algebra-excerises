import math

# u times v
def vectorProduct(u,v):
    print(u,v)
    # multiple first array current i by another array current i
    if  len(u[0]) != len(v[0]) or len(u)!=len(v) :
        print("not valid")
        return 
    # u times v 
    j= []
    productVectors =0
    for i in range(len(u[0])):
        k = eval(u[0][i]) *eval( v[0][i])
        j.append(k)
    for i in j:
        productVectors+= i
    return productVectors  
        
# vectorProduct(u,v)

def calculateNorm (vector):
    sqaured =0
    for i in vector:
        sqaured+= i * i
    return sqaured **0.5


def findAngle(*args):
    ProductVectors = vectorProduct(args[0],args[1])
    vectorTimesVectors = 1

    for i in args:
        vectorTimesVectors*=calculateNorm(i[0])
    angleRadian=  math.acos(ProductVectors/vectorTimesVectors)
    # A radian is a unit used to measure an angle.
    return math.degrees(angleRadian)

