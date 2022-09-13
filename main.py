from Room import Room

if __name__ == '__main__':
    b = Room(10, 1)
    b.travel()
    print(b.boxes_per_cycle)
    print(b.nodes_view)


