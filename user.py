import time
import sys

def progress():
	toolbar_width = 49

	sys.stdout.write("[%s]" % ("-" * toolbar_width))
	sys.stdout.flush()
	sys.stdout.write("\b" * (toolbar_width+1))

	for i in range(toolbar_width):
	    time.sleep(0.05)
	    sys.stdout.write("#")
	    sys.stdout.flush()
	
	sys.stdout.write("]\n")


def signup(u,p):

	f = open('udata.txt','a')
	encred = encrypt(u,p)
	f.write("%s " % encred[0])
	f.write("%s\n" % encred[1])
	print("-"*50)
	progress()
	print("-"*50)
	print("> Your credentials have been accepted.")
	print("-"*50)
	print("\n")
	f.close()

	return u,p


def login(u,p):
	
	f = open('udata.txt','r')
	b = False
	for x in f:
		line = x
		l = ""
		for x in line:
			l += x
		l = l.split(' ')
		l1 = list(l[1])
		l2 = l1[:len(l1)-1]
		l3 = ''.join(l2)
		decred = decrypt(l[0],l3)
		us = decred[0]
		pas = decred[1]
		if us==u and pas==p:
			progress()
			print("-"*50)
			print("> You have been logged in.")
			print("-"*50)
			print("\n")
			b = True
			break
	if b == False:
		progress()
		print("-"*50)
		print("> You have entered invalid credentials.")
		print("-"*50)
		print("\n")
	f.close()
	
	return u,True


def encrypt(u,p):
	
	u = list(u)
	p = list(p)
	uencrypt,pencrypt = [],[]
	for x in p:
		if x.isdigit() and x!=0:
			shift = int(x)
			ind = p.index(x)
			break
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for x in u:
		for y in alphabet:
			if x==y:
				uencrypt += alphabet[(alphabet.index(y))+shift]
				break
			else:
				uencrypt += chr(ord(x)+shift)
				break
	for x in p:
		for y in alphabet:
			if x==y:
				pencrypt += alphabet[(alphabet.index(y))+shift]
				break
			elif x!=str(shift):
				if x==str(0):
					pencrypt += x
				else:
					pencrypt += chr(ord(x)+shift)
				break
			else:
				pencrypt += x
				break
	uname = ''.join(uencrypt)
	passw = ''.join(pencrypt)
	
	
	return uname,passw
	
	

def decrypt(u,p):
	
	shift,ind,c = 0,0,0
	u,p = list(u),list(p	)
	udecrypt,pdecrypt = [],[]
	for x in p:
		if x.isdigit() and x!=0:
			shift = int(x)
			ind = p.index(x)
			break
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for x in u:
		for y in alphabet:
			if x==y:
				udecrypt += alphabet[(alphabet.index(y))-shift]
				break
			else:
				udecrypt += chr(ord(x)-shift)
				break
	for x in p:
		for y in alphabet:
			if x==y:
				pdecrypt += alphabet[(alphabet.index(y))-shift]
				break
			elif x!=str(shift):
				if x==str(0):
					pdecrypt += x
				else:
					pdecrypt += chr(ord(x)-shift)
				break
			else:
				pdecrypt += x
				break
	una = ''.join(udecrypt)
	pas = ''.join(pdecrypt)
	
	return una,pas



def login_or_signup(log):
	
	if log == 'signup':
		progress()
		q = False
		spaces,r = 0,0
		def us():
			print("-"*50)
			use = input("  USERNAME:> ")
			return use
		def check(u):
			c = True
			try:
				f = open('udata.txt','r')
			except FileNotFoundError:
				f = open('udata.txt','w')
				f.close()
				f = open('udata.txt','r')
			for x in f:	
				line = x
				l = ""
				for x in line:
					l += x
				l = l.split(' ')
				l1 = list(l[1])
				l2 = l1[:len(l1)-1]
				l3 = ''.join(l2)
				d = decrypt(l[0],l3)
				if u==d[0]:
					print("-"*50)
					print("Username already exists. Please enter a new one...")
					print("-"*50)
					c = False
					return c
					break
		while r==False:
			user = us()
			r = check(user)
		while q == False:
			for x in user:
				if x.isspace():
					spaces+= 1
			if len(user) >= 5 and spaces==0:
				q = True
			else:
				print("Username should not contain spaces and should be atleast 5 characters long. Please enter a new one.")
				print("-"*50)
				user = input("  USERNAME:> ")
		q = False
		print("-"*50)
		passwrd = input("  PASSWORD:> ")
		while q == False:
			special = 0
			numbers = 0
			for x in passwrd:
				if x.isdigit():
					numbers += 1
				elif x.isalnum() != True:
					special += 1
			if special >= 1 and numbers >= 1:
				q = True
			else:
				print("-"*50)
				print("\n")
				print("Password must have special characters and numbers for better security.")
				print("-"*50)
				passwrd = input("  PASSWORD:> ")
				print("-"*50)

		
		signup(user,passwrd)
	
	
	elif log == 'login':
		progress()
		print("-"*50)
		user = input("  USERNAME:> ")
		print("-"*50)
		passwrd = input("  PASSWORD:> ")
		print("-"*50)
		login(user,passwrd)
	

def inputchoice():
		
	q = False
	print("-"*50)
	print("Do you want to Login or Signup ?")
	print("-"*50)
	choice = input("> ")
	print("-"*50)
	while q == False:
		choice = choice.lower()
		choice = choice.strip()
		if choice == "login" or choice == "signup":
			q = True
		else:
			print("-"*50)
			choice = input("Do you want to Login or Signup ?\n")
			print("-"*50)
			print("\n")
	
	login_or_signup(choice)


inputchoice()
	