import re
def cleanText(text):
    text=text.strip()
    s=re.sub(r'@','a',text)
    s=re.sub(r'[^a-zA-Z0-9 ]','',s)
    s = re.sub(r' +', ' ', s)
    print(s)

cleanText(' Mumbai_!  India@ns    11 Punja@b ')