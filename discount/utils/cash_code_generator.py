import random

from discount.utils.constants import ALL_CHARACTERS


def generate():
    return 'boki9@*csh' + ''.join(random.sample(ALL_CHARACTERS, 8))
