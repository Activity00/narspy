from storage.bag import Bag
from storage.memory import Memory


class Nars:

    def __init__(self):
        self.memory = Memory(Bag(1, 1, 1))

    def start(self):
        while True:
            self.memory.cycle()
