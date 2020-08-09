numbers = [10, 5, 7, 2, 1]
print("List content:", numbers) # printing original list content


print("Original list content:", numbers) # printing original list content

numbers[0] = 111
print("New list content: ", numbers) # current list content
numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers) # printing original list content

numbers[0] = 111
print("\nPrevious list content:", numbers) # printing previous list content

numbers[1] = numbers[4] # copying value of the fifth element to the second
print("New list content:", numbers) # printing current list content


numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

myList = [] # creating an empty list

for i in range(5):
    myList.append(i + 1)

print(myList)

myList = [] # creating an empty list

for i in range(5):
    myList.insert(0, i + 1)

print(myList)