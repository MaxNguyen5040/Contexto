from PyDictionary import PyDictionary

class TextComparisonModel:
    def __init__(self, model_name="bert-base-uncased-finetuned-sst-2-english"):
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

# Example usage
model = TextComparisonModel()
similarity_score = model.compare_texts("This is sentence 1.", "This is sentence 2.")
print(f"Similarity Score: {similarity_score}")

word_definition = model.get_word_definition("example")
print(f"Definition of 'example': {word_definition}")