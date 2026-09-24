import proveOrthogonal
from lib import norm
import degreeOfVector
from lib import getVarsEq
from lib import varsOps
def distance(u,plane):
    formatedEqu=getVarsEq.findVandC(plane)
    c = getC(formatedEqu)
    varsOps.varsOps(formatedEqu)
    orderedPlane =orderTheCoef(formatedEqu)
    print(orderedPlane)
    # formatedEqu[0]= orderedPlane
    v = proveOrthogonal.getCoefficient(orderedPlane)
    print(v)
    normOfV = norm.findNorm(v[0])
    print(normOfV)
    # # u.v
    vectorProduct = degreeOfVector.vectorProduct([u],v)
    shortestDis = abs((vectorProduct+c)/normOfV)
    print(shortestDis)
    return shortestDis

def getC(vars):
    i =0
    c=0
    while i < len(vars):
        try:
            if float(vars[i]):
                c=c+float(vars[i])
                vars.pop(i)
                continue
        
        except:
            i=i+1
            pass
    return c



def orderTheCoef(th):
        jj ={
           
        }
        temp1 = []
        temp2=[]
        for i in th:
            for j in i:
                if j.isdigit() or j =='-':
                    temp2.append(j)
                    continue
                if len(temp2) ==0:
                    temp2.append("1")
                if len(temp2)==1 and temp2[0]=="-":
                    temp2.append("1")
                if not j.isdigit() and len(temp2)>0:
                    if not j in temp1:
                        temp1.append(j)
                    if j in jj:
                        jj[j]=(int(jj[j])+int("".join(temp2)))
                        temp2=[]
                        continue
                    jj[j]= "".join(temp2)
                    temp2=[]
        newPlane = sorted(temp1)
        index = 0
        for i in newPlane:
            try:
                for key,val in jj.items():
                    if i ==key:
                        ii = str(val)+i
                        newPlane[index]= ii
                index=index+1
            except ValueError as e:
                index=index+1
                print(e)
        return newPlane
    


# def hasTypeChange(plane,index):
#     baseIsDigit=None
#     for i in range(index, len(plane)):
#         if plane[i] == "=" or plane[i]=="-" or plane[i]=="+":
#             return False
#         if baseIsDigit==None:
#             baseIsDigit=plane[i].isdigit()
#             continue
#         if plane[i].isdigit() != baseIsDigit:
#             return True

# def addToVars(plane,equalPresent,opsInt,intt,c,cIndex):
#             if equalPresent:
#                 if opsInt=="-":
#                     c.append(intt)
#                 else:
#                     c.append(f"-{intt}")
#             else:
#                 if opsInt=="-":
#                     c.append(f"-{intt}")
#                 else:
#                     c.append(intt)
#             intt=""
