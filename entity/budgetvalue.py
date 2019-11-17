from inference.utility_functions import inference_or, inference_and


class BudgetValue:
    """
    A triple of priority (current), durability (decay), and quality (long-term average).
    """

    def __init__(self, priority: float, durability: float, quality: float):
        self._priority = priority
        self._durability = durability
        self._quality = quality

    def __str__(self):
        return f'priority({self.priority}) durability({self.durability}) quality({self.quality})'

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, v):
        if v > 1.0:
            raise ValueError(f'priority value ({v}) must <= 1.0.')
        self._priority = v

    def dec_priority(self, v):
        self._priority = inference_and(self._priority, v)

    def inc_priority(self, v):
        self._priority = min(1.0, inference_or(self._priority, v))
