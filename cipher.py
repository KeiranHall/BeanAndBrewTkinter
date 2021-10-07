import string

def encrypt(text):
    alphabet = list(string.ascii_uppercase)
    text = text.upper()
    newText = ""
    for i in text:
        if i in alphabet:
            order = alphabet.index(i)
            if order + 6 >= 26:
                overflow = order + 6 - 26
                newText += alphabet[overflow]
            else:
                newText += alphabet[order+6]
        else:
            try:
                i = int(i)
                if i + 6 > 9:
                    overflow = i + 6 - 9
                    newText += overflow
                else:
                    newText += str(i + 6)
            except:
                newText += str(i)
            
    return newText

def decrypt(text):
    alphabet = list(string.ascii_uppercase)
    text = text.upper()
    newText = ""
    for i in text:
        if i in alphabet:
            order = alphabet.index(i)
            if order - 6 < 0:
                order = str(order-6)
                overflow = order[1:]
                newText += alphabet[26 - int(overflow)]
            else:
                newText += alphabet[order-6]
        else:
            try:
                i = int(i)
                if i - 6 < 0:
                    overflow = i - 6
                    overflow = str(overflow[1:])
                    newText += overflow
                else:
                    newText += str(i - 6)
            except:
                newText += str(i)
            
    return newText
