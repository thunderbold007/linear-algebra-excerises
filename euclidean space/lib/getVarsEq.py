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
        
    return vars
def push(ops,eq,value):
    if eq:
        if ops=="-":
            return value
        else:
            return f"-{value}"
    elif ops=="-":
        return f"{ops}{value}"
    return value
