def prime1to100():
    p=[]
    for i in range(2,101):
        if isprime(i):
            p.append(i)
        else:
            continue
    return p
print(prime1to100())