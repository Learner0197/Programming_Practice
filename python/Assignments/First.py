#Q1
a=1
b=2
a,b=b,a
print(a,b)

#Q2
num = 498
br = 0
for i in range(0,3):
    br += num%10
    num = num//10

print(br)

#Q3
a=5
if a%2==0:
    print("Even number")
else:
    print("Odd number")

#Q4
a = 56
if a>=70:
    print("Distinction")
elif 70 > a >= 50:
    print("Satisfactory")
elif 50 > a >= 40:
    print("Pass")
else:
    print("Fail")

#Q5
n=5
fact =1
for i in range(1,n+1,1):
    fact = fact*i
print(fact)

#Q6
n =13
count = 0
for i in range(1,n,1):
    if(n%i==0):
        count+=1
if count>1:
    print("Not prime")
else:
    print("Prime")

#Q7
l=[1,2,3,4,5,6]
print(l[::-1])

#Q8
l=[]
sum=0
for i in range(101):
    l.append(i)
for i in l:
    if i%2==0:
        sum+=i
print(sum)

#Q9
l=[23,52,5,6,44,53,76,88,91,23]
l1=[]
for i in l:
    if i%2!=0:
        l1.append(i)
print(l1)

#Q10
n=100
sum = 0
for i in range(2,n+1,1):
    count =0
    for j in range(1, (i//2)+1, 1):
        if i%j==0:
            count+=1
    if count<=1:
        print(i)

#Q11
lst = [1, 2, 2, 3, 4, 4, 5]
ansl = []
for item in lst:
    if item not in ansl:
        ansl.append(item)
print(ansl)

#Q12
v=["a","e","i","o","u"]
lst=["umbrella","car","brand","caravan"]
nlst=[]
for i in lst:
    count=0
    for j in i:
        if j in v:
            count+=1
    if count>1:
        nlst.append(i)
print(nlst)

#Q13
t=(1,2,3,4,5,6,7)
# def cprime(n):
#     count=0
#     for j in range(1, (n//2)+1, 1):
#         if n%j==0:
#             count+=1
#     if count<=1:
#         return n
# def odd(n):
#     if n%2!=0:
#         return n
# print(len(list(filter(cprime, t))))
# print(len(list(filter(odd, t))))
p,o=0,0
for i in t:
    count = 0
    for j in range(1, (i//2)+1, 1):
        if i%j==0:
            count+=1
    if count<=1:
        p+=1
    if i%2!=0:
        o+=1
print("Prime count:", p)
print("Odd count:", o)

#Q14
s="Python is great"
print(s[::-1])

#Q15
s = "The quick brown fox jumps over the lazy dog"
s = s.lower()
n = set(s.replace(" ", ""))
print(n)
if len(n) == 26:
    print("pangram")
else:
    print("not pangram")

#Q16
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

#Q17
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

#Q18
s="The quick brown fox jumps over the lazy dog"
s=s.split()
n=[]
for i in s:
    n.append(i[::-1])
print(" ".join(n))

#Q19
key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y',
'm':'z', 'n':'a','o':'b',
'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O',
'C':'P', 'D':'Q','E':'R',
'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E',
'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
print(key)
enc="Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
dec=""
for i in enc:
    if i.isalpha():
        dec = dec+key[i]
    else:
        dec = dec+i
print(dec)
n=''
for i in dec:
    if i.isalpha():
        n = n+key[i]
    else:
        n = n+i
print(n)
