
#Key to determine how each individual letter will be changed depending on user input
letter_key = ['A','B','C','D','E','F','G','H','I',
              'J','K','L','M','N','O','P','Q','R',
              'S','T','U','V','W','X','Y','Z','a',
              'b','c','d','e','f','g','h','i','j',
              'k','l','m','n','o','p','q','r','s',
              't','u','v','w','x','y','z']

#key to determine how each number or symbol will be changed
number_key = {'0':'!','1':'@','2':'#','3':'$','4':'%',
              '5':'^','6':'&','7':'*','8':'(','9':')',
              '!':'0','@':'1','#':'2','$':'3','%':'4',
              '^':'5','&':'6','*':'7','(':'8',')':'9'}

def encrypt(content : list[str],shift : int) -> list[str]:
    '''
    Changes each character to a different one to create an unreadable document
    :param content: The data to be changed
    :param shift: The amount the data will be changed
    :return: The product created by shifting all characters
    '''
    newlist = []
    shift = shift % 52
    for x in content:
        newstring = []
        for n in x:
            if n.isalpha():
                place = letter_key.index(n)
                if place + shift > 51:
                    n = letter_key[place + shift - 52]
                    newstring.append(n)
                elif place + shift < -51:
                    n = letter_key[place + shift + 52]
                    newstring.append(n)
                else:
                    n = letter_key[place + shift]
                    newstring.append(n)
            elif n in number_key:
                swap = number_key.get(n)
                n = swap
                newstring.append(n)
            else:
                newstring.append(n)
        newlist.append(''.join(newstring))
    return newlist

def decrypt(content : list[str],shift : int) -> list[str]:
    '''
    Takes in unreadable data previously encrypted and changes each character back to its original
    value, as long as the same value is given for "shift" as was given when it was encrypted
    :param content: The unreadable data
    :param shift: Used to decided how much to change the characters to make the data readable as before
    :return: The decrypted data
    '''
    newlist = []
    shift = shift % 52
    for x in content:
        newstring = []
        for n in x:
            if n.isalpha():
                place = letter_key.index(n)
                if place - shift > 51:
                    n = letter_key[place - shift - 52]
                    newstring.append(n)
                elif place - shift < -51:
                    n = letter_key[place - shift + 52]
                    newstring.append(n)
                else:
                    n = letter_key[place - shift]
                    newstring.append(n)
            elif n in number_key:
                swap = number_key.get(n)
                n = swap
                newstring.append(n)
            else:
                newstring.append(n)
        newlist.append(''.join(newstring))
    return newlist


def main():
    #This was used for testing
    content = ['^%$ Modernization Act which exempted credit default swaps perhaps the key financial mechan']
    product = encrypt(content, 198)
    print(content)
    print(product)

if __name__=='__main__':
    main()