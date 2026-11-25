from collections import Counter

reviews = [
    "good product and good service",
    "good product and fast delivery",
    "fast delivery and good service"
]

words = " ".join(reviews).lower().split()

unigram = Counter(words)

bigram = Counter(zip(words, words[1:]))

print("Unigrams:", unigram)
print("Bigrams:", bigram)

word = input("Enter a word: ")

print("Following words:")

for (w1, w2), count in bigram.items():
    if w1 == word:
        print(w2, ":", count)
