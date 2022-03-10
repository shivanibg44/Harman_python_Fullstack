class car:

    def __init__(self,model,color,year):
        self.model=model
        self.color=color
        self.year=year


    def printdata(self):
        print(self.model)
        print(self.model)
        print(self.model)


    def getcustomer(self,name):
        self.name=name

    def printgetcustomer(self):
        print(self.name)


bmw=car("y series","white",2020)
audi=car("yseries","red",2020)


bmw.getcustomer("sumanth")
bmw.getcustomer()