file = open("text.txt", "r")
lines = file.read()
current_line = ""

lowercase = "abcdefghijklmnopqrstuvwxyz"

#splitting the text into a list
list = lines.split(". ")
delete_later = []
for i in range(len(list) - 1):
	list[i] = list[i] + "."

for i in range(len(list) - 1):
	#checking if sample titles got separated
	if len(list[i]) <= 4:
		list[i + 1]  = list[i] + " " + list[i + 1]
		delete_later.append(i)
	
	#checking if period is supposed to be part of a word instead of a separator
	if list[i][0] in lowercase:
		list[i - 1] = list[i - 1] + " " + list[i]
		delete_later.append(i)

#printing the text line by line
for i in range(len(list)):
	if i not in delete_later:
		print(list[i])
	
file.close()