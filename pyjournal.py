import time, sys, os, platform
from datetime import date


def progress():
	
	toolbar_width = 49
	sys.stdout.write("[%s]" % ("-" * toolbar_width))
	sys.stdout.flush()
	sys.stdout.write("\b" * (toolbar_width+1))
	for _ in range(toolbar_width):
	    time.sleep(0.03)
	    sys.stdout.write("#")
	    sys.stdout.flush()	
	sys.stdout.write("]\n")


def actualsignup(u,p):

	f = open('udata.txt','a')
	encred = encrypt(u,p)
	f.write("%s " % encred[0])
	f.write("%s\n" % encred[1])
	print("-"*50)
	progress()
	print("-"*50)
	print("> Your credentials have been accepted.")
	print("-"*50)
	f.close()

	inputchoice()


def actuallogin(u,p):
	
	if platform.system() == "Linux":
		if 'ANDROID_STORAGE' in os.environ:
			try:
				os.chdir('/storage/emulated/0/pyjournal')
				f = open("udata.txt","r")
			except:
				os.makedirs('/storage/emulated/0/pyjournal')
				os.chdir('/storage/emulated/0/pyjournal')
				f = open("udata.txt","w")
				f.close()
				f = open("udata.txt","r")
		else:
			try:
				os.chdir('/pyjournal')
				f = open("udata.txt","r")
			except:
				os.makedirs('/pyjournal')
				os.chdir('/pyjournal')
				f = open("udata.txt","w")
				f.close()
				f = open("udata.txt","r")
	elif platform.system() == "Windows":
		try:
			os.chdir('C:/Users/%s/Documents/pyjournal' % os.getenv('username'))
			f = open("udata.txt","r")
		except:
			os.chdir('C:/Users/%s/Documents' % os.getenv('username'))
			os.mkdir('pyjournal')
			os.chdir('C:/Users/%s/Documents/pyjournal' % os.getenv('username'))
			f = open("udata.txt","w")
			f.close()
			f = open("udata.txt","r")
	else:
		try:
			os.chdir('/pyjournal')
			f = open("udata.txt","r")
		except:
			os.makedirs('/pyjournal')
			os.chdir('/pyjournal')
			f = open("udata.txt","w")
			f.close()
			f = open("udata.txt","r")
	if platform.system() == "Linux":
		if 'ANDROID_STORAGE' in os.environ:
			size = os.path.getsize('/storage/emulated/0/pyjournal/udata.txt')
		else:
			size = os.path.getsize('/pyjournal/udata.txt')
	elif platform.system() == "Windows":
		size = os.path.getsize('C:/Users/%s/Documents/pyjournal/udata.txt' % os.getenv('username'))
	else:
		size = os.path.getsize('/pyjournal/udata.txt')
	if  size == 0:
		print("> No user credentials found. Please signup for creating a new one.")
		print("-"*50)
		exit(0)
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
		if us == u and pas == p:
			progress()
			print("-"*50)
			print("> You have been logged in.")
			print("-"*50)
			print("\n")
			journal(u,p)
			b = True
			break
	if b == False:
		progress()
		print("-"*50)
		print("> You have entered invalid credentials.")
		print("-"*50)
		print("\n")
	f.close()

	inputchoice()


def encrypt(u,p):
	
	u = list(u)
	p = list(p)
	uencrypt,pencrypt = [],[]
	for x in p:
		if x.isdigit() and x != 0:
			shift = int(x)
			break
	alphabet = list(map(chr, range(97,123)))
	for x in u:
		for y in alphabet:
			if x == y:
				uencrypt += alphabet[(alphabet.index(y))+shift]
				break
			else:
				uencrypt += chr(ord(x)+shift)
				break
	for x in p:
		for y in alphabet:
			if x == y:
				pencrypt += alphabet[(alphabet.index(y))+shift]
				break
			elif x!=str(shift):
				if x == str(0):
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
	
	shift = 0
	u,p = list(u),list(p)
	udecrypt,pdecrypt = [],[]
	for x in p:
		if x.isdigit() and x != 0:
			shift = int(x)
			break
	alphabet = list(map(chr, range(97,123)))
	for x in u:
		for y in alphabet:
			if x == y:
				udecrypt += alphabet[(alphabet.index(y))-shift]
				break
			else:
				udecrypt += chr(ord(x)-shift)
				break
	for x in p:
		for y in alphabet:
			if x == y:
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

	
def signup():

	progress()
	q = False
	spaces, r = 0, 0
	def us():
		print("-"*50)
		q = False
		while q == False:
			try:
				use = input("  USERNAME:> ")
				q = True
			except:
				continue
		return use
	def check(u):
		c = True
		if platform.system() == "Linux":
			if 'ANDROID_STORAGE' in os.environ:
				try:
					os.chdir('/storage/emulated/0/pyjournal')
					f = open("udata.txt","r")
				except:
					os.makedirs('/storage/emulated/0/pyjournal')
					os.chdir('/storage/emulated/0/pyjournal')
					f = open("udata.txt","w")
					f.close()
					f = open("udata.txt","r")
			else:
				try:
					os.chdir('/pyjournal')
					f = open("udata.txt","r")
				except:
					os.makedirs('/pyjournal')
					os.chdir('/pyjournal')
					f = open("udata.txt","w")
					f.close()
					f = open("udata.txt","r")
		elif platform.system() == "Windows":
			try:
				os.chdir('C:/Users/%s/Documents/pyjournal' % os.getenv('username'))
				f = open("udata.txt","r")
			except:
				os.chdir('C:/Users/%s/Documents' % os.getenv('username'))
				os.mkdir('pyjournal')
				os.chdir('C:/Users/%s/Documents/pyjournal' % os.getenv('username'))
				f = open("udata.txt","w")
				f.close()
				f = open("udata.txt","r")
		else:
			try:
				os.chdir('/pyjournal')
				f = open("udata.txt","r")
			except:
				os.makedirs('/pyjournal')
				os.chdir('/pyjournal')
				f = open("udata.txt","w")
				f.close()
				f = open("udata.txt","r")
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
			if u == d[0]:
				print("-"*50)
				print("> Username already exists. Please enter a new one...")
				print("-"*50)
				c = False
				return c
	while r == False:
		user = us()
		r = check(user)
	while q == False:
		for x in user:
			if x.isspace():
				spaces+= 1
		if len(user) >= 5 and spaces == 0:
			q = True
		else:
			print("-"*50)
			print("> Username should not contain spaces and should be atleast 5 characters long.")
			print("-"*50)
			v = False
			while v == False:
				try:
					user = input("  USERNAME:> ")
					v = True
				except:
					continue
	print("-"*50)
	v = False
	while v == False:
		try:
			passwrd = input("  PASSWORD:> ")
			v = True
		except:
			continue
	q = False
	while q == False:
		special = 0
		numbers = 0
		for x in passwrd:
			if x.isdigit():
				numbers += 1
			elif x.isalnum() != True:
				special += 1
		if special >= 1 and numbers >= 1 and len(passwrd) >= 5:
			q = True
		else:
			print("-"*50)
			print("> Password must have special characters,numbers and should be at least 5 characters long.")
			print("-"*50)
			v = False
			while v == False:
				try:
					passwrd = input("  PASSWORD:> ")
					v = True
				except:
					continue

	actualsignup(user,passwrd)

def login():

	progress()
	print("-"*50)
	v = False
	while v == False:
		try:
			user = input("  USERNAME:> ")
			v = True
		except:
			continue
	print("-"*50)
	v = False
	while v == False:
		try:
			passwrd = input("  PASSWORD:> ")
			v = True
		except:
			continue
	print("-"*50)

	actuallogin(user,passwrd)


def journal(u,p):
	
	username = encrypt(u,p)
	if platform.system() == "Linux":
		if 'ANDROID_STORAGE' in os.environ:
			try:
				os.chdir('/storage/emulated/0/pyjournal/%s' % username[0])
			except:
				os.chdir('/storage/emulated/0/pyjournal')
				os.mkdir(username[0])
				os.chdir('/storage/emulated/0/pyjournal/%s' % username[0])
		else:
			try:
				os.chdir('/pyjournal/%s' % username[0])
			except:
				os.chdir('/pyjournal')
				os.mkdir(username[0])
				os.chdir('/pyjournal/%s' % username[0])
	elif platform.system() == "Windows":
		try:
			os.chdir('C:/Users/%s/Documents/pyjournal/%s' % (os.getenv('username'),username[0]))
		except:
			os.chdir('C:/Users/%s/Documents/pyjournal' % os.getenv('username'))
			os.mkdir(username[0])
			os.chdir('C:/Users/%s/Documents/pyjournal/%s' % (os.getenv('username'),username[0]))
	else:
		try:
			os.chdir('/pyjournal/%s' % username[0])
		except:
			os.chdir('/pyjournal')
			os.mkdir(username[0])
			os.chdir('/pyjournal/%s' % username[0])
	today = date.today()
	d = today.strftime("%d/%m/%Y")
	d = d.split("/")
	d = '.'.join(d)
	entry = open('%s.txt' % d,'a')
	v = False
	while v == False:
		try:
			choice = input("<%s@pyjournal> " % u)
			choice = choice.lower()
			choice = choice.strip()
			if choice == "check" or choice == "entry":
				v = True
			elif choice == "login":
				print("-"*50)
				print("> You are already logged in.")
				print("-"*50)
			elif choice == "signup":
				print("-"*50)
				print("> You already have a journal.")
				print("-"*50)
			elif choice == "kill":
				os._exit(0)
			elif choice == "help":
				print("-"*50)
				print("   entry: Adds a new entry to your journal for this day\n   check: Accepts a date and checks previous entries in your journal")
				print("-"*50)
			else:
				print("-"*50)
				print("  Type help for more info")
				print("-"*50)
		except:
			print("  Type help for more info")
			continue
	print("-"*50)
	if choice == "entry":
		entryin = input("  ENTRY:> ")
		print("-"*50)
		encred = encrypt(entryin,p)
		entry.write("%s\n" % encred[0])
	elif choice == "check":
		v = False
		while v == False:
			try:
				entrydate = input("  DATE (dd/mm/yyyy):> ")
				testdate = entrydate.split("/")
				_ = int(testdate[1])
				_ = int(testdate[2])
				v = True
			except:
				continue
		def checkdate(edate):
			edate = edate.strip()
			datelist = edate.split("/")
			dd = int(datelist[0])
			mm = int(datelist[1])
			yyyy = int(datelist[2])
			m30 = [4,6,9,11]
			m31 = [1,3,5,7,8,10,12]
			m = 0
			cd = False
			if mm in m30:
				if dd > 0 and dd <= 30:
					m = 1
			elif mm in m31:
				if dd > 0 and dd <= 31:
					m = 1
			elif mm == 2:
				if yyyy % 4 == 0:
					if dd > 0 and dd <= 29:
						m = 1
				else:
					if dd > 0 and dd <= 28:
						m = 1
			else:
				return cd
			if m == 1:
				cd = True
				return cd
			else:
				return cd
		q = False
		while q == False:
			z = checkdate(entrydate)
			if z == True:
				q = True
			else:
				print("-"*50)
				print("> You entered an invalid date.")
				print("-"*50)
				entrydate = input("  DATE (dd/mm/yyyy):> ")
		print("-"*50)
		entrydate = entrydate.replace('/','.')
		try:
			entry = open('%s.txt' % entrydate,'r')
		except:
			print("> ENTRIES DATED %s" % entrydate)
			print("-"*50)
			print("  No entries on this day")
			print("-"*50)
			exit(0)
		entryout = entry.readlines()
		out = ''
		for x in entryout:
			decred = decrypt(x,p)
			out += decred[0] + '\n    '
		out = out.strip()
		print("> ENTRIES DATED %s :" % entrydate)
		print("-"*50)
		print("    %s" % out)
		print("-"*50)

		inputchoice()


def inputchoice():
		
	q = False
	while q == False:
		try:
			choice = input("</@pyjournal> ")
			choice = choice.lower()
			choice = choice.strip()
			if choice == "login":
				login()
				q = True
			elif choice == "signup":
				signup()
				q = True
			elif choice == "kill":
				os._exit(0)
			elif choice == "clear":
				if platform.system() == "Windows":
					os.system('cls')
				elif platform.system() == "Linux":
					os.system('clear')
				else:
					os.system('clear')
			elif choice == "help":
				print("-"*50)
				print("To get started with pyjournal, type any of these commands:\n\n   login: Enter your username and password to access your journal\n   signup: Enter a new username and password to create your journal\n   clear: Clears the screen")
				print("-"*50)
		except:
			print("Type help for more info")
			continue


print("-"*50)
print("#"*50)
print("                PYJOURNAL                ")
print("#"*50)
print("-"*50)
inputchoice()