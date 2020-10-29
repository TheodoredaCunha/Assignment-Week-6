#open original text file
file = open("story.txt", "r")
list_of_lines = file.readlines()
file.close()

#ask user for the name of the new file
#Will continue asking until the inputted value is valid
done = False
while not done:
	new_filename = input("New file name (make sure there is no other file in the folder with the same name): ")
	try:
		new_file = open("{}.txt".format(new_filename), "x")
		done = True
	except:
		print("That file name already exists")
		continue
#write in the new text file
#line_counter is used to number the lines
line_counter = 0
for i in list_of_lines:
	line_counter += 1
	new_file.write("{}. {}\n".format(line_counter, i))

new_file.close()



