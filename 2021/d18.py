from copy import deepcopy as dc     # for deep copying lists
data = []                           # for storing inputs

def convert(x):                     # converts everything to list type
  if type(x) is int: return [x]     # if integer, return one element list
  return [convert(y) for y in x]    # recursion

for line in open('d18.txt', 'r'):   # read input file
  data.append(convert(eval(line)))  # add converted lines to data

# Functions:
def add_l(x, v):                    # increases the leftmost elem of x by v
  if x is None: return              # there is no left elem
  if len(x) == 1: x[0] += v         # left elem is number, so increase
  else: add_l(x[0], v)              # left elem is pair, recursion

def add_r(x, v):                    # increases the rightmost elem of x by v
  if x is None: return              # there is no right elem
  if len(x) == 1: x[0] += v         # left elem is number, so increase
  else: add_r(x[1], v)              # right elem is pair, recursion
    
def explode(x, l = None, r = None, d = 0):    # args: x to explode, left branch, right branch and depth
  if len(x) == 1:                             # elem is number
    return False                              # no explosion happened
  if d >= 4 and len(x[0]) == len(x[1]) == 1:  # 4 nests reached and we have a pair
    add_r(l, x[0][0])                         # add left value to the rightmost elem on the left block
    add_l(r, x[1][0])                         # add right value to the leftmost elem on the right block
    x[:] = [0]                                # replace x with 0
    return True                               # explosion happened
  return explode(x[0], l, x[1], d + 1) or explode(x[1], x[0], r, d + 1) # explode left first or right if no success

def split(x):                                 # splits the numbers greater than 10 to pairs in x
  if len(x) == 1:                             # we have a number
    if x[0] >= 10:                            # if greater than 10
      x[:] = [[x[0] // 2], [-(-x[0] // 2)]]   # half floor down and half floor up (--trick)
      return True                             # split happened
    else: return False                        # no split happened
  return split(x[0]) or split(x[1])           # first split left, or right if no success

def reduce(x):                                # reduce the number x
  while explode(x) or split(x):               # first explode, or split if no success
    pass                                      # if either explode or split happened, repeat

def mag(x):                                   # calculates the magnitude of the number
  if len(x) == 1: return x[0]                 # magnitude of number
  else: return 3 * mag(x[0]) + 2 * mag(x[1])  # magnitude of pair
    
# Part 1 - Add up all data:
a = data[0]                    # first number               
for b in data[1:]:             # loop through the rest of the numbers
  a = dc([a, b])               # addition is creating a new pair
  reduce(a)                    # reduce new pair
print(mag(a))

# Part 2 - Look for highest  sum:
m = 0                                # sum will be always positive (no negatives in input)
for i in range(len(data)):           # loop through combinations
  for j in range(len(data)): 
    if i == j: continue              # do not add up same indices
    pair = dc([data[i], data[j]])    # deepcopy pairs from data list
    reduce(pair)                     # reduce number
    m = max(m, mag(pair))            # check if larger than current max
print(m)