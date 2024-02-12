import random

# 3x3 puzzle
puzzle = random.sample(range(1, 10), 9)



print(" Random Puzzle Generated:")

print("{} {} {}".format(puzzle[0], puzzle[1], puzzle[2]))

print("{} {} {}".format(puzzle[3], puzzle[4], puzzle[5]))

print("{} {} {}".format(puzzle[6], puzzle[7], puzzle[8]))

print()


# checking if it is magic puzzle or not
while True:
    # rows
    r1 = puzzle[0] + puzzle[1] + puzzle[2]
    
    r2 = puzzle[3] + puzzle[4] + puzzle[5]
    
    r3 = puzzle[6] + puzzle[7] + puzzle[8]
   # columns 
    c1 = puzzle[0] + puzzle[3] + puzzle[6]
    
    c2 = puzzle[1] + puzzle[4] + puzzle[7]
   
    c3 = puzzle[2] + puzzle[5] + puzzle[8]
   # diagonals
    d1 = puzzle[0] + puzzle[4] + puzzle[8]
   
    d2 = puzzle[2] + puzzle[4] + puzzle[6]

    if r1 == r2 == r3 == c1 == c2 == c3 == d1 == d2 == 15:
        break
    else:
        # 3x3
        puzzle = random.sample(range(1, 10), 9)

# Display
print("Solved:")

print("{} {} {}".format(puzzle[0], puzzle[1], puzzle[2]))

print("{} {} {}".format(puzzle[3], puzzle[4], puzzle[5]))

print("{} {} {}".format(puzzle[6], puzzle[7], puzzle[8]))