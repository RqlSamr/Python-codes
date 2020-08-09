# Create a program with a for loop and a continue statement. 
# The program should iterate over a string of digits, 
# replace each 0 with x, and print the modified string to the screen. 

numberString =input("Enter a number: ")
for digit in numberString:
    if digit == "0":
       print("x", end="")
    continue
    print(digit, end="")