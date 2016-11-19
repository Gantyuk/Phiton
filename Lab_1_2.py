def Lengt_Of_Longers_Words(text):
    intermediate_lengt = 0
    i=0
    lengt = 0
    while i < len(text):
        if text[i] != ' ' or text[i] != ',' or text[i] != '.' or text[i] != ':' or text[i] != ';':
         intermediate_lengt += 1
         if text[i+1] != ' ' or text[i+1] != ',' or text[i+1] != '.' or text[i+1] != ':' or text[i+1] != ';':
             if intermediate_lengt > lengt:
                 lengt = intermediate_lengt
        else:
            intermediate_lengt = 0
        i += 1
    return lengt
    
