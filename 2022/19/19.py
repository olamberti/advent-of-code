# Read input:
blueprints = []
for line in open('19.txt'):
  numbers = [int(x) for x in line.split() if x.isnumeric()]
  recipe = [[(0, numbers[0])], [(0, numbers[1])], [(0, numbers[2]), (1, numbers[3])], [(0, numbers[4]), (2, numbers[5])]]
  blueprints.append(recipe)  # recipe [robot_type (0-3)][(0: resource_type (0-3), 1: ore_cost]
  
# Calcualte maximum possible value of a blueprint:
def blueprint_value(blueprint, max_costs, resources, robots, time, cashe):
  
  if time == 0: return resources[3]                                                    # time is up, return number of geodes 

  state = tuple([time, *resources, *robots])                                           # create state variable
  if state in cache: return cache[state]                                               # check if we reached it before
  
  value = resources[3] + robots[3] * time                                              # current geodes & their production, if nothing happens 
                                                             
  for robot_type, recipe in enumerate(blueprint):                                      # iterate through each robot and check if we can build
    if robot_type != 3 and robots[robot_type] >= max_costs[robot_type][1]:             # miners reached the maximum numbers that is woth to build
      continue

    wait = 0                                                                           # waiting time till next build
    for resource_type, cost in recipe:                                                 # iterate through resources in the recipe
      if robots[resource_type] == 0:                                                   # there is no robot producing the necessary resource
        break
      wait = max(wait, -(-(cost - resources[resource_type]) // robots[resource_type])) # how much we need to wait until next robot is produced
    else:                                                                              # only runs if 'for' cycle was not broken, as last loop
      new_time = time - wait - 1                                                       # time left when robot is produced
      if new_time <= 0: continue                                                       # skip robot, no time to build it
      new_robots = robots[:]                                                           # robots for the next round
      new_robots[robot_type] += 1                                                      # we build the robot
      new_resources = [resources[i] + robots[i] * (wait + 1) for i in range(4)]        # resources for the next round
      for resource_type, cost in recipe:
        new_resources[resource_type] -= cost                                           # pay for the robot

      max_theory = new_resources[3] + new_robots[3] * new_time                         # theoretical maximum we can build
      for t in range(new_time):
        max_theory += t + 1                                                            # for every new geode cracker
      if max_theory < value: continue                                                  # if lower than current maximum, stop
      
      for i in range(3):                                                               # reduce number of resources (not geodes)
        new_resources[i] = min(new_resources[i], max_costs[i][1] * new_time )          # cut resources to maximum spenable amount
      value = max(value, blueprint_value(blueprint, max_costs, new_resources, new_robots, new_time, cashe))

  cache[state] = value                                                                 # store result in cache
  return value

# Part 1:
solution_1 = 0
for i, bp in enumerate(blueprints, 1):
  max_costs = [max(bp[0][0], bp[1][0], bp[2][0], bp[3][0]), bp[2][1], bp[3][1]]  # maximum cost of each material [ore, clay, obsidian]
  resources = [0, 0, 0, 0]                                                       # ore, clay, obsidian, geod
  robots = [1, 0, 0, 0]                                                          # ore miner, clay miner, obsidian miner, geode cracker
  time = 24                                                                      # time remaining
  cache = {}                                                                     # cache for storing results  
  bp_value = blueprint_value(bp, max_costs, resources, robots, time, cache)      # calculate max value of the blueprint
  solution_1 += i * bp_value                                                     # calculate quality and add it to answer
print(solution_1)

# Part 2:
solution_2 = 1
for i, bp in enumerate(blueprints, 1):
  max_costs = [max(bp[0][0], bp[1][0], bp[2][0], bp[3][0]), bp[2][1], bp[3][1]]  # maximum cost of each material [ore, clay, obsidian]
  resources = [0, 0, 0, 0]                                                       # ore, clay, obsidian, geod
  robots = [1, 0, 0, 0]                                                          # ore miner, clay miner, obsidian miner, geode cracker
  time = 32                                                                      # time remaining
  cache = {}                                                                     # cache for storing results  
  bp_value = blueprint_value(bp, max_costs, resources, robots, time, cache)      # calculate max value of the blueprint
  solution_2 = solution_2 * bp_value                                             # calculate Part 2 answer
  if i >= 3:
    break
print(solution_2)