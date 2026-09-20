import proveOrthogonal
from lib import norm
import degreeOfVector
def distance(u,plane):
    formatedEqu=findVandC(plane)
    print(formatedEqu)
    # print(formatedEqu)
    orderedPlane =orderTheCoef(formatedEqu[0])
    print(orderedPlane)
    # formatedEqu[0]= orderedPlane
    v = proveOrthogonal.getCoefficient(formatedEqu[0])
    # c = formatedEqu[1]
    # print(c,formatedEqu)
    # normOfV = norm.findNorm(v[0])
    # # u.v
    # vectorProduct = degreeOfVector.vectorProduct([u],v)
    # shortestDis = abs((vectorProduct+c)/normOfV)
    # return shortestDis
    
def findVandC(plane):
    c = 0
    equalPresent = False
    vars = []
    j =0
    opsInt= "" 
    var=""
    for i in plane:
        if i == " ":
            j = j+1
            continue
        if (j==0 and i =="-"):
            opsInt= "-"
            j=j+1
            continue
        if i =="=" and plane[j+1]=="-":
            opsInt="-"
            equalPresent =True
            j=j+1
            continue
        if i == "=" or i == "+" or i == "-":
            j = j+1
            if len(var)>0:
                gg=push(opsInt,equalPresent,var)
                vars.append(gg)
            var=""
            if i =="=":
                equalPresent= True
            opsInt=i
            continue
        var= var+i
        if j == len(plane)-1:
            vars.append(push(opsInt,equalPresent,var))
        j=j+1
        
    c= getC(vars,c)
    return [vars,c]

def getC(vars,c):
    i =0
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

def push(ops,eq,value):
    if eq:
        if ops=="-":
            return value
        else:
            return f"-{value}"
    elif ops=="-":
        return f"{ops}{value}"
    return value




def orderTheCoef(th):
       
        jj ={
            
        }
        temp1 = []
        for i in th:
            if "-" in i:
                tempStr = i.replace("-","")
                temp1.append(tempStr)
                jj[tempStr]= "-"
            else:
                temp1.append(i)
        newPlane = sorted(temp1)
        index = 0
        for i in newPlane:
            try:
                for key,val in jj.items():
                    if i ==key:
                        i = val+i
                        newPlane[index]= i
                index=index+1
            except:
                index=index+1
                print("eror")
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
