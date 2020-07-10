from language.term import Term


class TrueValue:
    """Truth is a tuple of frequency and confidence as defined by NARS theory"""
    TRUTH_TRUE = Term("TRUE")
    TRUTH_FALSE = Term("FALSE")
    TRUTH_UNSURE = Term("UNSURE")

    def __init__(self, frequency: float, confidence: float, is_analytic: bool = False):
        self.frequency = frequency  # frequency factor of the truth value
        self.confidence = confidence  # confidence factor of the truth value

        self.analytic = is_analytic  # Whether the truth value is derived from a definition

    @property
    def true_value(self):
        return self.frequency, self.confidence

    def __eq__(self, other):
        if not isinstance(other, TrueValue):
            return False
        return self.frequency == other.frequency and self.confidence == other.confidence
