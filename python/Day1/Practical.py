#Grade printing
from itertools import count

# a = int(input("Input number"))
# if a>=70:
#     print("Distinction")
# elif a<70 and a>=50:
#     print("Satisfactory")
# elif a<50 and a>=40:
#     print("Pass")
# else:
#     print("Fail")

# i = 1
# sum = 0
# while(i<=10):
#     sum = sum+i
#     i+=1
# print(sum)
#
# j=99
# while j>0:
#     print(j)
#     j=j-2
#
# k=2
# while k<=100:
#     if k<=50 and k%2==0:
#         print(k)
#         k+=2
#     else:
#         print(k-1)
#         k+=2
#
# n=5
# fact =1
# for i in range(1,n+1,1):
#     fact = fact*i
# print(fact)
#
# for i in range(1,11):
#     print(i)
#     if i==3:
#         break
#
# for i in range(1,11):
#     if i==3:
#         continue
#     print(i)
#
# n =13
# count = 0
# for i in range(1,n,1):
#     if(n%i==0):
#         count+=1
# if count>1:
#     print("Not prime")
# else:
#     print("Prime")

# n=200
# primeno=0
# count=0
# for i in range(2,n,1):
#     for j in range(1,i,1):
#         count=0
#         if(i%j==0):
#             count+=1
#             if count>1:
#                 print(i)
#             continue
        # count=0
        # if(i%j==0):
        #     count+=1
        # if count>1:
        #     print(i)
        #     primeno+=1

# n=200
# sum = 0
# for i in range(2,n+1,1):
#     count =0
#     for j in range(1, (i//2)+1, 1):
#         if i%j==0:
#             count+=1
#     if count<=1:
#         print(i)
#         sum+=1
# print(sum)

for i in range(2,201,1):
    for j in range(1, (i//2)+1, 1):
        if i==2:
            print(i)
            break
        elif i%j == 0:
            break
    else:
        print(i)