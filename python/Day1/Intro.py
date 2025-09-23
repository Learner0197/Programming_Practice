print("hello world")

a = 10
print(type(a))

a=1.1
print(type(a))

a=True
print(type(a))

a,b,c,d,e=10,1.2,True,"Hello",5

print(a,b,c,d,e)

# del e
# print(e)

a,b = 10,2
print(a>b)
print(a<b)
print(a>=b)
print(a==b)
print(a!=b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

t=0
t=a
a=b
b=t
print(a,b)

a,b=b,a
print(a,b)

# print(1351245165563969**102)

c=5
a,b,c = c,b,a
print(a,b,c)

num = 498
br = 0
for i in range(0,3):
    br += num%10
    num = num//10

print(br)

# num=298
# i=0
# for num in range(i<3):
#     br += num / (10**i)

if a>b:
    print("inside if")
    print("a is greter")
else:
    print("inside else")
    print("b is greater")

if br==21:
    print("True")
else:
    print("False")

a=21
b=21
if a>b:
    print("A is greater")
elif a<b:
    print("B is greater")
else:
    print("A and B are equal")

a,b,c = 10,2,6
print(a>b and a>c)
print(a>b or a>c)
