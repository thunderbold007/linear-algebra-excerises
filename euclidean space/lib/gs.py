def gs(*args):
    args = [list(row) for row in args]   
    print(args)
    i = 0
    inIndex=0
    timing=[]
    refRow= 0
    stop=True
    # counter = args/2
    rowOps(args,timing)
    # while stop:
    #     # rowOps(args,timing)
    #     if i == len(args)-1:
    #         i+=1
    #         continue
    #     if i ==1:
    #         for j in args[i]:
    #             findG(i,inIndex,args,refRow)
    #             break 
    #         i+=1
    #     if i ==12:
    #         print("need correction!")
    #         stop=False
    #     i+=1
# def varsVal(vectors):
#     print(vectors)
#     pass
# we have small version to do row operations now to figure out which row to perform operations and repeat the process
def rowOps(vecs,timing):
    jj =[]
    total =[]
    for i in range(len(vecs)-1):
        if i == len(vecs)-1:
            continue
        # how to find which will be refRow and  current row
        for j in range(len(vecs[i])):
            if j ==0:
                jj.append([])
                total.append(0)
            if vecs[i][j]==0:
                jj[i].append([i,0])
                total[i] += 0
            else:
                jj[i].append([i,1])
                total[i] += 1

    # cur=None
    # ref=None
    # zeroIndex=None
    # print(jj)
    # for i in range(len(jj)):
    #     if total[i]==len(jj):
    #         continue
    #     for j in range(len(jj[i])):
    #         if jj[i][j][1]==0:
    #             zeroIndex= j
    #             for k in range(len(jj[i])):
    #                 if k ==j:
    #                     continue
                    
    #             print(zeroIndex)
                    
    return jj
def findG(i,inIndex,args,refRow):
    # print("row operation start")
    toMul = str(args[i][inIndex]/args[refRow][inIndex])
    # print(toMul,"toMul")
    temp=[]
    for ii in range(len(args[i])):
        temp.append(int(args[i][ii])-(float(toMul)*args[refRow][ii]))
    args[i]=temp
    # args[-1][i]= (int(args[-1][i]-float(toMul)*args[-1][refRow])) 
    # print("row operation end")