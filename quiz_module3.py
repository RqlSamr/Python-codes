i=2
while i>=0:
    print("*")
    i=-2
    
for i in range(-1,1):
    print("#")
    
z=10
y=0
x=z>y or z==y
print(x)

lst=[3,1,-1]
lst[-1]=lst[-2]
print(lst)

vals=[0,1,2]
vals[0],vals[1]=vals[1], vals[2]

print(vals)

nums=[]
vals=nums[:]
vals.append(1)

print(vals)
print(nums)

l=[0 for i in range(1,3)]

print(l)

lst=[0,1,2,3]
x=1
for elem in lst:
    x*=elem
print(x)