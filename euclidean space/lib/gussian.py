def guss(*args):
    args = [list(row) for row in args]   
    print(args)
    i = 0
    inIndex=0
    curretnRow=0
    refRow= 0
    while i < len(args):
        # rowOps()
        if i == len(args)-1:
            i+=1
            continue
        if i ==1:
            for j in args[i]:
                findG(i,inIndex,args,refRow)
                break 
            i+=1
        i+=1
    varsVal(args)
    print(args)

def varsVal(vectors):
    pass
    
def rowOps(row):
    print(row)

def findG(i,inIndex,args,refRow):
    toMul = str(args[i][inIndex]/args[refRow][inIndex])
    print(toMul,"toMul")
    args[i][inIndex]= (float(toMul)*args[refRow][inIndex])-int(args[i][inIndex]) 
    args[-1][i]= (float(toMul)*args[refRow][inIndex])-int(args[i][inIndex]) 
    # print(row1)

