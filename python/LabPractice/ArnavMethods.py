import re
def cleanText(text):
    text=text.strip()
    s=re.sub(r'@','a',text)
    s = re.sub(r' +', ' ', s)
    s=re.sub(r'[^a-zA-Z0-9]','',s)
    print(s)

cleanText(' Mumbai_!  Indian@s    11 Punj@b ')

# def cleanVowels(text):
#     text=text.strip()
#     s=re.sub(r'[a,e,i,o,u,A,E,I,O,U]','',text)
#     s=re.sub(r' +','',s)
#     print(s)
#
# cleanVowels(' Mumbai_!  Indian@s ')