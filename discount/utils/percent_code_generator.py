import random

from discount.utils.constants import ALL_CHARACTERS


def generate():
    return 'bkino#*prcnt' + ''.join(random.sample(ALL_CHARACTERS, 8))
