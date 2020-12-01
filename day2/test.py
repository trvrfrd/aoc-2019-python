import unittest
from part1 import run_intcode_program


class TestRunIntcodeProgram(unittest.TestCase):
    def test_example1(self):
        program = [1, 0, 0, 0, 99]
        result = run_intcode_program(program)
        self.assertEqual(result, [2, 0, 0, 0, 99])

    def test_example2(self):
        program = [2, 3, 0, 3, 99]
        result = run_intcode_program(program)
        self.assertEqual(result, [2, 3, 0, 6, 99])

    def test_example3(self):
        program = [2, 4, 4, 5, 99, 0]
        result = run_intcode_program(program)
        self.assertEqual(result, [2, 4, 4, 5, 99, 9801])

    def test_example4(self):
        program = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        result = run_intcode_program(program)
        self.assertEqual(result, [30, 1, 1, 4, 2, 5, 6, 0, 99])


if __name__ == "__main__":
    unittest.main()
