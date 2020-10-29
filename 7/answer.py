import re

f = open("story.txt", "r")
text = f.read()

cleaned_words_list = []
for word in re.split("\n| ", text):
	cleaned_word = ""
	for character in word:
		if character not in ".,?!$%()*[]{}\/":
			cleaned_word += character
	cleaned_words_list.append(len(cleaned_word))
	
average_word_length = sum(cleaned_words_list)/len(cleaned_words_list)
print(average_word_length)
	