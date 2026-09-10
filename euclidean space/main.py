import math
import numbers
import degreeOfVector
import unitVector
import proveOrthogonal
# excercise 2.2
# 1. let u and v be vetcors in R^2 . determina the angle between u and v
# u = (1 1) , v = (0 1)
#  u^ = cos^-1  u*v / ||u||*||v||
u = [[-2,3]]
v = [[1/2,-1/2]]
# print(degreeOfVector.findAngle(u,v))

#  2. determine the angle between R^3 vectors

u1 = [[-1,1,3]]
v1 = [[3,-1,5]]

# print(degreeOfVector.findAngle(u1,v1))

#3. find angle in R^4 

u2 = [[math.pi,math.sqrt(2),0,1]]
v2 = [[1/math.pi,math.sqrt(2),-1,1]]

# print(degreeOfVector.findAngle(u2,v2))

# 4. determina the values of k so that u^ = (1/math.sqrt(2) 1/2  k) is vector unit
# to find a vector unit , formula is cos(theta) = 1/||u|| *u

def findK(*args):
    unitLength = 1
    h =[]
    variable = None
    # formula is ||u^|| =1 , so ||u^|| means we need to (x^2+y^2 + z^2 ) under root = 1
    for i in args:
        if not isinstance(i,numbers.Number):
            variable = i
            continue
        h.append(i*i)
    # Now we have squared number of equation, next we need to square both sides to get rid of root of left sides to both sides to find value of varaible, we can just assume that we sqaured both sides because 1 square will be 1 and left side after squaring will be same as previoud loop results, we dont need to take account of negative numbers because after squaring negative numbers becomes postive

    # since on left side , all will be postive and right side will be 1
    # so subsituing everything on right side by positive 1 will be:
    subsByOne=0
    for i in h:
        subsByOne+= i
    m = unitLength-(subsByOne)
    return math.sqrt(m)

# valueOfK=findK(1/math.sqrt(2),1/2,'k')
# print(valueOfK)

# 5. Determine the unit vector for the following vectors
# u^ = 1/||u|| *u

u3 = [1,2,3]
u4 = [-math.pi/5, math.pi,-math.pi,math.pi/10,0]

# unitVector.findUnitVector(u4)

# We need to prove that u = (a b) and v = (-b a) are orthogonal 

# 8. prove u and v are orthogonal 
u5 = ['a','b']
v5 = ['-b','a']

orthogonal =proveOrthogonal.proveOrthogonal(u5,v5)
print(orthogonal)