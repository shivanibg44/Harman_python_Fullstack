class student:
    def __init__(self,name,rollnum,admnum,college):
        self.name=name
        self.rollnum=rollnum
        self.admnum=admnum
        self.college=college


    def printdata(self):
        print(self.name)
        print(self.rollnum)
        print(self.admnum)
        print(self.year)

student1=student(input("enter the student name:"),
                 input("enter the rollnum:"),
                 input("enter the student admnum:"),
                 input("enter the student college:"))



student1.printdata