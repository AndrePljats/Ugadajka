import random
def is_valid(n):
	return n.isdigit() and float(n)-int(float(n))==0 and 1<=int(n)<=100
def generate_num():
	print('Enter 1st and 2nd digits (Range 1-100)')
	while True:
		a,b=input(),input()
		if is_valid(a) and is_valid(b):
			a,b=int(a),int(b)
			if a<b:
				print('Your range:',a,'-',b)
				return random.randint(a,b)
			elif a>b:
				print('Your range change to:',b,'-',a)
				return random.randint(b,a)
		else:
			print('Enter correct 2 digits (for example: 50 80)')
def input_num():
	while True:
		print('Enter digit from 1 to 100')
		input_num=input()
		if is_valid(input_num):
			return int(input_num)
			break
		else:
			print('Try again!')
def compare():
	gen_n=generate_num()
	count=0
	while True:
		in_n=input_num()
		if in_n<gen_n:
			print('Generate Num is largest!')
			count+=1
		elif in_n>gen_n:
			print('Generate num is smallest!')
			count+=1
		else:
			print('You win! Score is',count)
			break
def retry():
	print('Do you want play again? Enter y/n')
	while True:
		ans=input()
		if ans=='y' or ans=='Y':
			game()
		elif ans=='n' or ans=='N':
			print('See you soon!')
			break
		else:
			print('OMG! Enter y/n!')
def game():
	print('Welcome to game!')
	compare()
	retry()
game()