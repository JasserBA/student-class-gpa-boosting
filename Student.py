import math
class Student :

    def __init__(self, firstName, lastName, gender, year, gpa):
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.year = year
        self.gpa = gpa
    
    def setFirstName(self,firstName):
        self.firstName = firstName
    
    def getFirstName(self):
        return self.firstName
    
    def setLastName(self,lastName):
        self.lastName = lastName
    
    def getLastName(self):
        return self.lastName
    
    def setGender(self,gender):
        self.gender = gender
    
    def getGender(self):
        return self.gender
    
    def setYear(self,year):
        self.year = year
    
    def getYear(self):
        return self.year
    
    def setGpa(self,gpa):
        self.gpa = gpa
    
    def getGpa(self):
        return self.gpa 
    
    def student_study_time(self, study_time):
        if (self.getGpa() + math.log(study_time)) <= 4.0 :
            self.setGpa(self.getGpa() + math.log(study_time))

    def show_student(self):
        print('Student First Name: ', self.getFirstName(), "\nLast Name: ", self.getLastName(), "\nGender: ", self.getGender(), "\nYear: ", self.getYear(), "\nGPA: ", self.getGpa())

student_GPA = [None] * 5

student_GPA[0] = Student("Ja", "Ba", "Male", "first-year student", 0.0)
student_GPA[1] = Student("Ja", "Bab", "Male", "sophomore", 3.0)
student_GPA[2] = Student("Ja", "Babd", "Male", "junior", 1.0)
student_GPA[3] = Student("Ja", "Baddall", "Male", "senior", 3.0)
student_GPA[4] = Student("Ja", "Babdallah", "Male", "junior", 2.0)

for i in range(5):
    study_time = float(input("Study Time (minutes = [30, 60, 90, 120, 180]) ? => "))
    student_GPA[i].student_study_time(study_time)
    student_GPA[i].show_student()
