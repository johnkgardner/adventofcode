# https://adventofcode.com/2020/day/3

# Read Input
input = open("day3.txt", "r")
lines = [ln[:-1] for ln in input.readlines() ] # needed to get lines with no \n at end


#Part 1: 

# Set variables
edge = len(lines[0]) # we will use %edge so that we go back to x=0 when we "go over the edge"
bottom = len(lines) - 1
x = 0 
y = 0
tree_count = 0

while y < bottom:
   x += 3
   y += 1
   if lines[y][x%edge] == '#': 
      tree_count += 1

print(tree_count)


# Part 2

