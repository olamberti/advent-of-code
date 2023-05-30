# Read and convert input
hexa = open('16.txt', 'r').read()
bits = ''.join([bin(int(x, 16))[2:].zfill(4) for x in hexa])

# Parse function
def parse(b):
  
  ver, typ = int(b[:3], 2), int(b[3:6], 2)
  b = b[6:]                                 
  
  if typ == 4:                  # literal value
    num = ''
    while True:                
      last = b[0]
      num += b[1:5]
      b = b[5:]
      if last == '0': break
    num = int(num, 2)
    return (ver, typ, num), b

  else:                           # operator
    packets = []
    lid = b[0]                    # length type ID
    b = b[1:]
    
    if lid == '0':                # 15-bit                  
      l = int(b[:15], 2)          # length of the packets
      p = b[15:15+l]              # packets
      b = b[15+l:]             
      while p:
        pack, p = parse(p)
        packets.append(pack)   
      
    elif lid == '1':              # 11-bit                  
      n = int(b[:11], 2)          # number of the packets
      b = b[11:]                  # packets
      for _ in range(n):
        pack, b = parse(b)
        packets.append(pack)
    
    return (ver, typ, packets), b  

# Parse input
trans = parse(bits)[0]

# Version sum calculator
def versions(code):
  ver = code[0]
  typ = code[1]
  if typ == 4:
    return ver
  else:
    for pack in code[2]:
      ver += versions(pack)
    return ver

# Value evaluator
def value(code):
  t = code[1]
  if t == 4: return code[2] 
  elif t == 0: return sum(value(pack) for pack in code[2])
  elif t == 1:
    val = 1
    for pack in code[2]: val *= value(pack)
    return val
  elif t == 2: return min(value(pack) for pack in code[2])
  elif t == 3: return max(value(pack) for pack in code[2])
  elif t == 5: return int(value(code[2][0]) > value(code[2][1]))
  elif t == 6: return int(value(code[2][0]) < value(code[2][1]))
  elif t == 7: return int(value(code[2][0]) == value(code[2][1]))
    
print(versions(trans))
print(value(trans))