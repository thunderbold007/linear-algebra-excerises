import degreeOfVector
def proveOrthogonal (u,v):
   vectors = getCoefficient(u,v)
   product = degreeOfVector.vectorProduct([vectors[0]],[vectors[1]])
   if product ==0:
       return f"This is orthogonal and product is {product}"
   else:
       return f"this is not orthogonal and product is {product}"


def getCoefficient(*args):
    kk =[]
    index = 0
    temp = ""
    for i in args:
        kk.append([])
        for j in i:
            i =0
            spldStr = list(j)
            for k in spldStr:
                if k =="-" :
                    temp = temp+"-"
                    if  spldStr[1].isdigit() ==False:
                        temp=temp+"1"
                        kk[index].append(temp)
                        temp=""
                        break
                    continue
                if( not str(k).isdigit()):
                    if i==0 :
                        temp= temp+"1"
                        kk[index].append(temp)
                        temp=""
                        break
                    kk[index].append(temp)
                    temp=""
                    i=i+1
                    continue
                temp=temp+k
                i=i+1
            i=0
        index+=1
    return kk
