def char_range(c1, c2):
  for c in range(ord(c1), ord(c2)+1):
      yield chr(c)

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
    codes = {} # stores set of letter known to be connected to digit
    segs = ['']*7 # stores letter known to correspond to segment
    counts = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,}
    number = ''
    for digit in display[0]:
      if len(digit) == 2:
        codes['1'] = [segment for segment in digit]
      elif len(digit) == 4:
        codes['4'] = [segment for segment in digit]
      elif len(digit) == 3:
        codes['7'] = [segment for segment in digit]       
      elif len(digit) == 7:
        codes['8'] = [segment for segment in digit]

      i = 0
      for char in char_range('a','g'):
        if char in digit:
          counts[char] += 1

    #print(counts)

    # deduces which letter correspond to each segment
    for char in char_range('a','g'):
      if char in codes['7'] and char not in codes['1']:
        segs[0] = char
      elif counts[char] == 6:
        segs[1] = char
      elif counts[char] == 8:
        segs[2] = char
      elif counts[char] == 4:
        segs[4] = char
      elif counts[char] == 9:
        segs[5] = char
      elif char in codes['8'] and char not in codes['4']:
        segs[6] = char
      else:
        segs[3] = char

    #define remaining codes
    codes['0'] = [segs[0], segs[1], segs[2], segs[4], segs[5], segs[6]]
    codes['2'] = [segs[0], segs[2], segs[3], segs[4], segs[6]]
    codes['3'] = [segs[0], segs[2], segs[3], segs[5], segs[6]]
    codes['5'] = [segs[0], segs[1], segs[3], segs[5], segs[6]]
    codes['6'] = [segs[0], segs[1], segs[3], segs[4], segs[5], segs[6]]
    codes['9'] = [segs[0], segs[1], segs[2], segs[3], segs[5], segs[6]]

    #print(codes)

    # original method is used for 1, 4, 7, 8, dictionary used for others
    # done from most segments to least to prevent issues of overlapping numbers
    # i.e. a 6 accidentally reading as being a 5
    for digit in display[1]:
      if len(digit) == 2:
        number += '1'
      elif len(digit) == 4:
        number += '4'
      elif len(digit) == 3:
        number += '7'       
      elif len(digit) == 7:
        number += '8'
      elif all(seg in digit for seg in codes['0']):
        number += '0'
      elif all(seg in digit for seg in codes['9']):
        number += '9'
      elif all(seg in digit for seg in codes['6']):
        number += '6'
      elif all(seg in digit for seg in codes['5']):
        number += '5'
      elif all(seg in digit for seg in codes['3']):
        number += '3'
      elif all(seg in digit for seg in codes['2']):
        number += '2'
    #print(number)
    answer += int(number)
  
  print(answer)

if __name__ == "__main__":
  main()
