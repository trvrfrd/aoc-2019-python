import unittest
from part1 import fuel_requirement
from part2 import total_fuel_requirement


class TestFuelRequirement(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(fuel_requirement(12), 2)

    def test_example2(self):
        self.assertEqual(fuel_requirement(14), 2)

    def test_example3(self):
        self.assertEqual(fuel_requirement(1969), 654)

    def test_example4(self):
        self.assertEqual(fuel_requirement(100756), 33583)


class TestTotalFuelRequirement(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(total_fuel_requirement(14), 2)

    def test_example2(self):
        self.assertEqual(total_fuel_requirement(1969), 966)

    def test_example3(self):
        self.assertEqual(total_fuel_requirement(100756), 50346)


if __name__ == "__main__":
    unittest.main()
