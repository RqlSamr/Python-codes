vals=[0,1,2]
vals.insert(0,1)
del vals[1]
suma=0
for i in vals:
    suma+=vals[i]
    
print(suma)

for i in range(1):
    print("#")
else:
    print("#")


lst=[3,1,-2]
print(lst[lst[-1]])

x=1
x=x==x

print(x)

lst=[1,2,3,4]
print(lst[-3:-2])

i=0
while i<=3:
    i+=2
    print("*")
    

lst1=[1,2,3]
lst2=[]
for v in lst1:
    lst2.insert(0,v)
print(lst2)

lst=[i for i in range(-1,2)]

print(lst)


var=1
while var < 10:
    print("#")
    var=var<<1
    
nums=[1,2,3]
vals=nums[-1:-2]
print(nums)
print(vals)

    
nums=[1,2,3]
vals=nums
del vals[1:2]
print(nums)
print(vals)

i=0
while i<=5:
    i+=1
    if i%2 ==0:
        break
    print("*")
    
    
t=[[3-i for i in range(3)] for j in range(3)]
s=0
for i in range(3):
    s+=t[i][i]
print(s)


vals=[0,1,2]
vals[0], vals[2]=vals[2], vals[0]

print(vals)

lst=[1,2,3]
for v in range(len(lst)):
    lst.insert(1, lst[v])
print(lst)

a=1
b=0
c=a&b
d=a|b
e=a^b
print(c+d+e)


var=0
while var <6:
    var+=1
    if var%2==0:
        continue
    print("#")
    
z=10
y=0
x=y<z and z>y or y>z and z<y

print(x)

lst [[0,1,2,3] for i in range(2)]
print(lst[2][0])
