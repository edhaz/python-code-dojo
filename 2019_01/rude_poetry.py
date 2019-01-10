import json
import random
import re

def censor(word):
    vowels = 'aeiouAEIOU'
    for letter in word:
        if letter in vowels:
            return word.replace(letter, '*', 1)

rude_words = json.load(open('rude_words.json', 'r'))

poems = open('poems.txt', 'r')
poems_text = poems.read()
poems_text = re.sub('[0-9]','', poems_text)

poems_split = poems_text.split('\n\n')


random_poem = random.choice(poems_split)
random_poem_split = random_poem.split(' ')

for i in range(5):
    rand_word_position = random.randint(0,len(random_poem_split)-1)
    rand_word = random_poem_split[rand_word_position]
    while '\n' in rand_word:
        rand_word_position = random.randint(0,len(random_poem_split)-1)
        rand_word = random_poem_split[rand_word_position]
    
    rude_word = random.choice(rude_words)
    random_poem_split[rand_word_position] = censor(rude_word)

new_poem = " ".join(random_poem_split)


print(new_poem)
