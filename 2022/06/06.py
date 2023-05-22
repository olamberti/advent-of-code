with open("06.txt","r") as input:
  text = input.read()
  start_of_packet = 0
  for i in range(len(text)):
    bit_1 = text[i : i + 4]
    bit_2 = text[i : i + 14]
    if len(set(bit_1)) == 4 and start_of_packet == 0:
      start_of_packet = i + 4
    if len(set(bit_2)) == 14:
      start_of_message = i + 14
      break
print(start_of_packet)
print(start_of_message)