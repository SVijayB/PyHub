import unittest

class MainClass:
    def adding(self,num1,num2):
        return num1+num2

    def subtracting(self,num1,num2):
        return num1-num2


class UnitTesting(unittest.TestCase):

    def test_add(self):
        mainc = MainClass()
        self.assertEqual((1+1),mainc.adding(1,1)


if __name__ == '__main__':
    unittest.main()