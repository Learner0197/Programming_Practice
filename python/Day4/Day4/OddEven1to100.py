def oddeveonetohun(n):
    l=[]
    if n=="odd":
        for i in range(1,101,2):
            l.append(i)
    if n=="even":
        for i in range(2,101,2):
            l.append(i)
    return l
print (oddeveonetohun("odd"))

print (oddeveonetohun("even"))