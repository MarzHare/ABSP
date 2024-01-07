# Count the number of times a character appears in a sentence
import pprint

sentence = input("Sentence: ")
count = {}

for character in sentence:
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)
