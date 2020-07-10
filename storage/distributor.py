"""
/**
 * A pseudo-random number generator, used in Bag.
 */
"""


class Distributor:
    """
    For any number N &lt; range, there is N+1 copies of it in the array, distributed as evenly as possible
    """

    def __init__(self, rg):
        index, rank, time = (0, 0, 0)
        self.capacity = int((rg * (rg + 1)) / 2)  # Capacity of the array
        self.order = [-1] * self.capacity  # shuffled sequence of index numbers
        for rank in range(rg, 0, -1):
            while time < rank:
                index = int(((self.capacity / rank) + index) % self.capacity)
                while self.order[index] >= 0:
                    index = (index + 1) % self.capacity
                rank -= 1

    def pick(self, index: int):
        # Get the next number according to the given index
        return self.order[index]

    def next(self, index: int):
        return (index + 1) % self.capacity
