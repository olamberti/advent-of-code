# Adapters
ads = [int(x) for x in open('10.txt').read().splitlines()]
ads.append(0)
ads.sort()
ads.append(ads[-1] + 3)

# P1 & P2
n1, n3 = 0, 0
arr = {key: None for key in ads}
arr[0], arr[ads[1]] = 1, 1
for i in range(len(ads) - 1):
  # P1
  if ads[i + 1] - ads[i] == 1: n1 += 1
  elif ads[i + 1] - ads[i] == 3: n3 +=1
  # P2
  if i == 2:
    if ads[2] <= 3: arr[ads[2]] = 2
    else: arr[ads[2]] = 1
  elif i > 2:
    arr[ads[i]] = arr[ads[i - 1]]
    if ads[i] - ads[i - 2] <= 3: arr[ads[i]] += arr[ads[i - 2]]
    if ads[i] - ads[i - 3] <= 3: arr[ads[i]] += arr[ads[i - 3]]
    
print(n1 * n3)
print(arr[ads[-2]])