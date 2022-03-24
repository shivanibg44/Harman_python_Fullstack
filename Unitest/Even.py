import unittest

def check_even_or_odd(x):
    if x%2==0:
        return "even"
    else:
        return "odd"

class MyEvenorOdd(unittest.TestCase):

    def test_case_even_or_odd1(self):
        result = check_even_or_odd(2)
        self.assertEqual("even",result)

    def test_case_even_or_odd2(self):
        result = check_even_or_odd(5)
        self.assertEqual("odd",result)


if __name__ == "__main__":
    unittest.main()