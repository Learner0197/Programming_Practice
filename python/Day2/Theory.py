from contextlib import nullcontext
from operator import index

a = [10,20,30,40,50]
print(a)
print(a[0])
print(a[1])
print(a[2])
print(type(a))
print(len(a))
# print(a[9])

# for i in range(0,len(a)):
#     print(a[i])
#
# for i in a:
#     print(i)
#
# for i in range(-1,(-len(a)-1), -1):
#     print(a[i])

# print(a[0:2])
#
# print(a[::-1])

b=[2,5,10,30,7,11,4,47]
# e=[]
# o=[]
# p=[]
# f=[]
# for i in b:
#     count = 0
#     if i%2==0:
#         e.append(i)
#     if i%2!=0:
#         o.append(i)
#     if i%10==0:
#         f.append(i)
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count<=2:
#         p.append(i)
# print("Even no:", e)
# print("Odd no:", o)
# print("Prime no:", p)
# print("10 factors:", f)

# b.append(64)
# print(b)
# b.pop()
# print(b)
# b.insert(3,45)
# print(b)
# b.remove(2)
# print(b)

# a=b.copy()
# print(a)
#
# # b.clear()
# print(b)
#
# c=a
# a.pop()
# print(a)
# print(b)
# print(c)
#
# print(a.count(2))
# print(a.count(100))
# print(a.index(10))
# a.append(10)
# print(a)
# print(a.index(10))                #index of 1st occurrence.
#
# x=[1,2,3]
# y=[3,4,5]
# print(x+y)
# x.extend(y)
# print(x)
#
# x.reverse()
# print(x)
#
# x.sort()
# print(x)
#
# x.sort(reverse=True)
# print(x)
#
# x.append("Hello")
# x.sort()
# print(x)

#Create a list of all odd numbers from 1 to 100
#Create a list of all prime numbers from 2 to 100
#find out all duplicate elements in the list
#Add elements of two list (both of equal size)
#Add elements of  two lists (Not same)

# o=[]
# p=[]
# for i in range(1,100,2):
#     o.append(i)
#
# for i in range(2,100):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         p.append(i)
#
# print(o)
# print(p)
#
# m=[46,26,272,82,24,64,46,90,73,13,24,64]
# d=[]
# for i in m:
#     if m.count(i) >1:
#         d.append(i)
# print(d)
#
# x=[1,2,3,4,5,6]
# y=[4,5,6,7,8,9]
# sum=[]
# for i in range(len(x)):
#     sum.append((x[i]+y[i]))
# print(sum)
#
# x=[1,2,3,4,5,6]
# y=[4,5,6,7,8,9,10,11]
# sum=[]
# for i in range(len(y)):
#     if i<=len(x)-1:
#         sum.append((x[i]+y[i]))
#     else:
#         sum.append(y[i])
# print(sum)

v=[46,26,272,82,24,64,46,90,73,13,24,64]
w=[]
# for i in v:
#     if v.count(i)>1:
#         v.remove(i)
#
# print(v)

# for i in v:
#     if i not in w:
#         w.append(i)
#     else:
#         continue
# print(w)
#
# a=[1,2,3,4]
# b=[1,2,3]
# c=[]
#
# for i in range(0,len(a)):
#     if len(a)==len(b):
#         c.append(a[i]+b[i])
#     elif i>=len(b):
#         c.append(a[i]+0)
#     else:
#         c.append

s="Hello World"
for i in range (0,len(s)):
    print(s[i])

