def Relaxometer(mode):

    print("Operate this First ")

    def innermeter(a, b):
        print(a)
        print(b)
        return mode(a, b)  # this only getting the parameters in the given input.
    return innermeter  # this only returns the outside of the given value in the given output.

@Relaxometer
def Music(a, b):
    print(a + b)

Music(21, 14)

