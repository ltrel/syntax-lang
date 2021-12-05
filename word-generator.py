import random
from pprint import pprint
import chars


def add_char(partial):
    if partial == '':
        return random.choice(random.choice([chars.consonants, chars.vowels]))
    if partial[-1] in chars.vowels:
        return partial + random.choice(chars.consonants)
    elif partial[-1] in chars.consonants:
        return partial + random.choice(chars.vowels)
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
    if word[-1] in chars.illegal_lasts:
        word = word[:-1] + random.choice(chars.last_replacements)
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
