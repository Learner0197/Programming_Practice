def minmaxsum(a,b):
    ans=0
    for i in range (a,b+1):
        ans=ans+i
    return ans
print(minmaxsum(23,64))