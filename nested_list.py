#You can use nested lists in Python to create matrices (i.e., two-dimensional lists). 

# A four-column/four-row table - a two dimensional array (4x4)

table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(table)
print(table[0][0]) # outputs: ':('
print(table[0][3]) # outputs: ':)'

 # You can nest as many lists in lists as you want, and therefore create n-dimensional lists, e.g., 
 # three-, four- or even sixty-four-dimensional arrays
 
 # Cube - a three-dimensional array (3x3x3)

cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

print(cube)
print(cube[0][0][0]) # outputs: ':('
print(cube[2][2][0]) # outputs: ':)'