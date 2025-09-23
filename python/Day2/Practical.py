# s="Hello World"
# for i in range (0,len(s)):
#     print(s[i])
#
# print(s[-1])
# print(s[::-1])
# print(s[0:4])
#
# s='''Hello
# How are you?
# Where are you?'''
#
# print(s)
#
# s="Hello World"
# print(s.capitalize())
# print(s.casefold())
# print(s.lower())
# print(s.index(' '))
# print(s.count("l"))
# print(s.endswith("d"))
# print(s.endswith("l"))
# print(s.startswith("H"))
# print(s.startswith("o"))
# print(s.find("World"))
# print(s.find("a"))
# # print(s.index("a"))
#
# print(s.replace("o", ""))
#
# s1="1234"
# print(s1.isnumeric())
# s1="12 34"
# print(s1.isnumeric())
# s1="abcd"
# print(s1.isalpha())
# s1="ab cd"
# print(s1.isalpha())
# s1="ab12"
# print((s1.isalnum()))
# s1="ab 12"
# print((s1.isalnum()))
# print(s1.isspace())
# s1=" "
# print(s1.isspace())
#
# s2="hello World"
#
# print(s2[0].upper()+s2[1:len(s2)])
#
# s="Python is a great language"
# l=s.split(" ")
# print(l)
#
# print(" ".join(l))
# print("#".join(l))
#
# a="hello world how are you"
# b=[]
# b=a.split(" ")
# c = ""
# print(b)
#
# for i in range(len(b)):
#     b[i] = b[i][::-1]
# print(" ".join(b))

a="heLLo woRlD hoW Are YOu"
c = " "
for i in range(len(a)):
    if a[i].isspace():
        b = a[i]
        c = c+b
        continue
    else:
        if a[i].isupper():
            b= a[i].lower()
            c=c+b
        else:
            b= a[i].upper()
            c=c+b
print(c)

d='''hello world
world is a beautiful place
we must save this world'''
d=d.split(' ')
e=[]
n=[]
print(d)
for i in d:
    if i not in e:
        if "\n" in i:
            i = i.split("\n")
            e = e+i
        else:
            e.append(i)
n = " ".join(e)
for i in e:
    print("Count of", i, n.count(i))





