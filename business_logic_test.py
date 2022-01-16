import unittest
import business_logic
import math


class CalcMatrixAdd(unittest.TestCase):
    def setUp(self) -> None:
        self.matrix = [
            # a , b , expected
            [0, 10, 0 + 10],  # 0. Integer numbers
            [0.1, 0.2, 0.1 + 0.2],  # 0. Float
            [0.1, 1, 0.1 + 1],  # 0. Integer and Float
            [1, 0.1, 1 + 0.1],  # 0. Float and Integer
            [-1, 10, -1 + 10],  # 0. Negative + Positive
            [1, -10, 1 - 10],  # 0. Positive + Negative
        ]

    def test_matrix(self):
        for test in self.matrix:
            a, b, expected = test[0], test[1], test[2]
            self.assertEqual(business_logic.add(a, b), expected, f'a:{a}, b:{b}, expected:{expected}')


class CalcMatrixSubstract(unittest.TestCase):
    def setUp(self) -> None:
        self.matrix = [
            # a , b , expected
            [0, 10, 0 - 10],  # 0. Integer numbers
            [0.1, 0.2, 0.1 - 0.2],  # 0. Float
            [0.1, 1, 0.1 - 1],  # 0. Float and Integer
            [1, 0.1, 1 - 0.1],  # 0. Integer and Float
            [-1, 10, -1 - 10],  # 0. Negative and Positive
            [1, -10, 1 - (-10)],  # 0. Positive and Negative
        ]

    def test_matrix(self):
        for test in self.matrix:
            a, b, expected = test[0], test[1], test[2]
            self.assertEqual(business_logic.substract(a, b), expected, f'a:{a}, b:{b}, expected:{expected}')


class CalcMatrixMultiply(unittest.TestCase):
    def setUp(self) -> None:
        self.matrix = [
            # a , b , expected
            [3, 4, 12],  # 0. Integer
            [0.3, 4, 0.3 * 4],  # 0. Float
            [3, 0.4, 3 * 0.4],  # 0. Integer and Float
            [-3, -4, 12],  # 0. Negative
            [3, -4, -12],  # 0. Positive and Negative
            [0, 15, 0],  # 0. Multiply zero
        ]

    def test_matrix(self):
        for test in self.matrix:
            a, b, expected = test[0], test[1], test[2]
            self.assertEqual(business_logic.multiply(a, b), expected, f'a:{a}, b:{b}, expected:{expected}')


class CalcMatrixDivision(unittest.TestCase):
    def setUp(self) -> None:
        self.matrix = [
            # a , b , expected
            [3, 5, 3 / 5],  # Integer
            [0.3, 0.5, 0.3 / 0.5],  # Float
            [3, 0.5, 3 / 0.5],  # Integer and Float
            [3, 5, 3 / 5],  # Positive
            [-3, -5, -3 / (-5)],  # Negative
            [3, -5, 3 / (-5)],  # Positive and Negative
            [0, 0.5, 0],  # Zero divide on float
            [0, 0, -1],  # Zero division
        ]

    def test_matrix(self):
        for test in self.matrix:
            a, b, expected = test[0], test[1], test[2]
            self.assertEqual(business_logic.divide(a, b), expected, f'a:{a}, b:{b}, expected:{expected}')


class CalcMatrixMod(unittest.TestCase):
    def setUp(self) -> None:
        self.matrix = [
            # a , b , expected
            [20, 11, 9],  # Integer
            [20, 11, 4 + 5],  # Positive
            [-20, -11, -9],  # Negative
            [20, -11, -2],  # Positive and Negative
            [0, 11, 0]  # Zero mod

        ]

    def test_matrix(self):
        for test in self.matrix:
            a, b, expected = test[0], test[1], test[2]
            self.assertEqual(business_logic.mod(a, b), expected, f'a:{a}, b:{b}, expected:{expected}')


class CalcMatrixLog(unittest.TestCase):
    def setUp(self) -> None:
        self.matrix = [
            # a , b , expected
            [10, 10, 1],  # Integer
            [20, 10, 1.301029995663981],  # Positive

        ]

    def test_matrix(self):
        for test in self.matrix:
            a, b, expected = test[0], test[1], test[2]
            self.assertEqual(business_logic.log(a, b), expected, f'a:{a}, b:{b}, expected:{expected}')


class CalcMatrixExp(unittest.TestCase):
    def setUp(self) -> None:
        self.matrix = [
            # a , b , expected
            [11, 10, 11 ** 10],  # 0. Integer numbers
            [11, -10, 11 ** (-10)],  # 0. Positive and Negative
            [-11, 10, (-11) ** 10],  # 0. Negative and Positive

        ]

    def test_matrix(self):
        for test in self.matrix:
            a, b, expected = test[0], test[1], test[2]
            self.assertEqual(business_logic.exp(a, b), expected, f'a:{a}, b:{b}, expected:{expected}')


class CalcSmokeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.a = 10
        self.b = 11

    def test_add(self):
        self.assertEqual(business_logic.add(self.a, self.b), self.a + self.b)

    def test_substract(self):
        self.assertEqual(business_logic.substract(self.a, self.b), self.a - self.b)

    def test_multiply(self):
        self.assertEqual(business_logic.multiply(self.a, self.b), self.a * self.b)

    def test_divide(self):
        self.assertEqual(business_logic.divide(self.a, self.b), self.a / self.b)

    def test_mod(self):
        self.assertEqual(business_logic.mod(self.a, self.b), self.a % self.b)

    def test_exp(self):
        self.assertEqual(business_logic.exp(self.a, self.b), self.a ** self.b)

    def test_average(self):
        self.assertEqual(business_logic.average(self.a, self.b), (self.a + self.b) / 2)

    def test_log(self):
        self.assertEqual(business_logic.log(self.a, self.b), math.log(self.a, self.b))


class NegativeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.a = 10
        self.b = 11

    def test_divide(self):
        self.assertEqual(business_logic.divide(self.a, 0), -1)


if __name__ == '__main__':
    unittest.main()
