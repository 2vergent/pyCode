import nltk
from nltk.corpus import wordnet
from googletrans import Translator

synonyms = []
antonyms = []

s = input("Do you want to Translate or Dictionary or Compare two words? \n")

if s == "t":
	lang = input("Enter Language code: ")
	word = input("Enter your sentence: ")
	translator = Translator()
	translated = translator.translate(word, dest=lang)	
	print("Translation: ",translated.text)

elif s == "d":
	word = input("Enter your word to get more info on it: ")
	
	for syn in wordnet.synsets(word):
		for l in syn.lemmas():
			synonyms.append(l.name())
			if l.antonyms():
				antonyms.append(l.antonyms()[0].name())

				
	print("\n")
	d = syn.definition()
	print("DEFINITION: ",d.capitalize())
	
	print("\n")
	expressions = syn.examples()
	print("EXPRESSIONS: ")
	c = 1
	for x in expressions:
		print("   ",c,"."," ",x.capitalize(),sep='')
		c+= 1
	
	print("\n")
	c = 1
	print("SYNONYMS: ")
	for x in set(synonyms):
		x = x.replace('_',' ')
		print("   ",c,"."," ",x.capitalize(),sep='')
		c+= 1
		
	print("\n")
	c = 1
	print("ANTONYMS: ")
	if len(antonyms)!= 0:
		for x in set(antonyms):
			print("   ",c,"."," ",x.capitalize(),sep='')
			c+= 1
	else:
		print("   ","Sorry, I couldn't find any antonyms for",word)

elif s == "c":
	 word1 = input("Enter first word: ")
	 word2 = input("Enter second word: ")
	 w1 = wordnet.synset('%s.n.01' % word1)
	 w2 = wordnet.synset('%s.n.01' % word2)
	 print(w1.path_similarity(w2))	