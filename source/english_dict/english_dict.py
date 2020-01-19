import json
import difflib

data = json.load(open("data.json"))

def search_word():
	word = input("Enter Word: ")
	close_words = difflib.get_close_matches(word, data.keys())
	c = 0
	if word.lower() in data.keys():
		for val in data.get(word.lower()):
			c += 1
			print ("Meaning %s:" % c,val)
	elif word.lower() not in data.keys():
		if len(close_words):
			print ("Did you mean? ", str(close_words)[1:-1])
			user_choice = input("Enter Y or N: ")
			if user_choice.lower() == "y":
				search_word()
			else:
				print ("Word doesn't exists!")
		else:		
			print ("Word doesn't exists!")

search_word()