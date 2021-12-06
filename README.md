# SyntaxLang
## Reserved Defined Words
| Word | Function                                          |
| :--- | :------------------------------------------------ |
| fo   | Terminates an adjective block                     |
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
An adjective block is a set of one or more adjective phrases joined together. This construction may immediately follow the noun or verb in noun and verb phrases respectively. An adjective block may be explicitly terminated using `fo`. This is often necessary when an adjective phrase formed through conversion is followed by another adjective phrase. For example:

```converter noun-phrase fo adjective```

If the `fo` in this example was omitted, the final adjective would become a part of the converted noun phrase's adjective block rather than the top-level adjective block.
