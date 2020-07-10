"""
In NARS, a “concept” is an object that is uniquely named by a term,
and it contains the tasks and beliefs with that term as subject or predicate.
In this way, a concept is a data structure, or object (as in object-oriented
programming), that is both a unit of storage and a unit of processing.
All inference steps happen “locally” within concepts. This feature greatly
reduces the range of beliefs to be considered for a given task, and also
makes distributed implementation of NARS possible. It is perfectly fine to
run different concepts on different hardware devices, and let them cooperate
by exchanging tasks.
Since inference happens locally within concepts, so does the resource
competition among tasks and beliefs within a concept. Now we can specify
a concept Ct as a data structure that is named by term t, and consist of a
bag of tasks and a bag of beliefs, and the items of both bags are Narsese
sentences that have t as subject or predicate.
For example, the belief “robin → bird h1, 0.9i” is stored in concepts
Crobin and Cbird only. When question “robin → animal” is processed, it
only directly interacts with beliefs in Crobin and Canimal, but not with beliefs in Cwater or Cbird,
though the latter concept will probably be involved
indirectly, via a derived question like “bird → animal”.
We can talk about “the meaning of a concept” in a way that is parallel to
“the meaning of a term” — just like the meaning of term robin is determined
by its experienced relations with other terms (including bird), the meaning
of concept Crobin is determined by its experienced relations with other
concepts (including Cbird). The difference is just that a term is a symbol,
while a concept is a data structure named by a term.

"""
from entity import Item
from language.term import Term
from storage.bag import Bag


class Concept(Item):
    """
    Concept as defined by the NARS-theory
    Concepts are used to keep track of interrelated sentences
    """

    def __int__(self, term: Term):
        self.term = term  # The term is the unique ID of the concept
        self.beliefs = Bag()
        self.tasks = Bag()

    def get_a_belief(self):
        return self.beliefs.get()

    def get_a_task(self):
        return self.tasks.get()
