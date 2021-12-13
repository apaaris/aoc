############## Part 1 ######################

inp = open('in.txt').read().splitlines()

a = [ [int(j) for j in x] for x in inp ]
step=100
f=0

def countN():
	c10,c0=0,0
	for i in range(10):
		for j in range(10):
			if a[i][j]==10:
				c10+=1
			if a[i][j]==0:
				c0+=1
	return c10,c0

for x in range(step):
	for i in range(10):
		for j in range(10):
			a[i][j]+=1
	while countN()[0]>0:
		for i in range(10):
			for j in range(10):
				if a[i][j]==10:
					a[i][j]=0
					f+=1
					for di,dj in [ [-1,1],[0,1],[1,1],[-1,0],[1,0],[-1,-1],[0,-1],[1,-1] ]:
						ni,nj=i+di,j+dj
						if 0<=ni<10 and 0<=nj<10:
							if a[ni][nj]!=10 and a[ni][nj]!=0:
								a[ni][nj]+=1
		# if countN()[1]==100:
		# 	print(x+1)
		# 	exit()
print(f)





########################################




############## Part 2 ######################

inp = open('in.txt').read().splitlines()

a = [ [int(j) for j in x] for x in inp ]
step=1000
f=0

def countN():
	c10,c0=0,0
	for i in range(10):
		for j in range(10):
			if a[i][j]==10:
				c10+=1
			if a[i][j]==0:
				c0+=1
	return c10,c0

for x in range(step):
	for i in range(10):
		for j in range(10):
			a[i][j]+=1
	while countN()[0]>0:
		for i in range(10):
			for j in range(10):
				if a[i][j]==10:
					a[i][j]=0
					f+=1
					for di,dj in [ [-1,1],[0,1],[1,1],[-1,0],[1,0],[-1,-1],[0,-1],[1,-1] ]:
						ni,nj=i+di,j+dj
						if 0<=ni<10 and 0<=nj<10:
							if a[ni][nj]!=10 and a[ni][nj]!=0:
								a[ni][nj]+=1
		if countN()[1]==100:
			print(x+1)
			exit()
#print(f)





########################################
