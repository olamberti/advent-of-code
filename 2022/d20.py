# Read data:
data = [int(x) for x in open('d20.txt')]
part = 2

if part == 1:
  mixes = 1
  multi = 1
elif part == 2:
  mixes = 10
  multi = 811589153
  
# Create chain modell from chain links:
class ChainLink:
  def __init__(self, value):
    self.value = value
    self.right = None
    self.left = None
  
# Create chain:
chain = []
length = len(data)
for id, x in enumerate(data):
  chain.append(ChainLink(x * multi))  # 1 or 811589153
  if x == 0:
    zero_id = id

for link_1, link_2 in zip(chain[:], chain[1:]):
  link_1.right = link_2
  link_2.left = link_1
chain[0].left = chain[-1]
chain[-1].right = chain[0]

mod = length - 1

# Mix the file:
for m in range(mixes):  
  for id in range(len(data)):
    link = chain[id % length]
    if link.value == 0: continue
    
    cutted_link = link
    if link.value > 0:
      for i in range(link.value % mod):
        cutted_link = cutted_link.right
      if cutted_link == link:
        continue
      link.left.right = link.right
      link.right.left = link.left
      cutted_link.right.left = link
      link.right = cutted_link.right
      cutted_link.right  = link
      link.left = cutted_link
    
    if link.value < 0:
      for i in range(-link.value % mod):
        cutted_link = cutted_link.left
      if cutted_link == link:
        continue
      link.left.right = link.right
      link.right.left = link.left
      cutted_link.left.right = link
      link.left = cutted_link.left
      cutted_link.left  = link
      link.right = cutted_link

# Decode:
solution = 0
link = chain[zero_id]
for step in range(1, 3001):
  link = link.right
  if step % 1000 == 0:
    solution += link.value
print(solution)