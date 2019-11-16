class ProcessTask:
    @staticmethod
    def process_task(concept, cont, task):
        return None


class DerivationContext:
    def __int__(self, concept):
        self.concept = concept

    def set_current_task(self, task):
        pass

    def set_current_term(self, term):
        pass

    def set_current_concept(self, budget):
        pass

    def get_current_concept(self):
        pass


def select_concept_for_inference(memory: 'Memory'):
    current_concept = memory.concepts.tack_out()
    nal = DerivationContext(current_concept)
    # use current concept (current concept is the resource)


class Memory:

    def __int__(self):
        self.concepts = Bag()  # Dict[Concept: Term]

    def cycle(self):
        # 1. get a concept from the memory
        concept = self.concepts.tack_out()
        if not concept:
            return

        concept.task_links =
        # 2. get a task from concept
        task = concept.get_task()
        # 3. get a belief from concept
        belief = concept.get_belief()
        # 4. derive new tasks from the selected task and belief

        # 5. put the involved items back into the corresponding bags

        # 6. put the new tasks into the corresponding bags

        current_concept = memory.concepts.tack_out()
        nal = DerivationContext(current_concept)
        # use current concept (current concept is the resource)


class Nars:

    def __init__(self):
        self.memory = Memory()

    def start(self):
        while True:
            self.memory.cycle()
