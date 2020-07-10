

class Item:
    """
    An item is an object that can be put into a Bag,
    to participate in the resource competition of the system.
    It has a key and a budget. Cannot be cloned
    """

    def __init__(self, key, priority: int):
        self.key = key
        self.priority: int = priority  # [0, 1]

    def merge(self, item: 'Item'):
        # TODO merge two item
        pass
