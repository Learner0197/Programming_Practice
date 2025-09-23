def delduplicate(s):
    s=s.replace(""," ").split()
    news=[]
    for i in s:
        if i not in news:
            news.append(i)
    return news

print(delduplicate("Hello World"))