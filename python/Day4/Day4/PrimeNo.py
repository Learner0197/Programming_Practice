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