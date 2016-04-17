
balance = int(raw_input('enter balance: '))
annualInterestRate = float(raw_input('enter interest rate: '))
monthlyInterest = annualInterestRate/12.0
#optimize by looking at balance, divide by 12 and then 10 to have a better starting point
originalbalance = balance

lowerbound = balance/12.0
upperbound = (balance * (1+ monthlyInterest)**12)/12    

while abs(balance) >  0.01:
    balance = originalbalance

    payment = (upperbound - lowerbound) / 2 + lowerbound

    for x in range(12):
        print 'month:', x 
        print payment       
        balance -= payment
        balance *= 1 + monthlyInterest
        print balance

    if balance >0:
        lowerbound = payment
    elif balance < 0:
        upperbound = payment    
       # payment += 0.01
        
print round(payment,2)


