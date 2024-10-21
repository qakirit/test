
#7) Find the count of occurrences of each word in a sentence.
from collections import Counter

# Get input sentence from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Count occurrences of each word
word_counts = Counter(words)

# Print the counts
print("Occurrences of each word:", dict(word_counts))
