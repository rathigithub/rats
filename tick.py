#print("_1_|_2_|_3_")
#print(" 7 | 8 | 9 ")
import random
b=['1','2','3','4','5','6','7','8','9']


co=random.randint(1,9)

def board():
		print(b[0]+'|'+b[1]+'|'+b[2])
		print("______")
		print(b[3]+"|"+b[4]+"|"+b[5])
		print("______")
		print(b[6]+"|"+b[7]+"|"+b[8])
count=1
while(count<=9):
	#player turn
	print("chose your position.")
	pl=int(input())
	b[pl-1]=("x")
	board()
	# comp turn
	#co=random.randint(1,9)
	print("the computer has chosen..",co)
	b[co-1]=("o")
	board()
	count=count+1

#winning conditions
if((b[0,4,8]=='x') or (b[2,4,6]=='x') or (b[0,1,2]=='x') or (b[3,4,5]=='x') or (b[6,7,8]=='x') or (b[0,3,6]=='x') or (b[1,4,7]=='x') or (b[2,5,8]=='x')):
	print("you won...")
elif((b[0,4,8]=='o') or (b[2,4,6]=='o') or (b[0,1,2]=='o') or (b[3,4,5]=='o') or (b[6,7,8]=='o') or (b[0,3,6]=='o') or (b[1,4,7]=='o') or (b[2,5,8]=='o')):
	print("I won..")
else:
	print("It's a tie..."


for i in range(0,4,8):
	if(a[i]==a[1+3]==a[i+6]):
		if(a[i]=='x'):
			print("you won")