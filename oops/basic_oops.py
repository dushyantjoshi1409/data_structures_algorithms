
# You are tasked with designing a class Student that stores and displays information about students.
# The class must have the following :
# Attributes :
# name (string) : Stores the name of the student.
# rollNumber (int) : Stores the roll number of the student
# Methods :
# setDetails (String name, int rollNumber) : This method initializes the attributes name and rollNumber with the values provided by the user.
# displayDetails() : This method prints the details of the student in following format (The output consist of two separate lines) :
# Your code goes here
class Student:
    def __init__(self):
        self.name = ""
        self.rollNumber = 0
    
    def setDetails(self, name, rollNumber):
        self.name = name
        self.rollNumber = rollNumber
    
    def displayDetails(self):
        print("Name :", self.name)
        print("Roll Number :", self.rollNumber)
