print("# prog to play a dice game")
print(" press 'r' to roll the dice and 'q' to quit")
a=input()
if(a=='r'):
	import random
	print("you've got .... ",random.randint(1,6)," this time")
else:
	print("bye.")