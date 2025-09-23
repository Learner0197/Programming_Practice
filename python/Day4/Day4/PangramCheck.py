def pangram(n):
    count = 0
    s1 = ""
    for i in n:
        if i not in s1:
            s1 = s1 + i
    for i in s1:
        if 122 >= ord(i) >= 97:
            count += 1
    if count == 26:
        print("Pangram")
    else:
        print("Not Pangram")
pangram("The quick brown fox over the lazy dog")