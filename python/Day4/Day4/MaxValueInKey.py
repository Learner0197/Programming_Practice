def keymaxval(abc):
    keylist=[]
    keycol=abc.keys()
    for i in keycol:
        keylist.append(i)
    print(keylist)
    keylist.sort()
    return keylist

print(keymaxval({7:'43',2:34,1:75,8:'jhj'}))