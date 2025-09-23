#Q1
from traceback import print_tb

a="heLLo woRlD hoW Are YOu"
c = " "
v=['a','e','i','o','u']
for i in range(len(a)):
    if a[i] in v:
        if a[i].isupper():
            b= a[i].lower()
            c=c+b
        else:
            b= a[i].upper()
            c=c+b
    else:
        b = a[i]
        c = c+b
        continue
print(c)

#Q2
d="aaaabbcddd"
e=[]
d=d.replace(""," ")
d=d.split()
for i in d:
    if i not in e:
        e.append(i)
        e.append(str(d.count(i)))
f = "".join(e)
print(f)

#Q3
g="silent"
h="listen"
g=g.replace('',' ')
g=g.split()
h=h.replace('',' ')
h=h.split()
# print(sorted(g))
# print(sorted(h))
g.sort()
h.sort()
print(g)
print(h)
if g==h:
    print("Anagram")
else:
    print("Not Anagram")

#Q4
i="assignment"
i=i.replace('',' ')
i=i.split()
j=[]
for a in i:
    if a not in j:
        j.append(a)
print(j)

#Q5
k="pnuemonoultramicroscopicvolcanoconiosis is a deadlier disease than conjunctivitis"
k=k.split(" ")
l=sorted(k,key=len, reverse = True)
print("max length word:", l[0])

#Q6
s="Python is a great language"
l=['a','e','i','o','u']
v=[]
for i in s:
    if i in l and i not in v:
        v.append(i)
for i in v:
    print("count of", i, s.count(i))

#Q7
s="malayalam"
if s==s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#Q8
s="Hello World! How's Life?"
for i in s:
    if not i.isspace():
            if i.isalnum():
                continue
            else:
                s= s.replace(i,"")
    else:
        continue
print(s)

#Q9
s="1atr54j89"
sum1 = 0
for i in s:
    if i.isnumeric():
        sum1 =sum1 + int(i)
print(sum1)

#Q10
s="hello world world is a beautiful place we must save this world"
n=s.split()
m=[]
x=[]
for i in n:
    if i not in m:
        m.append(i)
for j in m:
    x.append(s.count(j))
for k in n:
    if s.count(k)==max(x):
        print("Max times word:", k)