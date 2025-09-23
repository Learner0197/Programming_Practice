l=[10,20,30,32,45,67,93]
x=map(lambda a:a+10, l)
print(list(x))

x=filter(lambda a:a%10!=0, l)
print(list(x))

def myfunc(num):
    return num+10

x=map(myfunc, l)
print(list(x))

first = ["abc","sdv","ftg","tyh"]
last = ["tyh","iiu","ooy","rtt"]

m=zip(first,last)
# print(list(m))
print(tuple(m))

l=["malayalam", "chrome", "python", "madam", "level"]
# def palindrome(s):
#     if s[::1]==s[::-1]:
#         return True
#     else:
#         return False
# print(list(map(palindrome,l)))
print(list(filter(lambda s:s==s[::-1], l)))

l=[1,2,3,4,5,6,7]
def oddsqaure(b):
    if b%2!=0:
        return b*b
    else:
        return b
print(list(map(oddsqaure,l)))

print(list(map(lambda i:i**2 if i%2!=0 else i, l)))

l=["Malayalam", "chrome", "Python", "madam", "Level", "banana"]
print(list(filter(lambda s: len(s)!=len(set(s)), l)))

print(list(map(lambda s:s.swapcase() if not s.istitle() else s, l)))