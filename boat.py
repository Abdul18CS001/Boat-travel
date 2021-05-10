import random

print("\n\n\t   Can you reach the home from the island ?\n\n")

print("\U0001F449You have only '20' Attempts to reach the home")

print("\U0001F449You can move maximum '3' places from your position")

print("\U0001F449LET'S PLAY!\n\n\n")

print("Island\U0001F3DD\t\t\t      \t\t\tHOME\U0001F3E0")

print("\n")

print("\U0001F6A4",end=" ")

for i in range(1,21):

	print(i,end=" ")print("\n")

a=int(input("\t\t     Press 1 to Start!\n"))

if a==1:

 	print("\nIsland\U0001F3DD\t\t\t\t\t\tHOME\U0001F3E0")

 	print("\n")

 	for i in range(1,21):

			if i==1:

				print("   \U0001F6A4",end=" ")

			else:

					print(i,end=" ")

print("\n")

pos=1

def travel(pos,a):

		if a<=pos+3 and a>pos:

			b=random.randint(pos,pos+3)

			if a==b:

				print("Island\U0001F3DD\t\t\t\t\t\tHOME\U0001F3E0")

				print("\n")

				print("\t\tOOPS!",chr(10062),"Returned to Island\U0001F44E\n")

				pos=0

				print("\U0001F6A4",end="   ")

				for i in range(1,21):

					print (i,end=" ")			

			else:

				pos=a

				print("Island\U0001F3DD\t\t\t\t\t\tHOME\U0001F3E0")

				print('\n')

				print("\t\t\tReached ",a,"\U0001F44D")

				print("\n")

				print("   ",end=" ")						    

				for i in range(1,21):

					if i==a:

						print("\U0001F6A4",end=" ")

					else:

						print(i,end=" ")

		else:

			print("\t\t\U0001F6AB you can't go from",pos,"to",a,"\U0001F6AB")

		return pos

		

atm=20

while atm>0:

				print("\t\t    Attempts left :",atm)

				a=int(input())

				print('\n')

				pos = travel(pos,a)

				print("\n")

				if pos== 20:

					print("\t\t\U0001F3C1 YOU RACHED THE HOME \U0001F3C1\n")

					print("\t\t\t\U0001F389Congrats!\U0001F38A\n\n\n")

					break

				atm-=1

if atm==0:

				print("\t\t\U0001F641You did not reach the home\U0001F641\n")

				print("\t\t\U0001F91DBetter luck next time\U0001F91D\n\n\n")
