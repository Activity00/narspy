from functools import reduce


def inference_or(*values):
    product = 1
    for v in values:
        product *= (1-v)
    return 1 - product


def inference_and(*values):
    product = 1
    for v in values:
        product *= v
    return
