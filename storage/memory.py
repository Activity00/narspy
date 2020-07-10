from control import general_inference
from storage.bag import Bag


class Memory:
    def __init__(self, concepts: Bag):
        self.concepts = concepts

    def cycle(self):
        general_inference.select_concept_for_inference(self)
