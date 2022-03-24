import unittest

def check_divisibleby7(x):
    if(x%7==0):
        return True
    else:
        return False

class CheckDivisible(unittest.TestCase):
    def check_divisible1(self):
        result = check_divisibleby7(14)
        self.assertTrue(result)

    def check_divisible2(self):
        result = check_divisibleby7(2)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()