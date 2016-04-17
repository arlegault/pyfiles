total = []
def checklarge():
    findlarge(999,100)
    return max(total)

def ispal(number):
    return str(number) == str(number)[::-1] #wtf does this -1 do

def findlarge(high, low):
    for x in range(high,low, -1):
        for y in range(high, low, -1): #why do these minus ones have to be here?
            if ispal(x*y):
                total.append(x*y)

print checklarge()
