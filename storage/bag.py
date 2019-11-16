from typing import List, Dict


class Bag:
    name_table: Dict[object: object] = {}  # mapping from key to item
    item_table: List[List[object]] = []  # array of lists of items, for items on different level
    current_counter: int = 0  # maximum number of items to be taken out at current level
    current_level: int = 0 # index to get next level, kept in individual objects
    # shared DISTRIBUTOR that produce the probability distribution
    @classmethod
    def tack_out(cls):
        if not Bag.name_table:
            return None
        if cls._empty_level(Bag.current_level) or Bag.current_counter == 0:
            Bag.current_level =

    @classmethod
    def _empty_level(cls, level):
        return bool(cls.item_table[level])
