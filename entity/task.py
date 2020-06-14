from entity.budgetvalue import BudgetValue
from entity.sentence import Sentence


class Task:
    """
    A task to be processed, consists of a Sentence and a BudgetValue.
    A task references its parent and an optional causal factor (usually an Operation instance).
    These are implemented as WeakReference to allow forgetting via the
    garbage collection process.  Otherwise, Task ancestry would grow unbounded,
    violating the assumption of insufficient resources (AIKR).
    """

    def __init__(self, sentence: Sentence, parent_belief: BudgetValue, best_solution: Sentence, name):
        self.sentence = sentence
        self.parent_belief = parent_belief
        self.best_solution = best_solution

