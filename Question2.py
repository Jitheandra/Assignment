dog = dict()  # Create an empty dictionary:dog
dog["Name"] = "Jarvis"  # To add name to the dog
dog["Color"] = "Black"  # To add color to the dog
dog["Breed"] = "Bulldog"  # To add breed name to the dog
dog["Legs"] = 4  # To add no of legs to the dog
dog["Age"] = 5  # To add age to the dog
print(dog)  # To print dog

student = dict()  # Create an empty dictionary student
student["First_name"] = "Thala"  # To add first name to the student
student["Last_name"] = "Ajith"  # To add last name to the student
student["Gender"] = "Male"  # To add gender to the student
student["Marital status"] = "Married"  # To add marital status to the student
student["Skills"] = ["Actor", "Pilot", "Car Racer"]  # To add skills to the student
student["Country"] = "India"  # To add country to the student
student["Address"] = "Chennai"  # To add address to the student
print(student)  # To print student
print(len(student))  # To print length of student
print(student["Skills"])  # To get skills of student
print(type(student["Skills"]))  # To get type of skills of student
student["Skills"].extend(["Bike Racer", "Chef"])  # To modify skills of student
print(student["Skills"])  # To print student skills after modifying
print(student.keys())  # To get keys of student dictionary as list
print(student.values())  # To get values of student dictionary as list
