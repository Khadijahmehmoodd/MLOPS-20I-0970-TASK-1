import unittest
from magic_square import generate_magic_square

class TestMagicSquare(unittest.TestCase):
    def test_generate_magic_square(self):
        # Test if the generated square is a 3x3 square
        magic_square = generate_magic_square()
        self.assertEqual(len(magic_square), 3)
        for row in magic_square:
            self.assertEqual(len(row), 3)

        # Test if the rows sum to the same value
        row_sum = sum(magic_square[0])
        for i in range(1, 3):
            self.assertEqual(sum(magic_square[i]), row_sum)

        # Test if the columns sum to the same value
        col_sum = sum(magic_square[i][0] for i in range(3))
        for j in range(1, 3):
            self.assertEqual(sum(magic_square[i][j] for i in range(3)), col_sum)

        # Test if the diagonals sum to the same value
        diag_sum1 = magic_square[0][0] + magic_square[1][1] + magic_square[2][2]
        diag_sum2 = magic_square[0][2] + magic_square[1][1] + magic_square[2][0]
        self.assertEqual(diag_sum1, diag_sum2)

        # Test if all numbers from 1 to 9 are present in the square
        all_numbers = set(range(1, 10))
        generated_numbers = set()
        for row in magic_square:
            generated_numbers.update(row)
        self.assertEqual(generated_numbers, all_numbers)

if __name__ == '__main__':
    unittest.main()
