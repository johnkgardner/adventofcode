# https://adventofcode.com/2020/day/2

# Reading in Question Input: 
data = open("day2.txt", "r")
lines = data.readlines()

# Part 1:
count = 0
for line in lines:
   separated = line.strip().split()
   low, high = separated[0].split("-")
   low = int(low)
   high = int(high)
   ch = separated[1].split(":")[0]
   pw = separated[2]
   cnt = pw.count(ch)
   if cnt >= low and cnt <= high:
      count += 1

print("Part 1: " + str(count))  

# Part 2:
count = 0
for line in lines: 
   separated = line.strip().split()
   iPos,fPos  = separated[0].split("-")
   iPos = int(iPos)
   fPos = int(fPos)
   ch = separated[1].split(":")[0]
   pw = separated[2]
   # this part is an XOR
   if (pw[iPos-1] == ch) != (pw[fPos-1] == ch):
      count += 1

print("Part 2: " + str(count))

