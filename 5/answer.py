import re

def find_hapax(storyname):
	#The story I chose is "Jack Manly" by James Grant
	story = open(storyname, "r")
	words = story.read()

	#splitting the story into a list of individual words
	list_of_words = re.split("\n| |--|-|_|__|/|$|%|;|:", words.lower())

	#cleaning up words in the list and seperating repeating words from hapax words
	cleaned_words_list = []
	repeated_words = []
	for word in list_of_words:
		cleaned_word = ""
		for character in word:
			#getting rid of unwanted characters in each word
			if character not in ".,\"\'?!()":
				cleaned_word += character
		#testing wether or not a word have appeared more than once
		if cleaned_word not in cleaned_words_list and cleaned_word not in repeated_words:
			cleaned_words_list.append(cleaned_word)
		else:
			try:
				cleaned_words_list.remove(cleaned_word)
				repeated_words.append(cleaned_word)
			except:
				repeated_words.append(cleaned_word)
	#printing a list filled with hapax words
	print(cleaned_words_list)

#if the cmd is not in the directory of the text file, the user must include the directory in the input
storyname = input("Text file name (include directory if cmd not already in the right directory):")
find_hapax(storyname)