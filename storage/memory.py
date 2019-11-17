import time

from storage.bag import Bag


class Memory:
    def __init__(self, concepts: Bag):
        self.concepts = concepts

    def cycle(self):
        # 1. get a concept from the memory
        concept = self.concepts.take_out()
        if not concept:
            return
        concept.task_links = 1
        # 2. get a task from concept
        task = concept.get_task()
        # 3. get a belief from concept
        belief = concept.get_belief()
        # 4. derive new tasks from the selected task and belief

        # 5. put the involved items back into the corresponding bags

        # 6. put the new tasks into the corresponding bags

        # current_concept = memory.concepts.tack_out()
        # nal = DerivationContext(current_concept)
        # use current concept (current concept is the resource)
