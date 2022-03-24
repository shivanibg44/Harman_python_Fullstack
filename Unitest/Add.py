import unittest

def add(x,y):
    return x+y

class Myapp(unittest.TestCase):
    def test_case_add(self):
        a = 10
        b = 20
        c= add(a,b)
        self.assertEqual(a+b,c)

    def test_case_add1(self):
        a = 12.5
        b = 13.5
        c = add(a,b)
        self.assertEqual(a+b,c)

    def test_case_add2(self):
        a = -12
        b = -13
        c = add(a,b)
        self.assertEqual(a+b,c)

if __name__ == "__main__":
    unittest.main()









