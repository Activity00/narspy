import time

from storage.bag import Bag
from storage.memory import Memory


class Nars:

    def __init__(self):
        self.memory = Memory(Bag())

    def start(self):
        while True:
            self.memory.cycle()
            time.sleep(0.01)
