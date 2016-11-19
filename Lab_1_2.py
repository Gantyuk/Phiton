def Lengt_Of_Longers_Words(text):
    intermediate_lengt = 0
    i = 0
    lengt = 0
    while i < len(text):
        if text[i] != ' ' :
         intermediate_lengt += 1
         if (i + 1 < len(text)) and (text[i+1] == ' '):
             if intermediate_lengt > lengt:
                 lengt = intermediate_lengt
        else:
            intermediate_lengt = 0
        i += 1
    return lengt
    
def Delet_Words(text):
    text += ' ' 
    intermediate_lengt = 0
    i = 0
    words = ''
    lengt = Lengt_Of_Longers_Words(text)
    while i < len(text):
        if text[i] != ' ' :
         intermediate_lengt += 1
         words += text[i]
         if (i + 1 < len(text)) and (text[i+1] == ' '):
             if intermediate_lengt == lengt:
                 text = text.replace(words,'')
                 words=''
                 
        else:
            intermediate_lengt = 0
            words=''
        i += 1
    return text
text =str(input("Text:"))
print ("Text:"+text)
print ("Text:"+Delet_Words(text))
