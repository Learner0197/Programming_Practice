l=[ i for i in range(1,11)]
print(l)
l={ i for i in range(1,11)}
print(l)

l=[ i for i in range(1,11) if i%2!=0]
print(l)

def oddeve(n):
    if n%2==0:
        return True
    else:
        return False

l=[ i for i in range(1,11) if oddeve(i)==True]
print(l)

#Comprehensions
#1.Create a list of all from 1 to 10
#2. Create a list of all even numbers from 1 to 100
#3. Create a list of all even numbers from 1 to 50 and odd numbers from 51 to 100
#4. Create a list of all factorials from 1 to 10
#Create a list of all prime numbers from 2 to 100

l=[ i for i in range(1,11)]
print(l)
l=[ i for i in range(1,101) if i%2==0]
print(l)

def evethenodd(a):
    if a%2==0 and a<51:
        return True
    if a%2!=0 and a>50 and a<100:
        return True
    return None


g=[i for i in range(0,100) if evethenodd(i)]
print(g)

def fact(q):
    facto=1
    for j in range(1,q+1):
        facto=facto*j
    return facto

h=[fact(i) for i in range (1,11)]
print(h)

def isprime(d):
    count=0
    for i in range(2,d+1):
        if d%i==0:
            count+=1
        else:
            continue
    if count<2:
        return True
    else:
        return False

w=[t for t in(0,100) if isprime(t)]
print(w)

#Generator
l=( i for i in range(1,11))
for j in l:
    print(next(l))
l=(i for i in range(1,101) if i%2==0)
for j in l:
    print(next(l))

def evethenodd(a):
    if a%2==0 and a<51:
        return True
    if a%2!=0 and a>50 and a<100:
        return True
    return None


g=(i for i in range(0,100) if evethenodd(i))
for j in g:
    if j < 10:
        print(next(g))
    else:
        break

def fact(q):
    facto=1
    for j in range(1,q+1):
        facto=facto*j
    return facto

h=(fact(i) for i in range (1,11))
for j in h:
    if j<10:
        print(next(h))
    else:
        break

def isprime(d):
    count=0
    for i in range(2,d+1):
        if d%i==0:
            count+=1
        else:
            continue
    if count<2:
        return True
    else:
        return False

w=(t for t in range(2,101) if isprime(t))
for j in w:
    if j < 97:
        print(next(w))
    else:
        break

#ComprehensionTypes:

l=[a for a in range(0,11)]
print(type(l))
s={a for a in range(0,11)}
print(type(s))
d={a:a*a for a in range(0,11)}
print(type(d))
c=(a for a in range(0,11))
print(type(c))

#Given a list of strings, extract only those words in which there are 2 or more vowels using comprehension.
l=["Python", "is", "great", "language", "and", "Arnav", "is", "sleepy"]
def vovcount(s):
    count=0
    l=["a", "e", "i", "o", "u"]
    for i in s:
        if i.lower() in l:
            count+=1
    if count >= 2:
        return s
    # else:
    #     return
v=(vovcount(i) for i in l if vovcount(i) is not None)
for i in v:
    print(i)


#from a given list fo names, create a list which stores only the names starting with a and in upper case.
l=["Aman", "Arnav", "Ishan", "Pankaj", "Rahul"]
def nameSelect(s):
    if s[0].lower()=="a":
        return s.upper()
ln=[nameSelect(i) for i in l if nameSelect(i) is not None]
print(ln)

#create a dictionary with all the keys from 1 to 10 and value has to be even or odd
def values(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
d={i:values(i) for i in range(1,11)}
print(d)

#Create dictionary using the following two lists (use map, zip and comprehension)
names=["abc", "mno", "pqr", "xyz"]
marks=[90, 55,78,66]

z=list(zip(names, marks))
def dict(i):
    key=i[0]
    value=i[1]
    d={key:value}
    return d

m = map(dict(i), z)
