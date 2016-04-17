p = raw_input('enter number to be encoded').lower()
c = []
temp = []
k = 13
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for x in range(0,len(p)-1):
    letter = p[x]
    for y in range(0,len(alpha)-1):
        if alpha[y] == letter:
            print y
            print letter
            p[x] = (y+k)%26

print p

#for x in range(0,len(temp)-1):
#    c.append(alpha[temp[x]])

#print ' '.join(c)

#this works but doesnt spit it back out with the correct spacing
