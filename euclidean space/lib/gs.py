def gs(*args):
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
    print(args,"after loop")
def varsVal(vectors):
    pass
# we have small version to do row operations now to figure out which row to perform operations and repeat the process

def rowOps(row):
    print(row)
    
    
def findG(i,inIndex,args,refRow):
    print("row operation start")
    toMul = str(args[i][inIndex]/args[refRow][inIndex])
    print(toMul,"toMul")
    temp=[]
    for ii in range(len(args[i])):
        temp.append(int(args[i][ii])-(float(toMul)*args[refRow][ii]))
    args[i]=temp
    args[-1][i]= (int(args[-1][i]-float(toMul)*args[-1][refRow])) 
    print("row operation end")