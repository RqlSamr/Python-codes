print("Hissssssssssssssssssss...")
print("Hello, Python!")
print("Raquel Marisol Sánchez Mejía")
print(); print("YO")

print("The itsy bitsy spider\nclimbed up the waterspout.")
print()
print("Down came the rain\nand washed the spider out.")


print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

print("My", "name", "is", "Python", sep="--") ##separa cada argumentocon dos guiones, sep es una palabra reservada
print("My name is Python,", end=" ") ## end es una palabra reservada, en este caso separa las dos oraciones con un espacio
print("Monty Python.")##ignora el saldo de línea entre los dos print

print("Programming","Essentials","in", sep="***", end="...")
print("Python")

print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

print("     *\n","   * *\n","  *   *\n", " *     *\n", "***   ***\n","  *   *\n","  *   *\n","  *****")
#################################################################
kilometers = 12.25
miles = 7.38

miles_to_kilometers = 7.38*1.61
kilometers_to_miles = 12.25/1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")


####################################
# write your code here 
#3x3 - 2x2 + 3x - 1
x = 0
x = float(x)

y=3*x**3-2*x**2+3*x-1
print("x=0, y =", y)

x = 1
x = float(x)
y=3*x**3-2*x**2+3*x-1
print("x=0, y =", y)

x = -1
x = float(x)
y=3*x**3-2*x**2+3*x-1
print("x=0, y =", y)


# If you'd like to quickly comment or uncomment multiple lines of code, select the line(s) 
# you wish to modify and use the following keyboard shortcut: CTRL + / (Windows) or CMD + / (Mac OS). 
# It's a very useful trick, isn't it? Try this code in Sandbox.

######################

anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

#####################
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

true=0
TRUE=1
True=2
tRUE3