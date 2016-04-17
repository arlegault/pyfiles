def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    radiationTotal = 0
    counter = start
   # for x in range(start, stop, step):
    while counter  != stop:
        print counter, radiationTotal
        radiationTotal += f(counter)
        counter += step
       
    print radiationTotal


radiationExposure(0,5,1)
radiationExposure(5,11,1)
radiationExposure(0,11,1)
radiationExposure(40,100,1.5)
