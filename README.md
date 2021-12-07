# SyntaxLang
## Phonological Features
This list is incomplete and currently contains only the consonant pronunciations that are not always consistent with English
- `c` is pronounced as `/tʃ/` (the `ch` sound in `chip`)
- `g` is pronounced as `/g/` (the `g` sound in `glass`)
- `x` is pronounced as `/ʒ/` (the `g` sound in `genre`)
- `j` is pronounced as `/dʒ/` (the `j` sound in `jar`)


## Reserved Defined Words
| Word | Function                                          |
| :--- | :------------------------------------------------ |
| fo   | Terminates a noun phrase or verb phrase           |
| tu   | Converts an adjective block or sentence to a noun |
| to   | Terminates 'tu'                                   |

## Word Classes for Undefined Words
| Word Class | Description                                                             |
| :--------- | :---------------------------------------------------------------------- |
| Noun       | A thing                                                                 |
| Verb       | An action, state, or occurrence                                         |
| Adjective  | A descriptor of a noun or verb                                          |
| Modifier   | A word modifying an adjective                                           |
| Converter  | Converts a noun to an adjective that conveys a relationship to the noun |

## List of Syntactic Constructions
### Adjective Phrase
An adjective phrase conveys a single attribute or relationship of a noun or verb. It can come in either of the following forms, both of which optionally end with a single modifier.

```adjective (modifier)```

```converter noun-phrase (modifier)```

### Adjective Block
An adjective block is a set of one or more adjective phrases joined together. This construction may immediately follow the noun or verb in noun and verb phrases respectively. When an adjective block contains an adjective phrase formed through conversion followed by another adjective phrase, it is necessary to use `fo` to explicitly terminate the noun phrase being converted. If `fo` is omitted, the adjective phrase that follows will instead bind to the adjective block of the converted noun phrase. Here are some examples with the boundaries of adjective blocks and phrases shown using square brackets and parentheses respectively.

```[(adjective) (adjective)]```

```[(adjective modifier) (adjective)]```

```[(converter noun-phrase fo) (adjective)]```

```[(converter noun-phrase [adjective])]```

### `tu` Conversion
The reserved word `tu` can be used to form more abstract nouns from either an adjective block or grammatical sentence. Sentences contained within a `tu` conversion are not required to have a subject noun phrase. The construction is terminated with `to` to prevent ambiguity.

```tu adjective-block to```

```tu noun-phrase verb-phrase to```

```tu verb-phrase to```

### Noun Phrase
A noun phrase consists of a noun and optionally an adjective block describing it. The noun may be a single word from the noun word class or a noun formed through `tu` conversion.

```noun```

```noun adjective-block```

### Verb Phrase
A verb phrase consists of a verb, an optional adjective block, and an optional noun phrase expressing the verb's object. The components must appear in that order.

```verb```

```verb adjective-block```

```verb adjective-block noun-phrase```

```verb noun-phrase```

### Sentence
A sentence consists of a noun phrase expressing the subject followed by a verb phrase expressing the predicate.
```noun-phrase verb-phrase.```
