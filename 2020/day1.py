# https://adventofcode.com/2020/day/1

# Read Input In
data = open('input.txt', 'r').read()
data = [int(n) for n in data.split()]


#Part 1
for i in range(len(data)): 
   for j in range(i+1, len(data)): 
      if data[i]+data[j] == 2020:
         print(data[i]*data[j])


# Part 2
for i in range(len(data)):
   for j in range(i+1, len(data)): 
      for k in range(j+1, len(data)): 
         if data[i] + data[j] + data[k] == 2020: 
            print(data[i]*data[j]*data[k])
