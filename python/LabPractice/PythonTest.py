def cleanName():
    tName = input("Enter the IPL team name")
    tName = tName.strip()
    cleaned = ''
    for i in range(len(tName)):
        if tName[i].isspace() and i<len(tName)-1 and tName[i+1].isspace():
            cleaned = cleaned + tName[i]
            continue
        elif not tName[i].isalnum() and i<len(tName)-1:
            continue
        else:
            cleaned = cleaned + tName[i]

    return cleaned

print(cleanName())