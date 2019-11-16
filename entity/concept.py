"""
concepts are used to keep track of interrelated sentences
"""
from entity.item import Item


class Concept(Item):
    """
    Concept as defined by the NARS-theory
    Concepts are used to keep track of interrelated sentences
    """

    def __int__(self, budget_value, term: 'Term'):
        self.budget_value = budget_value
        self.term = term  # The term is the unique ID of the concept
