import unittest

from Prisoner import Prisoner
from Room import Room


class SinglePrisonerSearchInRoom100Seed3NoOffset(unittest.TestCase):
    def test_Prisoner_7_with_offset_0(self):
        p = Prisoner(7, 0)
        (result, _) = p.search_own_box(Room(100, 3), -1)
        self.assertEqual(result, True)

    def test_Prisoner_43_with_offset_0(self):
        p = Prisoner(43, 0)
        (result, _) = p.search_own_box(Room(100, 3), -1)
        self.assertEqual(result, True)

    def test_Prisoner_56_with_offset_0(self):
        p = Prisoner(56, 0)
        (result, _) = p.search_own_box(Room(100, 3), -1)
        self.assertEqual(result, True)

    def test_Prisoner_102_with_offset_0(self):
        p = Prisoner(102, 0)
        (result, _) = p.search_own_box(Room(100, 3), -1)
        self.assertEqual(result, False)

    def test_Prisoner_0_with_offset_0(self):
        p = Prisoner(0, 0)
        (result, _) = p.search_own_box(Room(100, 3), -1)
        self.assertEqual(result, True)

    def test_Prisoner_neg_1_with_offset_0(self):
        p = Prisoner(-1, 0)
        (result, _) = p.search_own_box(Room(100, 3), -1)
        self.assertEqual(result, False)


class SinglePrisonerSearchInRoom100Seed3Offset8(unittest.TestCase):
    def test_Prisoner_7_with_offset_8(self):
        p = Prisoner(7, 8)
        (result, _) = p.search_own_box(Room(100, 3), -1)
        self.assertEqual(result, True)

    def test_Prisoner_43_with_offset_8(self):
        p = Prisoner(43, 8)
        (result, _) = p.search_own_box(Room(100, 3), -1)
        self.assertEqual(result, True)

    def test_Prisoner_56_with_offset_8(self):
        p = Prisoner(56, 8)
        (result, _) = p.search_own_box(Room(100, 3), -1)
        self.assertEqual(result, True)

    def test_Prisoner_102_with_offset_8(self):
        p = Prisoner(102, 8)
        (result, _) = p.search_own_box(Room(100, 3), -1)
        self.assertEqual(result, False)

    def test_Prisoner_0_with_offset_8(self):
        p = Prisoner(0, 8)
        (result, _) = p.search_own_box(Room(100, 3), -1)
        self.assertEqual(result, True)

    def test_Prisoner_neg_1_with_offset_8(self):
        p = Prisoner(-1, 8)
        (result, _) = p.search_own_box(Room(100, 3), -1)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
