variable1 = 1
variable2 = 2

variable1, variable2 = variable2, variable1

print(variable1)
print(variable2)

variable1 = 1
variable2 = 2

auxiliary = variable1
variable1 = variable2
variable2 = auxiliary

print(variable1)
print(variable2)