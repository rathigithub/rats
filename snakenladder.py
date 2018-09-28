# to import a file
import random
# starting up with the game
print(" welcome to the snake and ladder game!!!!!")
print(" you can start playing the game only if you get 1 or 6")
# 'while' the stmt is always true..is used so tht the loop willl be continued always
while True:
	print(" press 'r' to roll the dice or press 'q' to quit the game ")
	a=input()
# creating a function called dice which does the work of a dice
	def dice():
		d=(random.randint(1,6))
		return(d)
# 'if' condition to quit
	if(a=='q'):
		print("bye. hope we'd play another time...  :(")
		exit()
#'if' condition to check whether the user has pressed 'r' to roll the dice.
	if(a=='r'):
		p=dice()
		print(" you have got",p)
		if(p != 1 and p != 6):
			print("aww...try again...")
#'while' condition to start only if the user gets 1 or 6
while(p==1 or 6):
#to greet when the user gets 1
	print(" congradulations!!! your position is, ",p)
	print(" press 'r' to roll the dice or press 'q' to quit the game ")
	a=input()
	if(a=='r'):
		p=dice()
		current=p+1
		print(" you have got",p," and your position is, ",current)
	if(a=='q'):
		print("bye. hope we'd play another time...  :(")
		exit()
print("awww... try again...")



  










				