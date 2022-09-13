import numpy as np
from Box import Box


class Room:
    def __init__(self, number_of_boxes: int, seed=None):
        self.nodes_view = None
        self.boxes_per_cycle = None
        self.boxes = dict()
        self.number_of_boxes = number_of_boxes
        np.random.seed(seed)
        permutations = list(np.random.permutation(number_of_boxes))
        for i in range(number_of_boxes):
            self.boxes[i] = Box(i, permutations[i])

    def travel(self):
        self.boxes_per_cycle = list()
        self.nodes_view = list()
        for box in self.boxes.values():
            current_box = box
            current_num = 0
            current_node_view = ""
            while not current_box.visited:
                current_node_view += "-->" + str(current_box.value) + "[" + str(current_box.pointer) + "]"
                current_num += 1
                current_box.visited = True
                current_box = self.get_next_box(current_box)
            if current_num != 0:
                self.boxes_per_cycle.append(current_num)
                self.nodes_view.append(current_node_view)


    def get_next_box(self, box, travel_offset=0):
        return self.boxes[(box.pointer + travel_offset) % self.number_of_boxes]

    def get_numbered_box(self, number, travel_offset=0):
        if number >= self.number_of_boxes:
            raise KeyError
        return self.boxes[(number + travel_offset) % self.number_of_boxes]
