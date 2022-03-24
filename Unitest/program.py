import unittest

class Myapp2(unittest.TestCase):
    def test_case3(self):
        self.assertEqual("hello","hello")

class MyApp(unittest.TestCase):

    def test_case1(self):
        a=10
        b=20
        c=a+b
        self.assertEqual(32,c) #(a+b,c)


    def test_case2(self):
        self.assertNotEqual("hello","hai")



if __name__ == "__main__":
    unittest()
