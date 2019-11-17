import math
from typing import List, Dict, Any

from storage.distributor import Distributor


class Bag:

    def __init__(self, total_level: int, capacity: int, threshold_level: int):
        self.total_level = total_level  # priority levels
        self.capacity = capacity  # defined in different bags
        self.threshold_level = threshold_level  # firing threshold

        # array of lists of items, for items on different level
        self.item_table: List[List[Any]] = [[] for _ in range(self.capacity)]
        self.name_table = {}  # mapping from key to item
        self.current_level = self.total_level - 1  # current take out level
        self.level_index = self.capacity % self.total_level  # index to get next level, kept in individual objects
        self.current_counter: int = 0  # maximum number of items to be taken out at current level
        self.mass: int = 0
        self.distributor = Distributor(self.total_level)

    def take_out(self):
        if not self.name_table:
            return None
        if self._empty_level(self.current_level) or self.current_counter == 0:
            self.current_level = self.distributor.pick(self.level_index)
            self.level_index = self.distributor.next(self.level_index)
            while self._empty_level(self.current_level):
                self.current_level = self.distributor.pick(self.level_index)
                self.level_index = self.distributor.next(self.level_index)

            if self.current_level < self.threshold_level:  # for dormant levels, take one item
                self.current_counter = 1
            else:
                self.current_counter = len(self.item_table[self.current_level()])

        selected = self._take_out_first(self.current_level)
        belonging_level = self._get_level(selected)
        if self.current_level != belonging_level:
            self._into_base(selected)
            return self.take_out()

        self.current_counter -= 1
        del self.name_table[selected.name()]
        return selected

    def _empty_level(self, level):
        return bool(self.item_table[level])

    def _take_out_first(self, current_level):
        selected = self.item_table[current_level].pop(0)
        self.mass = current_level + 1
        return selected

    def _get_level(self, item):
        fl = item.get_priority() * self.total_level
        level = int(math.ceil(fl) - 1)
        return 0 if level < 0 else level

    def _into_base(self, item):
        old_item = None
        in_level = self._get_level(item)
        if len(self.name_table) > self.capacity:
            out_level = 0
            while self._empty_level(out_level):
                out_level += 1
            if out_level > in_level:
                return item
            else:
                old_item = self._take_out_first(out_level)

        self.item_table[in_level].append(item)
        self.mass += in_level + 1
        return old_item
