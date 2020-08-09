blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#	
height=0
i=1
suma=0

while i <=blocks:
    suma=suma+i
    print ("*"*i," ", suma," ", i)
    if suma>blocks:     
        height=i-1
        break
    elif suma == blocks:
        height=i
        break
    i=i+1
print("The height of the pyramid:", height)