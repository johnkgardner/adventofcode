# https://adventofcode.com/2020/day/4

data = open('input.txt', 'r')
lines = [ln[:-1] for ln in data.readlines() ] 

def valid(passport):
   fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
   if all(x in passport for x in fields):
      return True
   else:
      return False

passport = {} # Use dictionary to keep track of the passports contents, constant check for if the passport contains all the values at the end
count = 0

for line in lines:  
   # Empty strings are "falsy" in Python so we know a passport ends when our line evalualtes to false.
   if line:
      split = line.split() # splits our line into list of fields. Example: pid:526669252 eyr:1972 --> ['pid:526669252', 'eyr:197']  
      for s in split:
         x = s.split(":")
         passport[x[0]] = x[1] # Adding each field the line has to our passport dictionary. Example: passport = {..., 'pid':'526669252',...}
   # when our line is falsy, when the passport has ended and it is time to check if its valid. Need to check if we are on the last line as that wont eval to falsy
   if not line or (line == lines[len(lines)-1]):
      if valid(passport): 
         print(passport)
         print("OK")
         count += 1
      passport = {} # clear the passport! On to the next one. 
      
print(count)
