class government:
    def __init__(self):
        self.__price=100

    def viewpetrolprice(self):
        print(self.__price)

    def hikeprice(self,price):
        self.__price=price


centralgovernment=government()
centralgovernment.viewpetrolprice()


centralgovernment.__price=130
centralgovernment.viewpetrolprice()

centralgovernment.hikeprice(120)
centralgovernment.viewpetrolprice()