# Read input:
data = open('d20.txt', 'r').read().splitlines()
iea = data[0]   # imnage enhancement algorithm
img = data[2:]  # image
edge = '.'      # points in the infinite, handled as edge

# Collect pixels lit up as complex numbers:
pix = set()
for r in range(len(img)):
  for c in range(len(img[r])):
    if img[r][c] == '#': pix.add(r + c * 1j)
      
# Function definitions:
def enhance(pixels, edge):
  mr, Mr = int(min(x.real for x in pixels)), int(max(x.real for x in pixels)) # smallest and largest row
  mc, Mc = int(min(x.imag for x in pixels)), int(max(x.imag for x in pixels)) # smallest and largest column
  new_pixels = set()                                                          # new pixel set

  for r in range(mr - 1, Mr + 2):                                             # loop throug rows (+- 1)
    for c in range(mc - 1, Mc + 2):                                           # loop through columns (+- 1)
      b = ''                                                                  # binary number for IEA
      for n in [-1 - 1j, -1, -1 + 1j, -1j, 0, 1j, 1 - 1j, 1, 1 + 1j]:         # loop through all 9 neighbours
        np = r + c * 1j + n                                                   # neighbour pixel
        if (mr > np.real or Mr < np.real) or (mc > np.imag or Mc < np.imag):  # neighbour pixel out of image
          b += '1' if edge == '#' else '0'                                    # decision based on edge
        elif np in pixels: b += '1'                                           # else check if pixel is lit up
        else: b += '0'                                                        # or not lit up
      if iea[int(b, 2)] == '#': new_pixels.add(r + c * 1j)                    # convert to binary and check IEA
  
  new_edge = iea[0] if edge == '.' else iea[-1]                               # calculate new edge based on IEA
  return (new_pixels, new_edge)
    
# Enhance picture twice:
for i in range(50):                  # repeat 50 times
  pix, edge = enhance(pix, edge)     # enhance image
  if i == 1:
    print(len(pix))                  # solution 1
print(len(pix))                      # solution 2