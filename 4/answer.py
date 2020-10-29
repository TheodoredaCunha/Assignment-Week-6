#student dictionaries
eren = {
  "name": "Eren",
  "homework": [90.0,97.0,75.0,92.0],
  "quizzes": [88.0,40.0,94.0],
  "tests": [75.0,90.0]
}
mikasa = {
 "name": "Mikasa",
 "homework": [100.0, 92.0, 98.0, 100.0],
 "quizzes": [82.0, 83.0, 91.0],
 "tests": [89.0, 97.0]
}

armin = {
"name": "Armin",
"homework": [0.0, 87.0, 75.0, 22.0],
"quizzes": [0.0, 75.0, 78.0],
"tests": [100.0, 100.0]
}


#list of students
student = [eren, mikasa, armin]

#printing student information
for person in student:
	print("name: {}".format(person["name"]))
	print("homework: {}".format(person["homework"]))
	print("quizzes: {}".format(person["quizzes"]))
	print("tests: {}".format(person["tests"]))
	print("\n")

#function to calculate the average of a list of numbers	
def average(numbers):
	total = sum(numbers)
	total = float(total)
	average = total / len(numbers)
	return average

#function to return the weighted average of a student's scores
def get_average(student):
	homework = average(student["homework"])
	quizzes = average(student["quizzes"])
	tests = average(student["tests"])
	weighted_average = homework*0.1 + quizzes*0.3 + tests*0.6
	return weighted_average
	
#function to return the letter grade of a score
def get_letter_grade(score):
	if score >= 90:
		return "A"
	elif 90 > score >= 80:
		return "B"
	elif 80 > score >= 70:
		return "C"
	elif 70 > score >= 60:
		return "D"
	else:
		return "F"
		
#testing the get_letter_grade() function with eren's info
print("Eren's letter grade is {}".format(get_letter_grade(get_average(eren))))

#function to return the class average (in numerical form)
def get_class_average(student):
	results = []
	for person in student:
		student_average = get_average(person)
		results.append(student_average)
		
	class_average = average(results)
	return class_average

#Printing the class average (numerical and letter form)
my_class_average = get_class_average(student)
my_class_average_letter = get_letter_grade(my_class_average)
print("\nThe class average in numerical form is {}".format(my_class_average))
print("The letter grade for the class average is {}".format(my_class_average_letter))