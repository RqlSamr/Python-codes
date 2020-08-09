# NEW FUNTION
def isItATriangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

print(isItATriangle(1, 1, 1))
print(isItATriangle(1, 1, 3))
# NEW FUNTION
def isItATriangle(a, b, c):
    if a + b <= c or b + c <= a or \
    c + a <= b:
        return False
    return True

print(isItATriangle(1, 1, 1))
print(isItATriangle(1, 1, 3))
# NEW FUNTION
def isItATriangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

print(isItATriangle(1, 1, 1))
print(isItATriangle(1, 1, 3))

# NEW FUNTION
def isItATriangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

a = float(input("Enter the first side's length: "))
b = float(input("Enter the second side's length: "))
c = float(input("Enter the third side's length: "))

if isItATriangle(a, b, c):
    print("Congratulations - it can be a triangle.")
else:
    print("Sorry, it won't be a triangle.")