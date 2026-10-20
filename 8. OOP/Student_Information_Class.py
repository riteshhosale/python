class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll)
        print("Marks:", self.marks)

s = Student("Ritesh", 1, 85)
s.display()