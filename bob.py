#check for the number of times that bob occurs when given a string of variable lengths


s = 'azcbobobegghakl'

def checkBob(string):
    count = 0
    for x in range(2, len(string)-1):
        if string[x-2] + string[x-1] + string[x] == 'bob':
            count +=1
    print 'Number of times bob occurs is: ',count


checkBob(s)
