# Analyzing the input shows that the MONAD goes through all 14 model numbers and
# processes them almost the same way. All paramters are resetted, only z is carried with.
# Our goal is to reach 0 with z in the end.
#
# We can differentiate two modules, based on the number p1 in each modules 6th line.
# If we have a positive integer to add, z will always increase:
# The increasing module does this: z = 26 * z + digit + p2 (p2 is the integr in the 15th line)
#
# Or z can decrease based on some condition.
# The decreasing module does this: z = z // 26 if: digit = (z % 26) + p1
#
# Since there are 7-7 of each module, we always want to fulfill the condition
# in order to reduce z whenever we can.
# MONAD works like a (26 based) stack, where we either add digit + p2 to the stack,
# or remove the last item from the stack if new_digit = digit_stack + p2 + p1.
#
# Based on the aforesaid and using the fact that the digits can only be 1 - 9,
# we can calculate each digitaccording to part 1 or part 2.
##############################################################################################
# Read input:
inp = open('d24.txt', 'r').read().splitlines() # read input line by line

# Process MONAD parameters:
p = []                                 # parameters list
for i in range(14):                    # 14 different monad modules
  modul = inp[i * 18 : i * 18 + 18]    # cut module (each 18 line length)
  p1 = int(modul[5].split()[2])        # read p1 parameter
  p2 = int(modul[15].split()[2])       # read p2 parameter
  if p1 > 0: p.append(p2)              # if p1 is poistive, we store p2
  else: p.append(p1)                   # if p1 is negative, we store p1

# Build up equation model:
stack, eq = [], []                     # stack and equation lists
for i, x in enumerate(p):              # loop through parameters
  if x > 0: stack.append([i, x])       # if positive, increase stack
  if x < 0:                            # if negative:
    ds, p2 = stack.pop()               # get and pop stacks last item
    eq.append((i, ds, p2 + x))         # create equation like digit_i = digit_s + p2 + p1

# Solve for part 1 (maximize) and part 2 (minimize):
nM, nm = [''] * 14, [''] * 14          # our number
for d2, d1, a in eq:                   # parts of the equation
  if a >= 0:                           # second digit is larger
    nM[d2], nM[d1] = 9, 9 - a          # can be 9 and 9 - a
    nm[d1], nm[d2] = 1, 1 + a          # can be 1 and 1 + a
  else:                                # first digit is larger
    nM[d1], nM[d2] = 9, 9 + a          # can be 9 and 9 + a
    nm[d2], nm[d1] = 1, 1 - a          # can be 1 and 1 - a
print(''.join([str(x) for x in nM]))   # print part 1 result
print(''.join([str(x) for x in nm]))   # print part 2 result