
# write a pair of functions converting l/100km into mpg, and vice versa.
# 1 American mile = 1609.344 metres;
# 1 American gallon = 3.785411784 litres.

def l100kmtompg(liters):    
    return ((liters/100)*(1.609344/3.785411784))

def mpgtol100km(miles):   
    return  ((miles/3.785411784)/1609)

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))