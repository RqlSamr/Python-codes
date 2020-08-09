# Copying the whole list
list1 = [1]
list2 = list1[:]
list1[0] = 2
print(list2)

# Copying part of the list
myList = [10, 8, 6, 4, 2]
newList = myList[1:3]
print(newList)

myList = [10, 8, 6, 4, 2]
newList = myList[1:-1]
print(newList)

#Slices - negative indices
myList = [10, 8, 6, 4, 2]
newList = myList[-1:1]
print(newList)

myList = [10, 8, 6, 4, 2]
newList = myList[:3]
print(newList)

myList = [10, 8, 6, 4, 2]
newList = myList[3:]
print(newList)

#As we've said before, omitting both start and end makes a copy of the whole list:
myList = [10, 8, 6, 4, 2]
newList = myList[:]
print(newList)

#delete more than just a list's element at once - it can delete slices too:
myList = [10, 8, 6, 4, 2]
del myList[1:3]
print(myList)

#Deleting all the elements at once
myList = [10, 8, 6, 4, 2]
del myList[:]
print(myList)

#The in and not in operators
myList = [0, 3, 12, 8, 2]

print(5 in myList)
print(5 not in myList)
print(12 in myList)