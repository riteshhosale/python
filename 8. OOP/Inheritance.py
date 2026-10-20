class Person:
    def display(self):
        print("This is the parent class")

class Student(Person):
    def show(self):
        print("This is the child class")

s = Student()
s.display()
s.show()