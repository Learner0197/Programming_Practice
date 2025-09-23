from math import factorial


def hello():
    print("My first python function")
    print("Hello World")
    return

hello()

n=4
print(factorial(n))

def add(x,y):
    return x+y
print(add(7,8))

#Create a function to show if a number is even or odd
#Create a function to calculate the factorial of a number
#Create a function to add 0 to n values
#Create a functon to validate a given number is prime or not

def oddeve(a):
    if a%2==0:
        print("Even number")
    else:
        print("Odd number")
    return

oddeve(5)
oddeve(6)

def fac(b):
    ans=1
    for i in range (1,b+1):
        ans=ans*i
    return ans

print(fac(7))

def sum(c):
    s=0
    for i in range (0,c+1):
        s=s+i
    return s

print(sum(9))

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
isprime(9)

def add(x=0,y=0):
    return x+y
print(add(y=83))

def listsum(l):
    ls=0
    for i in l:
        ls=ls+i
    return ls

print(listsum([64,5,35,75]))

def rot13dec(msg):
    key = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x',
           'l': 'y',
           'm': 'z', 'n': 'a', 'o': 'b',
           'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm',
           'A': 'N', 'B': 'O',
           'C': 'P', 'D': 'Q', 'E': 'R',
           'F': 'S', 'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A', 'O': 'B', 'P': 'C',
           'Q': 'D', 'R': 'E',
           'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}
    dec = ""
    for i in msg:
        if i.isalpha():
            dec = dec + key[i]
        else:
            dec = dec + i
    print(dec)
    return

def rot13enc(msg):
    key = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x',
           'l': 'y',
           'm': 'z', 'n': 'a', 'o': 'b',
           'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm',
           'A': 'N', 'B': 'O',
           'C': 'P', 'D': 'Q', 'E': 'R',
           'F': 'S', 'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A', 'O': 'B', 'P': 'C',
           'Q': 'D', 'R': 'E',
           'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}
    n = ''
    for i in msg:
        if i.isalpha():
            n = n + key[i]
        else:
            n = n + i
    print(n)
    return

rot13dec("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!")
rot13enc("Caesar cipher? I much prefer Caesar salad!")

#Create a list of all numbers from 1 to 10
#Create a list of all odd or even numbers from 1 to 100 based on parameter(even or odd)
#Create a function which takes two parameters min to max and return sum of the range
#Create a function to get a list of all prime numbers till 100(make use of function above to check whether number is
#prime or not)

def onetohun():
    l=[]
    for i in range (1,101):
        l.append(i)
    return l
print(onetohun())

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

def minmaxsum(a,b):
    ans=0
    for i in range (a,b+1):
        ans=ans+i
    return ans
print(minmaxsum(23,64))

def prime1to100():
    p=[]
    for i in range(2,101):
        if isprime(i):
            p.append(i)
        else:
            continue
    return p
print(prime1to100())

def add(*a):
    ans=0
    for i in a:
        ans=ans+i
    return ans
print(add(1,5,3,22,5))

def delduplicate(s):
    s=s.replace(""," ").split()
    news=[]
    for i in s:
        if i not in news:
            news.append(i)
    return news

print(delduplicate("Hello World"))

# def clistn(ln,n):
#     tup=()
#     sub=[]
#     l=len(ln)//n
#     count=0
#     for i in range(0,l+1):
#         for j in range(0,n+1):
#             sub.append(ln[count])
#         print(sub)
#         count += 1
#     return
# clistn([5,2,53,8,97,46],2)

def keymaxval(abc):
    keylist=[]
    keycol=abc.keys()
    for i in keycol:
        keylist.append(i)
    print(keylist)
    keylist.sort()
    return keylist

print(keymaxval({7:'43',2:34,1:75,8:'jhj'}))

def leapyear(year):
    year=str(year)
    year=year.replace('',' ').split()
    print(year)


leapyear(2024)

def splitlst(l,n):
    l1=len(l)//n
    p=[]
    for i in range(l1):
        p.append(l[0:n])
        for i in range(n):
            l.pop(0)
    return p

print(splitlst([1,2,3,4,5,6], 3))


def arithexp(s):
    s=s.split()
    sum=0
    mux = s.index("*")
    div = s.index("/")
    add = s.index("+")
    sub = s.index("-")

    s[mux-1]*s[mux+1]


    return sum

print(arithexp("2 + 3 - 9 * 5 / 2"))












def pangram(n):
    count = 0
    s1 = ""
    for i in n:
        if i not in s1:
            s1 = s1 + i
    for i in s1:
        if 122 >= ord(i) >= 97:
            count += 1
    if count == 26:
        print("Pangram")
    else:
        print("Not Pangram")
pangram("The quick brown fox over the lazy dog")




