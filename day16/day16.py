import numpy as np
f = open("in.txt","r")
def packetparse(binstring,versionlist):
  if binstring == '0'*len(binstring):
    #print(binstring)
    return 0
  #print(binstring)
  version = int(binstring[0:3],2)
  #print(version)
  versionlist.append(version)
  type = int(binstring[3:6],2)
  if type==4:
    print("Literal type")
    print(binstring)
    i = 6
    litbin = ""
    print(binstring[i])
    while binstring[i] == '1':
      print(i,binstring[i])
      litbin += binstring[i+1:i+5]
      i+=5
    litbin += binstring[i+1:i+5]
    print(litbin)
    finalval = (int(litbin,2))
    return (i+5,finalval)
  else:
    id = binstring[6]
    valuelist = []
    finval = 0
    if id=='0':
      #print("ID: "+id)
      #print(binstring[7:22],len(binstring[7:22]))
      binlength = int(binstring[7:22],2)
      #print("Total length: "+str(binlength))
      #if binlength > len(binstring): return 0
      currentlength = 0
      i = 22
      while currentlength < binlength:
        #print("Current length:" + str(currentlength)+"/"+str(binlength))
        count,val = packetparse(binstring[i:],versionlist)
        #print("Sub-packet length:" + str(count))
        valuelist.append(val)
        i+=count
        currentlength += count
      #print("Done")
      #return (22+currentlength)
      size = 22+currentlength
    elif id=='1':
      #print("ID: "+id)
      #print(binstring[7:18],len(binstring[7:18]))
      numbins = int(binstring[7:18],2)
      #print("Total packets: "+str(numbins))
      currentbins = 0
      currentlen = 0
      #print(versionlist)
      i = 18
      while currentbins < numbins:
        #print(binstring[i:])
        count,val = packetparse(binstring[i:],versionlist)
        #print("Sub-packet length:" + str(count))
        valuelist.append(val)
        currentlen+=count
        i+=count
        currentbins+=1
      #print(numbins,currentbins)
      #print(versionlist)
      #return (18+currentlen)
      size = 18+currentlen
    if type == 0: finval = sum(valuelist)
    if type ==1: finval = np.prod(valuelist)
    if type ==2: finval = min(valuelist)
    if type ==3: finval = max(valuelist)
    if type ==5:
      if valuelist[0]>valuelist[1]: finval = 1
      else: finval = 0
    if type ==6:
      if valuelist[0]<valuelist[1]: finval = 1
      else: finval = 0
    if type ==7:
      if valuelist[0]==valuelist[1]: finval = 1
      else: finval = 0
    return (size,finval)
binconv = ""
versionlist = []
for line in f:
  for char in line.strip():
    strbin = bin(int(char,16))[2:]
    while len(strbin)<4: strbin = '0'+strbin
    #print(strbin)
    binconv += strbin
print(binconv)
_,value = packetparse(binconv,versionlist)
print(versionlist)
print(sum(versionlist))
print(value)
f.close()
