import random
import itertools
from pprint import pprint
import chars

consonant_firsts = [''.join(i) for i in itertools.product(
    chars.consonants, chars.vowels)]
vowel_firsts = [''.join(i) for i in itertools.product(
    chars.vowels, chars.last_replacements)]
all = consonant_firsts + vowel_firsts
print(random.choice(all))
