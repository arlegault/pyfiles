

def calcMonth():
    balance = 4213
    annualInterestRate = .2
    monthlyPaymentRate = .04
    totalPaid = 0
    for month in range(1,13):
        payment = balance * monthlyPaymentRate
        totalPaid += payment
        unpaid = balance - payment
        interest = ((annualInterestRate/12.0) * unpaid)
        balance = unpaid + interest

        print 'Month:', month
        print 'Minimum monthly payment:', round(payment, 2)
        print ' Remaining balance:', round(balance, 2)

    print 'paid:', round(totalPaid, 2)
    print 'Remaining balance:', round(balance,2)

calcMonth()
