import string

vowels = 'aeiou'
illegal_consonants = 'wqy'
consonants = string.ascii_lowercase.translate(
    str.maketrans('', '', vowels + illegal_consonants))
letters = vowels + consonants
illegal_lasts = 'rh'
last_replacements = consonants.translate(
    str.maketrans('', '', illegal_consonants))
