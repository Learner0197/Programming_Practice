def arithexp(s):
    s=s.split()
    sum=0
    mux = s.index("*")
    div = s.index("/")
    add = s.index("+")
    sub = s.index("-")

    s[mux-1]*s[mux+1]


    return sum

print(arithexp("2 + 3 - 9 * 5 / 2"))