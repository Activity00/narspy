"""
# 1. get a concept from the memory
# 2. get a task from concept
# 3. get a belief from concept
# 4. derive new tasks from the selected task and belief
# 5. put the involved items back into the corresponding bags
# 6. put the new tasks into the corresponding bags
"""


def select_concept_for_inference(memory):
    # 1. get a concept from the memory
    concept = memory.concepts.get()
    if not concept:
        return

    # 2. get a task from concept
    task = concept.get_a_task()
    # 3. get a belief from concept
    belief = concept.get_a_belief()

    # 4. derive new tasks from the selected task and belief
    if task.is_judgement():
        pass
    else:  # is a question
        pass

    # 5. put the involved items back into the corresponding bags

    # 6. put the new tasks into the corresponding bags


def fire_concept(nal):
    pass
