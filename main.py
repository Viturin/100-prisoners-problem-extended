from Prisoner import Prisoner
from Room import Room

if __name__ == '__main__':
    b = Room(50, 2)
    b.travel()
    print(b)
    p = Prisoner(1)
    print(p.search_own_box(b, -1))


