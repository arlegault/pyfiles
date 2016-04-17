import itertools

alpha = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y' , 'z']
newphrase = []
newkey = []
longkey = []
newcode = []

def get_keyword():
    k = raw_input('input keyword')
    if k == "":
        get_keyword()
    else:
        return k.strip()


def get_phrase():
    p = raw_input('input phrase to encrypt')
    if p == "":
        get_phrase()
    else:
        return p

def encrypt():
    phrase = get_phrase()
#translate phrase to alphabet number
    for i in range(0, len(phrase)):
        if phrase[i].isalpha():
            for x in range(0, len(alpha)):
                if phrase[i] == alpha[x]:
                    newphrase.append(int(x))
        else:
            newphrase.append(phrase[i])
            print 'skipping spec char in phrase'
#translate keyword to alpabet number
    keyword = get_keyword()
    for y in range(0, len(keyword)):
        if keyword[y].isalpha():
            for z in range(0, len(alpha)):
                if keyword[y] == alpha[z]:
                    newkey.append(int(z))
        else:
            print 'skipping special char in keyword'
#making keyword long enough to translate phrase
        lendiff = len(phrase)-len(keyword)
        multiplier = len(phrase)/lendiff
        if multiplier > 1:
            longkey = newkey * multiplier

#add keyword and phrase values together to encrypt
    for a in range(0, len(newphrase)):
        if type(newphrase[a]) is int:
                newcode.append(alpha[((newphrase[a]+ longkey[a])%26)]) # why is this coming back out of range
        else:
            newcode.append(newphrase[a])
            print 'skipping non int'

#    for b in range(0, len(newphrase)):
#        if isinstance(newphrase[a], int) and newphrase[a] != ' ':
#            print newphrase[b]
#            newphrase[b] = alpha[newphrase[b]]

    print "".join(newcode)

encrypt()
