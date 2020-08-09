#3.1.6.7 Lists - more details


myList = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = myList[0]

for i in range(1, len(myList)):
    if myList[i]>largest:
        largest=myList[i]

print(largest)

#Other way    
largest = myList[0]

for i in myList:
    if i > largest:
        largest = i

print(largest)

#If you need to save computer power, you can use a slice:
myList = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = myList[0]

for i in myList[1:]:
    if i > largest:
        largest = i

print(largest)