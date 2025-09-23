def splitlst(l,n):
    l1=len(l)//n
    p=[]
    for i in range(l1):
        p.append(l[0:n])
        for i in range(n):
            l.pop(0)
    return p

print(splitlst([1,2,3,4,5,6], 3))