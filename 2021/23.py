# Part 1 or 2:
part = 1

# Read input:
lines = open('23.txt', 'r').read().splitlines()                            # read input lines 

# Build up map:
corr = list(lines[1][1:-1])                                            # representation of corridor
rooms = [lines[r][c] for c in range(3, 10, 2) for r in range(2, 4)]    # representation of rooms
if part == 2:                                                          # if we need part 2 solution
  rooms_ = []
  for i, amph in enumerate(rooms):                                     # loop through room members
    rooms_.append(amph)                                                # add original room member
    if i == 0: rooms_.extend(['D', 'D'])                               # room 1 extension
    elif i == 2: rooms_.extend(['C', 'B'])                             # room 2 extension
    elif i == 4: rooms_.extend(['B', 'A'])                             # room 3 extension
    elif i == 6: rooms_.extend(['A', 'C'])                             # room 4 extension
  rooms = rooms_.copy()                                                # copy back to original room
entry = [2, 4, 6, 8]                                                   # corridor entries to rooms
room_size = len(rooms) // 4                                            # size of each room
costs = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}                         # cost for each type of step

# Function definitions
def state_vector(state):                    # creates tuple from the state representations
  return (state[0], *state[1], *state[2])   # cost, corrdior and rooms
  
def next_steps(state):
  moves = []

  cost, corr, rooms = state[0], state[1], state[2]      # read state 
  
  # 1) Possible moves out from rooms:
  for i in range(4):                                    # loop through rooms
    room = rooms[room_size*i : room_size*i + room_size] # cut room
    
    # Search 1st amphipod, its deepness and if we want to move it or not:
    amph, deep, move = None, None, False                # first amphipod, its deepness and need to move
    for j, tile in enumerate(room):                     # go through room tiles
      if tile != '.' and not amph:                      # we found the first amphipod in the room
        amph = tile                                     # amphipod type we found
        deep = j                                        # deepness in room (0 to room_szie - 1)
      if tile != '.' and tile != 'ABCD'[i]:             # room has still bad amphipod inside
        move = True                                     # we want to move the found amphipod
        break
    if not move: continue                               # if room is OK, we just continue
    
    # Possible moves from room to corridor:
    r_e = 2 + 2 * i                                     # room entrance index in corridor
    l, r = 1, 1                                         # going left and right
    l_done, r_done = False, False                       # left and right directions done
    while (not l_done) or (not r_done):                 # we can go to either of the directions
      # Move to the left
      pos = r_e - l
      if pos < 0 or corr[pos] != '.':                   # reached end of corridor or an other amphipod
        l_done = True 
      if (not l_done) and pos not in entry:             # legit move
        new_cost = cost + costs[amph] * (deep + l + 1)  # new cost value
        new_rooms = rooms.copy()                        # copy old rooms
        new_rooms[room_size*i + deep] = '.'             # remove old amphipod position
        new_corr = corr.copy()                          # copy old corridor
        new_corr[pos] = amph                            # add amphipod to its new position
        moves.append([new_cost, new_corr, new_rooms])   # add new state to moves
      l += 1                                            # increase l
      # Move to the right
      pos = r_e + r
      if pos > 10 or corr[pos] != '.':                  # reached end of corridor or an other amphipod
        r_done = True 
      if (not r_done) and pos not in entry:             # legit move
        new_cost = cost + costs[amph] * (deep + r + 1)  # new cost value
        new_rooms = rooms.copy()                        # copy old rooms
        new_rooms[room_size*i + deep] = '.'             # remove old amphipod position
        new_corr = corr.copy()                          # copy old corridor
        new_corr[pos] = amph                            # add amphipod to its new position
        moves.append([new_cost, new_corr, new_rooms])   # add new state to moves
      r += 1                            

  # 2) Possible moves from corridor to room:
  for pos, tile in enumerate(corr):                     # loop through corridor with indexing
    if tile != '.':                                     # amphipod found
      amph = tile                                       # identify amphipod (just value assignment)
      r_id = 'ABCD'.find(amph)                          # target rooms ID
      r_e = 2 + 2 * r_id                                # target rooms entrance in corridor
      
      move = True                                       # assume we want to move
      # Check if corridor is clear until room entry:
      s = 1 if pos < r_e else -1                        # step size
      for c in range(pos + s, r_e, s):                  # loop through tiles
        if corr[c] != '.':                              # amphipod is in the way
          move = False                                  # we will not move
          break
      # Check if room is OK to move in:
      if move:                                          # corridor is clear until room
        room = rooms[room_size* r_id : room_size* r_id + room_size]     # cut out room of interest
        deep = -1                                       # deepness in room
        for tile in room:                               # loop  through room with indexing
          if tile != '.' and tile != amph:              # check tile
            move = False                                # we will not move
            break
          if tile == '.': deep += 1                     # free deepness to move to

      # If we want to move the amphipod into the room:
      if move:
        dist = abs(r_e - pos) + deep + 1                # distance to cover
        new_cost = cost + costs[amph] * dist            # new cost
        new_corr = corr.copy()                          # copy old corridor
        new_corr[pos] = '.'                             # remove amphipod from corridor
        new_rooms = rooms.copy()                        # copy old rooms
        new_rooms[r_id * room_size + deep] = amph       # move amphipod to room
        moves.append([new_cost, new_corr, new_rooms])   # add new state to move     
        
  return moves

  
# Tree search:
import heapq as hq                                          # priority queue handler
start = [0, corr, rooms]                                    # start state
goal = [c for c in ''.join(x * room_size for x in 'ABCD')]  # room goal to reach

cache = set()                                               # cache
queue = [start]                                             # priority queue

while True:                                                 # repeat untill inner break
  state = hq.heappop(queue)                                 # get lowest cost state from queue and pop it

  
  sv = state_vector(state)                                  # create state vector
  if sv in cache: continue                                  # if already done it skip
  cache.add(sv)                                             # otherwise add to cache

  if state[2] == goal:                                      # if rooms are organized according to goal
    print(state[0])                                         # print cost
    break                                                   # and break

  for next_state in next_steps(state):                      # loop through next steps
    if state_vector(next_state) in cache: continue          # if state is in cache skip
    hq.heappush(queue, next_state)                          # otherwise push it to queue