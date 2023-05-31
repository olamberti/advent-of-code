from copy import deepcopy as dp
import itertools
from intcode import IntCode
memory = [int(x) for x in open('07.txt').read().split(',')]

# P1:
val, thrust = 0, 0
phases = [0, 1, 2, 3, 4]
combos = [i for i in itertools.permutations(phases, 5)]

for combo in combos:
  val = 0
  for ph in combo:
    program = IntCode(memory)
    val = program.run([ph, val])
  thrust = max(thrust, val)
print(thrust)

# P2:
thrust = 0
phases = [5, 6, 7, 8, 9]
combos = [i for i in itertools.permutations(phases, 5)]

for combo in combos:
  amplifiers = [IntCode(memory), IntCode(memory), IntCode(memory), IntCode(memory), IntCode(memory)]
  val, first = 0, True
  while not amplifiers[-1].halt:
    for i, ph in enumerate(combo):
      if first: 
        val = amplifiers[i].run([ph, val])
      else: val = amplifiers[i].run(val)
    first = False
  thrust = max(thrust, val)
print(thrust)