def introduction(firstName, lastName):
    print("Hello, my name is", firstName, lastName)

introduction(firstName = "James", lastName = "Bond")
introduction(lastName = "Skywalker", firstName = "Luke")
	
    
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

# call the adding function here
adding(1, 2, 3)
adding(c = 1, a = 2, b = 3)
adding(3, c = 1, b = 2)


#The default parameter's value is set using clear and pictorial syntax:
def introduction(firstName, lastName="Smith"):
    print("Hello, my name is", firstName, lastName)

# call the function here
introduction("James", "Doe")
introduction("Henry")
introduction(firstName="William")

#Key Takeaways
# You can pass arguments to a function using the following techniques:

# positional argument passing in which the order of arguments passed matters (Ex. 1),
# keyword (named) argument passing in which the order of arguments passed doesn't matter (Ex. 2),
# a mix of positional and keyword argument passing (Ex. 3).

#Ex. 1
def subtra(a, b):
    print(a - b)

subtra(5, 2)    # outputs: 3
subtra(2, 5)    # outputs: -3


Ex. 2
def subtra(a, b):
    print(a - b)

subtra(a=5, b=2)    # outputs: 3
subtra(b=2, a=5)    # outputs: 3

Ex. 3
def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # outputs: 3
subtra(5, 2)    # outputs: 3

# It's important to remember that positional arguments mustn't follow keyword arguments.
# That's why if you try to run the following snippet:

def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # outputs: 3
subtra(a=5, 2)    # Syntax Error


#example error
def sum(a, b=2, c):
    print(a + b + c)

sum(a=1, c=3)

SyntaxError - a non-default argument (c) follows a default argument (b=2)