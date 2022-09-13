import unittest
from Room import Room


def find_helper(room, number, offset=0):
    try:
        current_box = room.get_numbered_box(number, offset).pointer
    except KeyError:
        return False, "ERROR " + str(number) + " was not found"
    for _ in range(room.number_of_boxes):
        if current_box == number:
            return True, str(number) + " was found by traveling in a size " + str(
                room.number_of_boxes) + " room."
        current_box = room.get_numbered_box(current_box, offset).pointer


def find_all_numbers_in_room(room, offset=0):
    for i in range(room.number_of_boxes):
        (res, msg) = find_helper(room, i, offset)
        if not res:
            return False, "ERROR " + str(i) + " was not found"
    return True, "all numbers found!"


class MyTestCase(unittest.TestCase):
    def test_is_number_5_reachable_in_a_10_room(self):
        (result, msg) = find_helper(Room(10), 5)
        self.assertEqual(True, result, msg)

    def test_is_number_6_reachable_in_a_10_room(self):
        (result, msg) = find_helper(Room(10), 6)
        self.assertEqual(True, result, msg)

    def test_is_number_7_reachable_in_a_10_room(self):
        (result, msg) = find_helper(Room(10), 7)
        self.assertEqual(True, result, msg)

    def test_is_number_7_reachable_in_a_1000_room(self):
        (result, msg) = find_helper(Room(1000), 7)
        self.assertEqual(True, result, msg)

    def test_is_number_7_reachable_in_a_10_room_with_2_offset(self):
        (result, msg) = find_helper(Room(10), 7, 2)
        self.assertEqual(True, result, msg)

    def test_is_number_11_reachable_in_a_10_room_with_0_offset(self):
        (result, msg) = find_helper(Room(10), 11, 0)
        self.assertEqual(False, result, msg)

    def test_is_number_11_reachable_in_a_10_room_with_12_offset(self):
        (result, msg) = find_helper(Room(10), 11, 12)
        self.assertEqual(False, result, msg)

    def test_all_numbers_of_a_room_with_size_10(self):
        (result, msg) = find_all_numbers_in_room(Room(10))
        self.assertEqual(True, result, msg)

    def test_all_numbers_of_a_room_with_size_100(self):
        (result, msg) = find_all_numbers_in_room(Room(100))
        self.assertEqual(True, result, msg)

    def test_all_numbers_of_a_room_with_size_1000(self):
        (result, msg) = find_all_numbers_in_room(Room(1000))
        self.assertEqual(True, result, msg)

    def test_all_numbers_of_a_room_with_size_10_and_offset_4(self):
        (result, msg) = find_all_numbers_in_room(Room(10), 4)
        self.assertEqual(True, result, msg)

    def test_all_numbers_of_a_room_with_size_100_and_offset_4(self):
        (result, msg) = find_all_numbers_in_room(Room(100), 4)
        self.assertEqual(True, result, msg)

    def test_all_numbers_of_a_room_with_size_1000_and_offset_4(self):
        (result, msg) = find_all_numbers_in_room(Room(1000), 4)
        self.assertEqual(True, result, msg)


if __name__ == '__main__':
    unittest.main()
