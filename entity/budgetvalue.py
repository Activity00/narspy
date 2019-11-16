class BudgetValue:
    """
    A triple of priority (current), durability (decay), and quality (long-term average).
    """
    def __init__(self, priority, durability, quality):
        self.priority = priority
        self.durability = durability
        self.quality = quality

    def __str__(self):
        return f'priority({self.priority}) durability({self.durability}) quality({self.quality})'
