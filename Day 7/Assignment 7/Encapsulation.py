class Prime:

    def __init__(self, password):
        self.__password = password

    def viewPassword(self):
        print(self.__password)

    def changingPassword(self, password):
        self.__password = password   # this must be same as we given in the initialisation part of the variable,
                                     # that can be privately accessed. like example:
                                     #  *** password *** is commonly used in the encap method.

accessing = Prime(7787)
accessing.viewPassword()

accessing.__password = 9087
accessing.viewPassword()     # outer side can't change the inner value that can be protected.

accessing.changingPassword(3476)   # it is used in inside of the given value of the private value can be accessed.
accessing.viewPassword()