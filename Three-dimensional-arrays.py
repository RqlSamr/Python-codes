# Imagine a hotel. It's a huge hotel consisting of three buildings, 15 floors each. There are 20 rooms on each floor.
# For this, you need an array which can collect and process information on the occupied/free rooms.

# First step - the type of the array's elements. In this case, a Boolean value (True/False) would fit.

# Step two - calm analysis of the situation. Summarize the available information: three buildings, 15 floors, 20 rooms.

rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
# The first index (0 through 2) selects one of the buildings; 
# the second (0 through 14) selects the floor, the third (0 through 19) selects the room number. All rooms are initially free.

vacancy = 0
rooms[1][9][13] = True
rooms[0][4][1] = False

for roomNumber in range(20):
    if not rooms[2][14][roomNumber]:
        vacancy += 1