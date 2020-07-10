from typing import Dict

from entity import Item


class Bag:
    """A bag can contain items up to a constant maximum number."""

    def __init__(self, capacity: int = 10000):
        self.capacity = capacity
        self.items: Dict[str:Item] = {}

    def put(self, item: Item):
        """
        The given item is put into the bag. If there is already an item
        with the same key, the two are merged; if the bag already reaches its
        full maximum capacity, an item with the lowest priority is taken out of
        the bag to make space for the new item.
        """
        if item.key in self.items:
            self.items[item.key].merge(item)
        else:
            if len(self.items) > self.capacity:
                self.__take_out()

            self.items[item.key] = item

    def get(self, key=None):
        """A selected item is taken out of the bag, and the probability for an
           item to be selected is propositional to its priority value
        """
        if key:
            return self.items.pop(key, None)
        return self.__take_out()

    def __take_out(self):
        # TODO
        return None

    # def __take_out(self):
    #     if not self.name_table:
    #         return None
    #     if self._empty_level(self.current_level) or self.current_counter == 0:
    #         self.current_level = self.distributor.pick(self.level_index)
    #         self.level_index = self.distributor.next(self.level_index)
    #         while self._empty_level(self.current_level):
    #             self.current_level = self.distributor.pick(self.level_index)
    #             self.level_index = self.distributor.next(self.level_index)
    #
    #         if self.current_level < self.threshold_level:  # for dormant levels, take one item
    #             self.current_counter = 1
    #         else:
    #             self.current_counter = len(self.item_table[self.current_level()])
    #
    #     selected = self._take_out_first(self.current_level)
    #     belonging_level = self._get_level(selected)
    #     if self.current_level != belonging_level:
    #         self._into_base(selected)
    #         return self.take_out()
    #
    #     self.current_counter -= 1
    #     del self.name_table[selected.name()]
    #     return selected
    #
    # def _empty_level(self, level):
    #     return bool(self.item_table[level])
    #
    # def _take_out_first(self, current_level):
    #     selected = self.item_table[current_level].pop(0)
    #     self.mass = current_level + 1
    #     return selected
    #
    # def _get_level(self, item):
    #     fl = item.get_priority() * self.total_level
    #     level = int(math.ceil(fl) - 1)
    #     return 0 if level < 0 else level
    #
    # def _into_base(self, item):
    #     old_item = None
    #     in_level = self._get_level(item)
    #     if len(self.name_table) > self.capacity:
    #         out_level = 0
    #         while self._empty_level(out_level):
    #             out_level += 1
    #         if out_level > in_level:
    #             return item
    #         else:
    #             old_item = self._take_out_first(out_level)
    #
    #     self.item_table[in_level].append(item)
    #     self.mass += in_level + 1
    #     return old_item
