import string
import random
from pprint import pprint

vowels = 'aeiou'
illegal_consonants = 'wqy'
consonants = string.ascii_lowercase.translate(
    str.maketrans('', '', vowels + illegal_consonants))
letters = vowels + consonants
illegal_lasts = 'rh'
last_replacements = consonants.translate(
    str.maketrans('', '', illegal_consonants))


def add_char(partial):
    if partial == '':
        return random.choice(random.choice([consonants, vowels]))
    if partial[-1] in vowels:
        return partial + random.choice(consonants)
    elif partial[-1] in consonants:
        return partial + random.choice(vowels)
    else:
        raise Exception('Can\'t add character')


def generate_word():
    def generator(chars_remaining, partial):
        if chars_remaining < 1:
            return partial
        else:
            new = add_char(partial)
            return generator(chars_remaining - 1, new)

    length = random.randrange(2, 9)
    word = generator(length, '')
    if word[-1] in illegal_lasts:
        word = word[:-1] + random.choice(last_replacements)
    return word


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
