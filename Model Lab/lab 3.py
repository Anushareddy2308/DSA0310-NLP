import nltk
from nltk import CFG

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the' | 'a'
N -> 'passenger' | 'ticket' | 'flight'
V -> 'books' | 'checks'
""")

parser = nltk.ChartParser(grammar)

sentence = input("Enter sentence: ").lower().split()

try:
    trees = list(parser.parse(sentence))

    if trees:
        for tree in trees:
            print(tree)
            tree.pretty_print()
    else:
        print("Invalid sentence")

except ValueError:
    print("Invalid sentence")
