from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

class TextComparisonModel:
    def __init__(self, model_name="bert-base-uncased-finetuned-sst-2-english"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)

    def compare_texts(self, text1, text2):
        inputs = self.tokenizer(text1, text2, return_tensors="pt", max_length=512, truncation=True)
        logits = self.model(**inputs).logits
        similarity_score = torch.argmax(logits, dim=1).item()
        return similarity_score

# Example usage
model = TextComparisonModel()
similarity_score = model.compare_texts("Hi I'm coding for hack club", "hackc lub arcade is cool")
print(f"Similarity Score: {similarity_score}")
