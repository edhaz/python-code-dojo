import json
import random

rude_words = json.load(open('rude_words.json', 'r'))

poems = open('poems.txt', 'r')
poems_text = poems.read()
poems_split = poems_text.split('\n\n')

random_poem = random.choice(poems_split)
random_poem_split = random_poem.split(' ')

        

print(random_poem_split)
