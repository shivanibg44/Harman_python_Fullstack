class person(object):
    def __init__(self,name,adhar,phone):
        self.name=name
        self.adhar=adhar
        self.phone=phone


    def displaydetails(self):
        print(self.name+"\n"+self.adhar+"\n"+self.phone)

class employee(person):

    def __init__(self,name,adhar,phone,email,tax):
        self.email=email
        self.tax=tax

        person.__init__(self,name,adhar,phone)

    def printdetails(self):
        print("name=",self.name)
        print("adhar=",self.adhar)
        print("phone=",self.phone)
        print("email=",self.email)
        print("tax=",self.tax)


x=employee("sumanth",1234,9677312849,"sumath@gmail.com",55)
x.printdetails()


