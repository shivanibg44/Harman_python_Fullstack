
class student:
    def _init_(self,name,Rollno,Admno,college):
        self.name=name
        self.Rollno=Rollno
        self.Admno=Admno
        self.college=college

    def show(self):
        print(self.name)
        print(self.Rollno)
        print(self.Admno)
        print(self.college)

class Exam(student):
    def _init_(self,name,Rollno,Admno,college,examname,engmark,mathmark,phymark,chemark):
        self.examname=examname
        self.engmark=engmark
        self.mathmark=mathmark
        self.phymark=phymark
        self.chemark=chemark

        student._init_(self,name,Rollno,Admno,college)

    def show1(self):
        print(self.name)
        print(self.Rollno)
        print(self.Admno)
        print(self.college)
        print(self.examname)
        print(self.engmark)
        print(self.mathmark)
        print(self.chemark)

obj=Exam("sumanth","123","567","ace","sem","89","89","90","87")
obj.printshow1()