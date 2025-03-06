"""
Given any input_word, return what the next word will be based on the occurrences of words following the input_word in a training text ("corpus"). 

Example corpus
corpus = 'The sky is blue and this water is blue and the grass is green.'

Given this corpus, if we input "is" into the solution, the output should be "blue" 2/3 of the time and "green" the other 1/3.
"""

from collections import defaultdict, Counter
import re
import random

"""
O(n) to build the model
O(k) for sampling, where k is the number of the next words for a candidate
Space: O(n) -- dict 
clean the corpus: lowercase and remove punctuation
build model:
for each word, create an entry: clean word from the corpus: Counter{next_word: its frequency}
finally, clean up the candidate
take care of the edge case when the candidate isn't in the corpus of words at all 
extract the list of possible next words and their corresponding weights (i.e., frequencies).
The random.choices function is used to select the next word based on these weights.

Test it by running this thing many times and eyeballing the distribution of the results 
"""

def preprocess(text):
    # Convert to lowercase and remove punctuation (keeping apostrophes)
    text = text.lower()
    text = re.sub(r'[^\w\s\']', '', text)
    return text

def build_model(corpus: str) -> dict:
    """
    Build a dictionary where each key is a word and the value is a Counter of the words that follow it.
    """
    clean_text = preprocess(corpus)
    words = clean_text.split()
    model = defaultdict(Counter)
    
    # Count occurrences of each following word
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        model[current_word][next_word] += 1
        
    return model

def predict_next_word_prob(model: dict, input_word: str) -> str:
    """
    Given an input word, return the next word based on the probability distribution
    derived from the training corpus. If the input word is not found, returns None.
    """
    input_word = input_word.lower()
    if input_word not in model:
        return None
    
    next_words = model[input_word]
    words = list(next_words.keys())
    weights = list(next_words.values())
    # random.choices selects one element based on the given weights
    predicted = random.choices(words, weights=weights, k=1)[0]
    return predicted

# Example usage:
if __name__ == "__main__":
    corpus = 'The sky is blue and this water is blue and the grass is green.'
    model = build_model(corpus)
    
    input_word = "is"
    # Run the prediction several times to see the distribution
    results = [predict_next_word_prob(model, input_word) for _ in range(1000)]
    
    # Calculate frequencies of predicted words
    freq = Counter(results)
    print("Prediction frequencies for the word 'is':")
    for word, count in freq.items():
        print(f"{word}: {count/1000:.2f}")
