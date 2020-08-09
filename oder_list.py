myList = [10, 1, 8, 3, 5]

myList[0], myList[4] = myList[4], myList[0]
myList[1], myList[3] = myList[3], myList[1]

print(myList)
myList = [10, 1, 8, 3, 5]
length = len(myList)

for i in range(length // 2):
    myList[i], myList[length - i - 1] = myList[length - i - 1], myList[i]

print(myList)

# we've assigned the length variable with the current list's length (this makes our code a bit clearer and shorter)
# we've launched the for loop to run through its body length // 2 times (this works well for lists with both even and odd lengths, 
# because when the list contains an odd number of elements, the middle one remains untouched)
# we've swapped the ith element (from the beginning of the list) with the one with an index equal to (length - i - 1) 
# (from the end of the list); in our example, for i equal to 0 the (l - i - 1) gives 4; 
# for i equal to 1, it gives 3 - this is exactly what we needed.