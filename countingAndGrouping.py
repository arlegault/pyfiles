def newfunction(something):

def item_order(order):
    salad = 0
    hamburger = 0
    water = 0
    array = []
    orderitems = []

    for index, letter in enumerate(order):
        if letter != ' ':
            array.append(letter)
        else:
           orderitems.append(''.join(array))
           array = []
     
    for i in orderitems:
        if i == 'salad':
            salad += 1
        elif i == 'hamburger':
            hamburger += 1
        elif i == 'water':
            water+= 1
    print 'waters:', water, 'salads:', salad, 'hamburgers:', hamburger

item_order(raw_input('what would you like to order? '))
