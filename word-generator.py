import string
import random
from pprint import pprint

vowels = 'aeiou'
illegal_consonants = 'wqy'
consonants = string.ascii_lowercase.translate(
    str.maketrans('','', vowels + illegal_consonants)
)
letters = vowels + consonants
illegal_lasts = 'rh'
last_replacements = consonants.translate(str.maketrans('','', illegal_consonants))

def add_char(partial):
    if partial == '':
        return random.choice(letters)
    if partial[-1] in vowels:
        return partial + random.choice(consonants)
    elif partial[-1] in consonants:
        return partial + random.choice(vowels)
    else:
        raise Exception('Can\'t add character')

def generate_word(partial=''):
    new = add_char(partial)
    if len(new) > 5:
        if new[-1] in illegal_lasts:
            new = new[:-1] + random.choice(last_replacements)
        return new
    else:
        return generate_word1(new)

def word_class(word):
    classes = [
        'noun',
        'verb',
        'adjective',
        'modifier',
        'converter',
    ]
    return classes[hash(word) % len(classes)]

words = [generate_word() for _ in range(10)]
table = [(i, word_class(i)) for i in words]

pprint(table)
