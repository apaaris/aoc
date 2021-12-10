def parse_data():
  with open('in.txt', 'r') as inFile:
    rawData = inFile.read().split('\n')
  data = [i.split(" | ") for i in rawData]
  #print(rawData)
  for x in range(len(data)):
    display = data[x]
    display = [i.split() for i in display]
    data[x] = display
  data.pop(len(data)-1)
  return data

def main():
  answer = 0
  counts = [0]*10
  displays = parse_data()
  for display in displays:
    for digit in display[1]:
      if len(digit) == 2:
        counts[1] += 1
      elif len(digit) == 4:
        counts[4] += 1
      elif len(digit) == 3:
        counts[7] += 1        
      elif len(digit) == 7:
        counts[8] += 1
  
  for x in counts:
    answer += x
  print(answer)

if __name__ == "__main__":
  main()
