class Box:
    def __init__(self, value: int, pointer: int):
        self.pointer = pointer
        self.value = value
        self.visited = False
