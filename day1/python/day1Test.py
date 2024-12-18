from main import part1, part2
import unittest

class day1(unittest.TestCase):

    def test_part1(self):
        fp = "../input.txt"
        result = part1(fp)
        print(result)
        self.assertIsInstance(result,int,"Resultatet är inte ett heltal!")
        self.assertGreaterEqual(result,0,"Resultatet är inte större än 0")
    
    def test_part2(self):
        fp = "../input.txt"
        result = part2(fp)
        print(result)
        self.assertIsInstance(result,int,"Resultatet är inte ett heltal!")
        self.assertGreaterEqual(result,0,"Talet är 0 eller mindre!")
