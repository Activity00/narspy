class Term:
    """
    Term is the basic component of Narsese, and the object of processing in NARS.

    A Term may have an associated Concept containing relations with other Terms.
    It is not linked in the Term, because a Concept may be forgot while the Term
    exists. Multiple objects may represent the same Term.
    """
    atoms = {}  # {string: Term}

    def __init__(self, name):
        self.name = name

    def get(self, name):
        term = self.atoms.get(name)
        if term:
            return term

