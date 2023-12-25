from collections import defaultdict
from copy import deepcopy as dc
import random
import math

# Build up graph from input and store number of vertices (1 by default)
graph, vertices = defaultdict(list), defaultdict(int)
for line in open('d25.txt'):
    left, rights = line.split(': ')
    vertices[left] = 1
    for right in rights.split():
        graph[left].append(right)
        graph[right].append(left)
        vertices[right] = 1

# Karger's algorithm to find min cut in graph and keep track of merged vertices
def karger(graph, vertices):
    while len(graph) > 2:
        left = random.choice(list(graph.keys())) # pick random vertex (keep)
        right = random.choice(graph[left])       # pick random neighbor (merge)
        graph[left].extend(graph[right])         # add right's neighbors to left
        for node in graph[right]:                # update right's neighbors
            graph[node].remove(right)
            graph[node].append(left)
        del graph[right]                         # delete right from graph
        while left in graph[left]:               # remove self-loops
            graph[left].remove(left)
        vertices[left] += vertices[right]        # update merged vertices
        del vertices[right]                      # delete right from vertices
    return len(graph[list(graph.keys())[0]]), graph, vertices

cuts = None
while cuts != 3:
    cuts, rg, rv = karger(dc(graph), dc(vertices))
print(math.prod(rv.values()))