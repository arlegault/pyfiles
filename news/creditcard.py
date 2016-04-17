

ccnumber= raw_input('Enter your creditcard number')
start = len(ccnumber)-2
w= len(ccnumber)-1
arr =[]
arr2 =[]
z =0

for x in range(start,0, -2):
    arr.append(int(ccnumber[x])*2)
    # confirmed this worked with the follwoing print(ccnumber[x])

for x in range(0,len(arr)):
    if len(str(arr[x])) > 1:
        temp = str(arr[x])
        for y in range(0,len(str(arr[x]))):
            z = int(temp[y])+z
    else:
         z = int(arr[x])+z

while w> -1:
    arr2.append(int(ccnumber[w]))
    #confirmed this worked with the following print(ccnumber[w])
    w = w-2

for x in range(0,len(arr2)):
    if len(str(arr2[x])) > 1:
        temp = str(arr2[x])
        for y in range(0,len(str(arr2[x]))):
            z = z + int(temp[y])
    else:
        z = z+ int(arr2[x])
print(z)
tempz =str(z)
if int(tempz[len(tempz)-1]) ==0:
    print('valid')
else:
     print('shit')
