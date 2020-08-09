n = 3

while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)
    
n = range(4)

for num in n:
    print(num - 1)
else:
    print(num)


for i in range(0, 6, 3):
    print(i)
    
x = 4
y = 1

a = x & y
b = x | y
c = ~x
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)