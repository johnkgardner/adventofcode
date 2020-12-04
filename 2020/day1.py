# https://adventofcode.com/2020/day/1

# Read Input In
data = open('input.txt', 'r').read()
data = [int(n) for n in data.split()]


#Part 1: O(N*N) 
for i in range(len(data)): 
   for j in range(i+1, len(data)): 
      if data[i]+data[j] == 2020:
         print(data[i]*data[j])


# Part 2: O(N*N*N)
for i in range(len(data)):
   for j in range(i+1, len(data)): 
      for k in range(j+1, len(data)): 
         if data[i] + data[j] + data[k] == 2020: 
            print(data[i]*data[j]*data[k])
             

#Part 1 Redo: O(N)
tbl = {}
for i in range(len(data)): 
   if (2000-data[i]) in tbl:
      print(data[i]*(2000-data[i]))
      break
   tbl[data[i]] = data[i] 

# Part 2 Redo: O(N*N)
tbl = {}
for i in range(len(data)): 
   for j  in range(i+1, len(data)): 
      complement = 2000 - data[i] - data[j]
      if complement in tbl: 
         print(data[i] * data[j] * complement)
         quit()
      tbl[data[i]] = data[i]
      tbl[data[j]] = data[j] 
