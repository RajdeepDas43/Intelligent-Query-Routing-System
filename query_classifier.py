from transformers import pipeline, BertForSequenceClassification, BertTokenizer
import torch

class QueryClassifier:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=4)

    def classify(self, query):
        inputs = self.tokenizer(query, return_tensors="pt")
        outputs = self.model(**inputs)
        probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
        label = torch.argmax(probabilities, dim=1)
        
        if label == 0:
            return "Simple Information Retrieval"
        elif label == 1:
            return "Contextual Information Retrieval"
        elif label == 2:
            return "General Query"
        elif label == 3:
            return "Hybrid Query"
        else:
            return "Complex Query"

# Example usage
if __name__ == "__main__":
    classifier = QueryClassifier()
    query = "What is the revenue of Google in 2023?"
    classification = classifier.classify(query)
    print(f"Query classified as: {classification}")
