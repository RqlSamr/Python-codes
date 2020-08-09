# Scenario
# Imagine a list - not very long, not very complicated, just a simple list containing some integer numbers. 
# Some of these numbers may be repeated, and this is the clue. We don't want any repetitions. We want them to be removed.
# Your task is to write a program which removes all the number repetitions from the list. 
# The goal is to have a list in which all the numbers appear not more than once.

myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
temporary=[]
#
# put your code here
#
count=0
for i in myList:
    if i not in temporary:
        temporary.append(i)    
print("The list with unique elements only:")
print(myList)
print(temporary)

