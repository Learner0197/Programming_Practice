from Day10.userdefinedexceptions import MyException

a=0
b=234
d=0
try:
    e=b//d
    print(e)
except ZeroDivisionError:
    d=1
    e=b
except:
    print("Something went wrong")
f=[1,2,3,4,5,6]
#print(f[6])
print(f[5])

for x in range(0,len(f)+2):
    try:
        print(f[x])
    except IndexError:
        print("Index out of range")
    finally:
        print("This code will always run")

#

# a=10
# if a>1:
#     raise MyException
# else:
#     print("This shouldn't happen")

# x=-25
# if x<5:
#     raise Exception("This number is zero")


# f=open("test.txt","w")
# f.write("This is my demo file \nHello World \nFile created")
# f.close()
#
# f=open("test.txt","r")
# data = f.read()
# print(data)
# f.close()

# f=None
# try:
#     f=open("test.txt","r")
#     data = f.read()
#     print(data)
#     f.seek(0)
#     print("Printing once again...", f.read())
# except FileNotFoundError:
#     print("File not found")
# except Exception as e:
#     print("Something went wrong")
# finally:
#     if f is not None:
#         f.close()
#         print("file closed")
#     else:
#         print("no file to close")

# f1=open("test1.txt","w")
# f1.write("let's copy")
# f1.close()
#
# f1= None
# try:
#     f1=open("test1.txt","r")
#     data = f1.read()
#     target = open("test.txt","a")
#     target = target.write(data)
#     print(target)
# except FileNotFoundError:
#     print("File not found")
# except Exception as e:
#     print("Something went wrong")
# finally:
#     if f1 is not None:
#         f1.close()
#         print("file closed")
#     else:
#         print("no file to close")


#To find no. of vowels in a file:

def vowelcount(filename):
    f = open(filename,"r")
    v = ["a", "e", "i","o","u"]
    count = 0
    for i in f.read():
        if i.lower() in v:
            count += 1
    f.close()
    return count

print(vowelcount("test.txt"))

#To write the word count f one file into another file:
def wordcount(filename, newfilename):
    f = open(filename,"r")
    count = 0
    for i in f.read().split():
        print(i)
        count+=1

    n = open(newfilename,"w")
    n.write("The count of words in test file is: %d"%count)
    f.close()
    n.close()
    return count

print(wordcount("test.txt","wordcount.txt"))

##To remove all blank lines from file and result in new file:
def removeblankline(filename, newfilename):
    f = open(filename,"r")
    r = f.readlines()
    for i in r:
        if i.isspace():
            r.pop(r.index(i))
    n = open(newfilename,"w")
    n.writelines(r)
    f.close()
    n.close()
    return newfilename

print(removeblankline("test.txt","withoutblank.txt"))

#To merge data of 2 files into 1 new file:
def mergefiles(firstfile, secondfile, mergedfile):
    f = open(firstfile,"r")
    r = f.read()
    s = open(secondfile,"r")
    r1 = s.read()
    merged = open(mergedfile,"w")
    merged.write(r)
    merged.close()
    merged = open(mergedfile, "a")
    merged.write(r1)
    merged.close()
    f.close()
    s.close()
    return "Merged"

print(mergefiles("firstFile.txt","secondFile.txt","merged.txt"))

def decipher(filename, newfilename):
    f = open(filename,"r")
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
    for i in f.read():
        if i.isalpha():
            n = n + key[i]
        else:
            n = n + i
    nf = open(newfilename,"w")
    nf.write(n)
    nf.close()
    f.close()
    return "Deciphered"

f= open("encfile.txt","w")
f.write("Caesar cipher? I much prefer Caesar salad!")
f.close()

print(decipher("encfile.txt","decfile.txt"))










