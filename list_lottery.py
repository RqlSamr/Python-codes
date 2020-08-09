# Let's assume that you've chosen the following numbers in the lottery: 3, 7, 11, 42, 34, 49.

# The numbers that have been drawn are: 5, 11, 9, 42, 3, 49.

# The question is: how many numbers have you hit?

lottery=[3, 7, 11, 42, 34, 49]
been_drawn=[5, 11, 9, 42, 3, 49]
hits=0

for i in been_drawn:
    if i in lottery:
      hits+=1

print(hits)      