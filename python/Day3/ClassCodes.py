d = {}
print(type(d))

d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print(d)
print(d["c"])

x = d.copy()
print(x)

x.clear()
print(x)

x = dict()
print(type(d))

for i in d.items():
    print(i)

for i in d.keys():
    print(i)

for i in d.values():
    print(i)
e = {"empid": 1, "ename": "abc", "salary": 90000}
print(e)

print(e.get("empid"))

x = d.copy()

x.pop("a")
print(x)

print(x.popitem())
print(x)

k = [10, 20, 40]
p = {}
p.fromkeys(k)
p = p.fromkeys(k)
print(p)
p[10] = "Hello"
print(p)
print(p[10])

p = p.fromkeys(k, "HEllo")
print(p)

a = {7: "a", 9: "g", 2: "trr", 42: "rt"}
d = a.copy()
print("rt" in d)

print(d.setdefault(7))
print(d.setdefault(42, "gf"))

h = " hello world world is a beautiful place we must save this world"
h = h.split()
j = {}
print(h)
for i in h:
    if i not in j:
        j.setdefault(i, h.count(i))
print(j)

t = (764, 35, 75, 25, 75)
print(t)
print(t.count(75))
print(t.index(35))
for i in t:
    print(i)
print(t)

a = [42, 56, 47, 36, 26]
b = [53, 36, 32, 7, 34]
c = {}
for i in a:
    for j in b:
        c.setdefault(i, j)

print(c)

count = 0
for i in c:
    count += 1
print(count)

v = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
x = {}
w = "pneumonoultramicroscopicvolcanoconiosis"
for i in w:
    if i in v:
        x.setdefault(i, w.count(i))
print(x)

comp = {"abc": 49000, "def": 75000, "ghi": 35990}
for i in comp:
    if comp[i] < 50000:
        comp[i] = comp[i] * 1.10

print(comp)

t = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
d = {}
for i in t:
    d.setdefault(i[0], i[1])
print(d)

d1 = {}
for i in reversed(d):
    d1.setdefault(i, d[i])
print(d1)

#SETS:
s = {1, 2, 3, 4, 4, 3, 5, 6}
print(s)

s.add(8)
print(s)

s.remove(8)
print(s)

print(s.pop())
l = [1, 2, 3, 4, 5, 6, 6, 5, 4, 3]
print(l)
s = set(l)
print(s)
l = list(s)
print(l)
m = {3, 4, 5, 6, 7, 8}
print(m.difference(l))
m.difference_update(l)
print(m)

#Check if a given string is Pangram
#Using sets:
s = "The quick brown fox jumps over the lazy dog"
s = s.lower()
n = set(s.replace(" ", ""))
print(n)
if len(n) == 26:
    print("pangram")
else:
    print("not pangram")

#Without using sets:
count = 0
s1=""
for i in n:
    if i not in s1:
        s1=s1+i
print(s1)
for i in s1:
    if 122>=ord(i)>=97:
        count+=1
print(count)
if count == 26:
    print("Pangram")
else:
    print("Not Pangram")

#key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y','m':'z','n':'a','o':'b','p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O','C':'P', 'D':'Q','E':'R','F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E','S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
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

#Q
l=["abc", "mno", "aaa", "pqr", "mnop"]
d={}
for i in l:
    v=[]
    a=i[0]
    print(a)
    for j in l:
        if j.startswith(a):
            v.append(j)
    d.setdefault(a,v)
print(d)

#Q
d={1:'A', 3:'B', 5:'C', 6:'A', 7:'B'}
d1={}
s=set(d.values())
for j in s:
    n=[]
    for k in d:
        if d[k] == j:
            n.append(k)
    d1.setdefault(j,n)
print(d1)
