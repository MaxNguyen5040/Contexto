from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased-finetuned-sst-2-english")

def compare_texts(text1, text2):
    inputs = tokenizer(text1, text2, return_tensors="pt", max_length=512, truncation=True)
    logits = model(**inputs).logits
    return torch.argmax(logits, dim=1).item()

# Usage example
similarity_score = compare_texts("This is sentence 1.", "This is sentence 2.")
print(f"Similarity Score: {similarity_score}")