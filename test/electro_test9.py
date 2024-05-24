import unittest
from electro import calculate_distance, define_max_wire_length



class TestWireLength(unittest.TestCase):
    def test_calculate_distance(self):
        self.assertAlmostEqual(calculate_distance(2, 3), 3.61, places=2)
        self.assertAlmostEqual(calculate_distance(4, 5), 6.40, places=2)

    def test_define_max_wire_length(self):
        self.assertAlmostEqual(define_max_wire_length(2, [3, 3, 3]), 5.66, places=2)
        self.assertAlmostEqual(define_max_wire_length(100, [1, 1, 1, 1]), 300.00, places=2)
        self.assertAlmostEqual(define_max_wire_length(4, [100, 2, 100, 2, 100]), 396.32, places=2)
        self.assertAlmostEqual(define_max_wire_length(4,
                                                      [56, 18, 17, 94, 23, 7, 21, 94, 29, 54, 44, 26, 86, 79, 4, 15, 5,
                                                       91, 25, 17, 88, 66, 28, 2, 95, 97, 60, 93, 40, 70, 75, 48, 38,
                                                       51, 34, 52, 87, 8, 62, 77, 35, 52, 3, 93, 34, 57, 51, 11, 39,
                                                       72]), 2738.18, places=2)