from PyDictionary import PyDictionary
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from collections import defaultdict
import itertools

class TextComparisonModel:
    def __init__(self, model_name="bert-base-uncased"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.dictionary = PyDictionary()

    def compare_texts(self, text1, text2):
        inputs = self.tokenizer(text1, text2, return_tensors="pt", max_length=512, truncation=True)
        logits = self.model(**inputs).logits
        similarity_score = torch.argmax(logits, dim=1).item()
        return similarity_score

    def get_word_definition(self, word):
        definition = self.dictionary.meaning(word)
        return definition

    def calculate_word_similarity(self, words):
        similarity_scores = defaultdict(dict)
        word_pairs = list(itertools.combinations(words, 2))

        for word1, word2 in word_pairs:
            similarity_scores[word1][word2] = self.compare_texts(word1, word2)
            similarity_scores[word2][word1] = similarity_scores[word1][word2]

        return similarity_scores

model = TextComparisonModel()
words = ["apple", "orange", "banana", "pear", "grape"]
similarity_scores = model.calculate_word_similarity(words)
print(similarity_scores)