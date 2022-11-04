from unittest import TestCase, main
from Z1_E import treu


class Z1ETest(TestCase):
    def test511(self):
        self.assertEqual(treu(5, 1, 1), 0)

    def test444(self):
        self.assertEqual(treu(4, 4, 4), 2)

    def test466(self):
        self.assertEqual(treu(4, 6, 6), 2)

    def test42_1(self):
        self.assertEqual(treu(4, 2, -1), 1)

    def test45_2(self):
        self.assertEqual(treu(4, 5, -2), 2)

    def test4_14(self):
        self.assertEqual(treu(4, -1, 2), 1)

    def test40_2(self):
        self.assertEqual(treu(4, 0, -2), 1)

    def test8_24(self):
        self.assertEqual(treu(8, -2, 4), 1)

    def test8_25(self):
        self.assertEqual(treu(8, -2, 5), 3)


if __name__ == '__main__':
    main()
