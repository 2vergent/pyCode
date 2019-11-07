from tkinter import *
import random as r

master = Tk()
master.config(background='black')


w = Canvas(master, width=2000, height=1000,background='#202020')
w.grid()


labelstr = Label(w, text="PASSWORD GENERATOR",width=40,height=2,pady=10,background='#2f4f4f',fg='white')
labelstr.grid(pady=60)

Strength = StringVar(master)
Strength.set("Choose Password Strength")	

opstr = OptionMenu(w, Strength, "Weak", "Strong", "Stronger", "Strongest")
opstr.grid(pady=10)

ch = ""
def ok():
    global ch 
    ch = Strength.get()
    ch = ch.lower()
	
button_strength = Button(w, text="OK", width=10,pady=20,borderwidth=8,relief='raised',activebackground='white', command=ok)
button_strength.grid(pady=60)

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alpharep = alpha.copy()
num = ['1','2','3','4','5','6','7','8','9','0']
numrep = num.copy()
spechar = ['@','@','#','#','&','&','$','$','_','_','!','!','?','?','/','/','*','*',':',':','%','%','[',']','{','}','(',')','<','>','+','+']
specharep = spechar.copy()

length = IntVar(master)
length.set("Choose Password Length")

oplen = OptionMenu(w, length, 1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)
oplen.grid(pady=20)

passlength = 0
def ok1():
	global passlength
	passlength = length.get()
	password()

button_length = Button(w, text="OK", width=10,pady=20,borderwidth=8,relief='raised',activebackground='white', command=ok1)
button_length.grid(pady=60)

def password():
	l = len(alpha + alpharep + num + spechar)
	pwd =[]
	r.shuffle(alpha)
	r.shuffle(alpharep)
	r.shuffle(num)
	r.shuffle(numrep)
	r.shuffle(spechar)
	r.shuffle(specharep)
	print(ch)
	if ch=="weak":
		pwd = alpha + alpharep
	elif ch=="strong":
		pwd = alpha + alpharep + num + numrep
	elif ch=="stronger":
		pwd = alpha + alpharep + spechar + specharep
	elif ch=="strongest":
		pwd = alpha + alpharep + num + numrep + spechar + specharep
	r.shuffle(pwd)
	z = False
	while(z!=True):
		pwd.pop()
		l2 = len(pwd)
		if (l2==passlength):
			z =True
		else:
			continue
	pwd = ''.join(pwd)
	pwd = pwd.upper()
	pwd = pwd.replace('',' ')
	pwd = pwd.strip()
	a = Label(master, text=pwd, width=40,borderwidth=20, height=2, relief='groove')
	a.grid()

master.mainloop()
