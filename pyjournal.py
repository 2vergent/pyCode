import time, sys, os, platform, getpass
from datetime import date


def progress():
	
	toolbar_width = 64
	sys.stdout.write("[%s]" % ("-" * toolbar_width))
	sys.stdout.flush()
	sys.stdout.write("\b" * (toolbar_width+1))
	for _ in range(toolbar_width):
	    time.sleep(0.007)
	    sys.stdout.write("#")
	    sys.stdout.flush()	
	sys.stdout.write("]\n")


def actualsignup(u,p):

	f = open('udata.txt','a')
	encred = encrypt(u,p)
	f.write("%s " % encred[0])
	f.write("%s\n" % encred[1])
	os.mkdir('%s' % encred[0])
	print("-"*67)
	progress()
	print("-"*67)
	print("> User Credentials successfully written")
	print("-"*67)
	print("\n")
	f.close()

	inputchoice()


def actuallogin(u,p):
	
	if platform.system() == "Linux":
		if 'ANDROID_STORAGE' in os.environ:
			try:
				os.chdir('/storage/emulated/0/pyjournal')
			except:
				os.chdir('/storage/emulated/0')
				os.mkdir('pyjournal')
				os.chdir('/storage/emulated/0/pyjournal')
			try:
				f = open("udata.txt","r")
			except:
				f = open("udata.txt","w")
				f.close()
				f = open("udata.txt","r")
		else:
			try:
				os.chdir('%s/pyjournal' % os.path.expanduser('~'))
			except:
				os.chdir('%s' % os.path.expanduser('~'))
				os.mkdir('pyjournal')
				os.chdir('%s/pyjournal' % os.path.expanduser('~'))
			try:
				f = open("udata.txt","r")
			except:
				f = open("udata.txt","w")
				f.close()
				f = open("udata.txt","r")
	elif platform.system() == "Windows":
		try:
			os.chdir('C:/Users/%s/Documents/pyjournal' % os.getenv('username'))
		except:
			os.chdir('C:/Users/%s/Documents' % os.getenv('username'))
			os.mkdir('pyjournal')
			os.chdir('C:/Users/%s/Documents/pyjournal' % os.getenv('username'))
		try:
			f = open("udata.txt","r")
		except:
			f = open("udata.txt","w")
			f.close()
			f = open("udata.txt","r")
	else:
		try:
			os.chdir('%s/pyjournal' % os.path.expanduser('~'))
		except:
			os.chdir('%s' % os.path.expanduser('~'))
			os.mkdir('pyjournal')
			os.chdir('%s/pyjournal' % os.path.expanduser('~'))
		try:
			f = open("udata.txt","r")
		except:
			f = open("udata.txt","w")
			f.close()
			f = open("udata.txt","r")
	if platform.system() == "Linux":
		if 'ANDROID_STORAGE' in os.environ:
			size = os.path.getsize('/storage/emulated/0/pyjournal/udata.txt')
		else:
			size = os.path.getsize('%s/pyjournal/udata.txt' % os.path.expanduser('~'))
	elif platform.system() == "Windows":
		size = os.path.getsize('C:/Users/%s/Documents/pyjournal/udata.txt' % os.getenv('username'))
	else:
		size = os.path.getsize('%s/pyjournal/udata.txt' % os.path.expanduser('~'))
	if  size == 0:
		print("> No user credentials found. Use 'signup' command to get started")
		print("-"*67)
		print("\n")
		f.close()
	else:
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
				print("-"*67)
				print("> Login Successful")
				print("-"*67)
				print("\n")
				journal(u,p)
				b = True
				break
		if b == False:
			progress()
			print("-"*67)
			print("> Invalid User Credentials")
			print("-"*67)
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
	r = 0
	def us():
		print("-"*67)
		q = False
		while q == False:
			try:
				use = input("   USERNAME:> ")
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
				except:
					os.chdir('/storage/emulated/0')
					os.mkdir('pyjournal')
					os.chdir('/storage/emulated/0/pyjournal')
				try:
					f = open("udata.txt","r")
				except:
					f = open("udata.txt","w")
					f.close()
					f = open("udata.txt","r")
			else:
				try:
					os.chdir('%s/pyjournal' % os.path.expanduser('~'))
				except:
					os.chdir('%s' % os.path.expanduser('~'))
					os.mkdir('pyjournal')
					os.chdir('%s/pyjournal' % os.path.expanduser('~'))
				try:
					f = open("udata.txt","r")
				except:
					f = open("udata.txt","w")
					f.close()
					f = open("udata.txt","r")
		elif platform.system() == "Windows":
			try:
				os.chdir('C:/Users/%s/Documents/pyjournal' % os.getenv('username'))
			except:
				os.chdir('C:/Users/%s/Documents' % os.getenv('username'))
				os.mkdir('pyjournal')
				os.chdir('C:/Users/%s/Documents/pyjournal' % os.getenv('username'))
			try:
				f = open("udata.txt","r")
			except:
				f = open("udata.txt","w")
				f.close()
				f = open("udata.txt","r")
		else:
			try:
				os.chdir('%s/pyjournal' % os.path.expanduser('~'))
			except:
				os.chdir('%s' % os.path.expanduser('~'))
				os.mkdir('pyjournal')
				os.chdir('%s/pyjournal' % os.path.expanduser('~'))
			try:
				f = open("udata.txt","r")
			except:
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
				print("-"*67)
				print("> Username already exists")
				c = False
				return c
	while r == False:
		user = us()
		r = check(user)
	while q == False:
		spaces = 0
		for x in user:
			if x.isspace():
				spaces+= 1
		if len(user) >= 5 and spaces == 0:
			q = True
		else:
			print("-"*67)
			print("> Username should not contain spaces and should be atleast 5 characters long.")
			print("-"*67)
			v = False
			while v == False:
				try:
					user = input("   USERNAME:> ")
					v = True
				except:
					continue
	print("-"*67)
	v = False
	while v == False:
		try:
			passwrd = getpass.getpass("   PASSWORD:> ")
			v = True
		except:
			continue
		v = False
		special = 0
		numbers = 0
		for x in passwrd:
			if x.isdigit():
				numbers += 1
			elif x.isalnum() != True:
				special += 1
		if special >= 1 and numbers >= 1 and len(passwrd) >= 5:
			v = True
		else:
			print("-"*67)
			print("> Password must have special characters,numbers and should be at least 5 characters long")
			print("-"*67)
			continue

	actualsignup(user,passwrd)

def login():

	progress()
	print("-"*67)
	v = False
	while v == False:
		try:
			user = input("   USERNAME:> ")
			v = True
		except:
			continue
	print("-"*67)
	v = False
	while v == False:
		try:
			passwrd = getpass.getpass("   PASSWORD:> ")
			v = True
		except:
			continue
	print("-"*67)

	actuallogin(user,passwrd)


def journal(u,p):
	
	username = encrypt(u,p)
	if platform.system() == "Linux":
		if 'ANDROID_STORAGE' in os.environ:
			os.chdir('/storage/emulated/0/pyjournal/%s' % username[0])
		else:
			os.chdir('%s/pyjournal/%s' % (os.path.expanduser('~'),username[0]))
	elif platform.system() == "Windows":
		os.chdir('C:/Users/%s/Documents/pyjournal/%s' % (os.getenv('username'),username[0]))
	else:
		os.chdir('%s/pyjournal/%s' % (os.path.expanduser('~'),username[0]))
	today = date.today()
	d = today.strftime("%d/%m/%Y")
	d = d.split("/")
	d = '.'.join(d)
	v = False
	while v == False:
		try:
			choice = input("@%s:> " % u)
			choice = choice.lower()
			choice = choice.strip()
			if choice == "entry":
				print("-"*67)
				entryin = input("  ENTRY:> ")
				print("-"*67)
				entry = open('%s.txt' % d,'a')
				encred = encrypt(entryin,p)
				entry.write("%s\n" % encred[0])
				entry.close()
				print("\n")
				continue
			elif choice == "check":
				q = False
				while q == False:
					try:
						print("-"*67)
						entrydate = input("   DATE (dd/mm/yyyy):> ")
						testdate = entrydate.split("/")
						_ = int(testdate[1])
						_ = int(testdate[2])
						q = True
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
						print("-"*67)
						print("> You entered an invalid date")
						print("-"*67)
						entrydate = input("   DATE (dd/mm/yyyy):> ")
				print("-"*67)
				entrydate = entrydate.replace('/','.')
				try:
					entry = open('%s.txt' % entrydate,'r')
				except:
					print("> ENTRIES DATED %s" % entrydate)
					print("-"*67)
					print("   No entries on this day")
					print("-"*67)
					print("\n")
					continue
				entryout = entry.readlines()
				out = ''
				for x in entryout:
					decred = decrypt(x,p)
					out += decred[0] + '\n    '
				out = out.strip()
				print("> ENTRIES DATED %s :" % entrydate)
				print("-"*67)
				print("    %s" % out)
				print("-"*67)
				entry.close()
				print("\n")
			elif choice == "login":
				print("-"*67)
				print("> You are already logged in")
				print("-"*67)
			elif choice == "signup":
				print("-"*67)
				print("> You already have a journal")
				print("-"*67)
			elif choice == "root":
				print("-"*67)
				print("> You have logged out")
				print("-"*67)
				inputchoice()
			elif choice == "list":
				listentries(u,p)
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
				print("-"*67)
				print("To proceed,enter any of the following commands:\n\n   entry: Adds a new entry to your journal for this day\n   check: Accepts date to check previous entries in your journal\n   root:  Go back to root\n   clear: Clears the screen\n   kill:  Exits pyJournal")
				print("-"*67)
			elif choice == "quit" or choice == "exit":
				print("-"*67)
				print("Use 'kill' to stop pyJournal")
				print("-"*67)
			elif choice == "":
				continue
			else:
				print("-"*67)
				print("'%s': Command not found. Type 'help' for more info" % choice)
				print("-"*67)
		except Exception as e:
			print(e)
			print("'%s': Command not found. Type 'help' for more info" % choice)
			continue


def listentries(u,p):

	encred = encrypt(u,p)
	user = encred[0]
	months = {'1':'January','2':'Feburary','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
	days = ""
	if platform.system() == "Linux":
		if 'ANDROID_STORAGE' in os.environ:
			os.chdir('/storage/emulated/0/pyjournal/%s' % user)
			files = os.listdir('/storage/emulated/0/pyjournal/%s' % user)
			if files == []:
				print("-"*67)
				print("> No Entries to be listed")
				print("-"*67)
				return 0
			print("-"*67)
			for month in months:
				for x in files:
					entry = x[:len(x)-4]
					try:
						entry = entry.split(".")
					except:
						continue
					if int(entry[1]) == int(month):
						days += "|" + str(entry[0]) + "|"
				if days != "":
					print("   %s:" % months[month],days)
				days = ""
			print("-"*67)
		else:
			os.chdir('%s/pyjournal/%s' % (os.path.expanduser('~'),user))
			files = os.listdir('%s/pyjournal/%s' % (os.path.expanduser('~'),user))
			if files == []:
				print("-"*67)
				print("> No Entries to be listed")
				print("-"*67)
				return 0
			print("-"*67)
			for month in months:
				for x in files:
					entry = x[:len(x)-4]
					try:
						entry = entry.split(".")
					except:
						continue
					if int(entry[1]) == int(month):
						days += "|" + str(entry[0]) + "|"
				if days != "":
					print("   %s:" % months[month],days)
				days = ""
			print("-"*67)
	elif platform.system() == "Windows":
		os.chdir('C:/Users/%s/Documents/pyjournal/%s' % (os.getenv('username'),user))
		files = os.listdir('C:/Users/%s/Documents/pyjournal/%s' % (os.getenv('username'),user))
		if files == []:
			print("-"*67)
			print("> No Entries to be listed")
			print("-"*67)
			return 0
		print("-"*67)
		for month in months:
			for x in files:
				entry = x[:len(x)-4]
				try:
					entry = entry.split(".")
				except:
					continue
				if int(entry[1]) == int(month):
					days += "|" + str(entry[0]) + "|"
			if days != "":
				print("   %s:" % months[month],days)
			days = ""
		print("-"*67)
	else:
		os.chdir('%s/pyjournal/%s' % (os.path.expanduser('~'),user))
		files = os.listdir('%s/pyjournal/%s' % (os.path.expanduser('~'),user))
		if files == []:
			print("-"*67)
			print("> No Entries to be listed")
			print("-"*67)
			return 0
		print("-"*67)
		for month in months:
			for x in files:
				entry = x[:len(x)-4]
				try:
					entry = entry.split(".")
				except:
					continue
				if int(entry[1]) == int(month):
					days += "|" + str(entry[0]) + "|"
			if days != "":
				print("   %s:" % months[month],days)
			days = ""
		print("-"*67)


def inputchoice():
		
	q = False
	while q == False:
		try:
			choice = input("@root:> ")
			choice = choice.lower()
			choice = choice.strip()
			if choice == "login":
				print("\n")
				login()
			elif choice == "signup":
				print("\n")
				signup()
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
				print("-"*67)
				print("To get started with pyjournal, type any of these commands:\n\n   login:  Enter your username and password to access your journal\n   signup: Enter a new username and password to create your journal\n   clear:  Clears the screen\n   kill:   Exits pyJournal")
				print("-"*67)
			elif choice == "":
				continue
			elif choice == "vineeth":
				print("-"*67)
				print("      Created from scratch with passion and elegance in mind")
				print("-"*67)
			elif choice == "quit" or choice == "exit":
				print("-"*67)
				print("Use 'kill' to stop pyJournal")
				print("-"*67)
			else:
				print("-"*67)
				print("'%s': Command not found. Type 'help' for more info" % choice)
				print("-"*67)
		except:
			print("-"*67)
			print("'%s': Command not found. Type 'help' for more info" % choice)
			print("-"*67)
			continue


print("-"*67)
print("[                      | pyJournal v3.0.1 |                         ]")
print("-"*67)
print("\n")


inputchoice()
