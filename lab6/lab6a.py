#!/usr/bin/env python3
# Author ID: skhanal15

class Student:

    # Define the name and number when a student object is created
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.courses = {}

    # Return student name and number
    def displayStudent(self):
        return 'Student Name: ' + str(self.name) + '\n' + 'Student Number: ' + str(self.number)

    # Add a new course and grade
    def addGrade(self, course, grade):
        self.courses[course] = grade

    # Return GPA
    def displayGPA(self):
        if len(self.courses) == 0:
            return 'GPA of student ' + self.name + ' is 0.0'

        gpa = 0.0
        count = 0

        for grade in self.courses.values():
            gpa += grade
            count += 1

        if count == 0:
            return 'GPA of student ' + self.name + ' is 0.0'

        return 'GPA of student ' + self.name + ' is ' + str(gpa / count)

    # Return list of passed courses
    def displayCourses(self):
        passed = []

        for course in self.courses:
            if self.courses[course] > 0.0:
                passed.append(course)

        return passed


if __name__ == '__main__':

    # Student 1
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Student 2
    student2 = Student('Jessica', '123456')
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())
