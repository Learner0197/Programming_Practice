from operator import index, indexOf


def analyse_text(s):
    count=0
    x,y,z = s,s,s
    s=s.split()
    for i in s:
        count+=1
    print("Word Count: ", count)
    count=0
    t=[]
    for i in s:
        if i not in t:
            t.append(i)
            count+=1
    print("Unique Word Count: ", count)
    v=['a','e','i','o','u']
    count=0
    x=x.replace('',' ').split()
    for i in x:
        if i in v:
            count+=1
    print("Vowel Count: ", count)
    sl=[]
    for i in s:
        sl.append(len(i))
    a=max(sl)
    count=0
    for j in sl:
        count+=1
        if j==max(sl):
            break
    print("Longest Word: ", s[count-1])

    count = 0
    for j in sl:
        count += 1
        if j == min(sl):
            break
    print("Shortest Word: ", s[count - 1])

    print(sl)

    com=[]
    sl2=list(set(sl))
    print(sl2)
    for i in sl2:
        com.append(sl.count(i))
    print(com)
    res=sl2[indexOf(com,max(com))]
    print(res)

    for i in s:
        if len(i)==res:
            print(i)

    return
print(analyse_text("The quickest of the brown fox jumps over the lazy dog"))

s="The quickest of the brown fox jumps over the lazy dog"
s=sorted(s.split(), key=len, reverse=True)
print("Longest word:", s[0])



