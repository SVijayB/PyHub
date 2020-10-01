import unittest
import MainClass




class MainClassTest(unittest.TestCase):

    def test_add(self):
        mainc = MainClass()
        self.assertEqual((1+1),mainc.adding(1,1)


if __name__ == '__main__':
    unittest.main()