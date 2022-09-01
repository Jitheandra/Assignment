studentweightlist = list()  # creating an empty list for students weight
n = int(input("Enter no of students: "))  # To read input from user for no of students
for i in range(n):
    studentweight = float(input("Enter weight of student " + str(i+1) + ": "))  # To get weight of student from user
    studentweightlist.append(studentweight * 0.454)  # To convert weight from lbs to kilogram.
a = ['%.2f' % elem for elem in studentweightlist]  # converting the values not more than 2 precision values
print(a)
