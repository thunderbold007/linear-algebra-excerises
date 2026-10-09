def gs(*args):
    # gs.gs([1,1,1],[1,4,8],[1,2,9],[6,7,8]) , last array is b from Ax=b where b is not 0
    args = [list(row) for row in args]   
    i = 0
    guardIndex=list(range(len(args) - 1))
    index= [0]*(len(args)-1)
    while i<len(args)-1:
        # i need to run each rows programmtically like if row ==0 then row 0 ref and everyhitng else
        rowOps(i,args,guardIndex,index)  
        i+=1
    arr = [[0 if abs(x) < 1e-12 else x for x in row] for row in args]
    print(arr)
def rowOps(i,args,guardIndex,index):
    print
    for j in range(len(args)-1):
        if i ==j:
            continue
        if index[j] ==guardIndex[j]:
            index[j]=index[j]+1
        if index[j]>=len(args)-1:
            continue
        findG(j,index,args,i)
def findG(i,rowIndex,args,refRow):
    cur= args[i]
    ref = args[refRow]
    inIndex= rowIndex[i]
    if ref[inIndex]==0 or cur[inIndex]==0:
        rowIndex[i]= rowIndex[i]+1
        return    
    toMul= float(cur[inIndex]/ref[inIndex])
    temp=[]
    for ii in range(len(cur)):
        temp.append(float(cur[ii])-(toMul)*ref[ii])
    args[i]=temp
    args[-1][i]= (float(args[-1][i]-float(toMul)*args[-1][refRow])) 
    # print(temp,f"index:{inIndex}, curI-{i}, refI:{refRow},args:{args},toMul:{toMul}")
    rowIndex[i]= rowIndex[i]+1


# [[11.0, 0, 0], [0, 1.9090909090909092, 0], [0, 0, 0.9999999999999991], [5.7619047619047645, -1.4545454545454612, 1.0]]