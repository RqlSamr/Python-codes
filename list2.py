hatList = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
number=int(input("Write a number: "))

# Step 2: write a line of code here that removes the last element from the list.
hatList[2]=number
# Step 3: write a line of code here that prints the length of the existing list.
print(len(hatList))
print(hatList)

myList = [10, 1, 8, 3, 5]
total = 0

for i in range(len(myList)):
    total += myList[i]

print(total)


