q = False
while (q!=True):
	choicer = input("Do you want to Encode or Decode a message?\n")
	print("-"*40)
	choice = choicer.lower()
	choicer = choice.strip()
	if (choicer=="decode" or choicer=="encode"):
		q = True
		

# Creating list with common english words
eng = ["you","are","password","name","have","has","late","early","come","possible","secret","kill","call"]



# Based on user input, program encodes/decodes the message
if (choicer == 'decode'):
	cipherin= input("Enter the Encoded message: ")
	print("-"*40)
	
	h = False
	while h!=True: 
		try:
			shift = int(input("Enter Shift value (1-26).If shift is unknown, type 0: "))
		except ValueError:
			continue
		if shift < 26:
			h = True
		else:
			continue
			
	print("-"*40,"\n")
	cipher = cipherin.lower()
	ciplet = list(cipher)
	de = []
	alphabet = list(map(chr, range(97, 123)))
	
	# Takes each letter from user input and compares with the list of alphabets
	# If shift is given as 0, the program calculates and prints all the 25 shifts
	
	if shift!= 0:
		for x in ciplet:
			if x ==' ':
				de+=' '
			# Substitutes the letters in user input based on the shift value
			for y in alphabet:
				if x==y:
					de+= alphabet[(alphabet.index(y))-shift]
		dejoin = ''.join(de)
		dejoin = str(dejoin)
		decoded = dejoin.upper()
		print("The Decoded message:","\n")
		print(decoded,"\n")
		print("-"*40)
		print("Enjoy the Secrecy")
		print("-"*40)
		
	else:
		for t in range(1,26):
			for a in ciplet:
				if a==' ':
					de+=' '
				for b in alphabet:
					if a==b:
						de+= alphabet[(alphabet.index(b))-t]
			dejoin = ''.join(de)
			dejoin = str(dejoin)
			decoded = dejoin.upper()
			length = len(eng)
			
			#Checks for common english words in the decoded message
			for g in range(length):
				word = eng[g]
				wordup = word.upper()
				result = decoded.find(wordup)
				
				if (result!=-1):
					print("The Decoded message with shift","+",t,":","\n")
					print(decoded,"\n")
					de = []
					print("-"*40)
					print("Enjoy your secrecy")
					print("-"*40,"\n")
					exit(0)
					
				else:
					continue
			
			# If no common english words were found, the program prints all the 25 shifts
			if (result==-1):
				print("The Decoded message with shift","+",t,":","\n")
				print(decoded,"\n")
				de = []
				print("-"*40)
				print("-"*40,"\n")
				continue
				
		print("Enjoy your secrecy")
		print("-"*40)
		
		
		

elif (choicer == 'encode'):
	cipherin2= input("Enter the message: ")
	print("-"*20)
	
	m = False
	while m!=True: 
		try:
			shift2 = int(input("Enter Shift value (1-26): "))
		except ValueError:
			continue
		if shift2 < 26 and shift2 > 0:
			m = True
		else:
			continue
			
	print("-"*40)
	cipher2 = cipherin2.lower()
	ciplet2 = list(cipher2)
	de2 = []
	
	alphabet2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	
	if shift2!=0:
		for x in ciplet2:
			for y in alphabet2:
				if x==y:
					de2+= alphabet2[(alphabet2.index(y))+shift2]
		delen = len(de2)
		
		for i in range(delen):
			del de2[i:(i+1)]
		
		dejoin2 = ''.join(de2)
		dejoin2 = str(dejoin2)
		encoded = dejoin2.upper()
		print("The Encoded message:",encoded)
		print("-"*40)
		print("Enjoy the Secrecy")
		print("-"*40)	
