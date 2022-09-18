class Prisoner:
    def __init__(self, number, offset=0):
        self.number = number
        self.offset = offset
        self.has_own_number = False

    def search_own_box(self, room, start_box_number):
        if self.number > room.number_of_boxes or self.number < 0:
            return False, room.number_of_boxes + 1
        if start_box_number == -1:
            start_box_number = (self.number + self.offset) % room.number_of_boxes
        current_box = room.boxes[start_box_number]
        for i in range(room.number_of_boxes):
            if current_box.pointer == self.number:
                return True, i + 1
            current_box = room.get_next_box(current_box, self.offset)
        return False, room.number_of_boxes + 1



