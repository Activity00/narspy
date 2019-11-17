from abc import abstractmethod

from entity.budgetvalue import BudgetValue


class Item:
    """
    An item is an object that can be put into a Bag,
    to participate in the resource competition of the system.
    It has a key and a budget. Cannot be cloned
    """

    def __init__(self, name, budget: BudgetValue = None):
        self.name = name
        self.budget = budget

    @abstractmethod
    def name(self):
        pass

    @property
    def priority(self):
        return self.budget.priority

    @priority.setter
    def priority(self, value: float):
        self.budget.priority = value

    def inc_priority(self, v):
        self.budget.inc_priority(v)

    def dec_priority(self, v):
        self.budget.dec_priority(v)
