import unittest
from query_classifier import QueryClassifier

class TestQueryClassifier(unittest.TestCase):

    def setUp(self):
        self.classifier = QueryClassifier()

    def test_classification(self):
        query = "What is the revenue of Google in 2023?"
        result = self.classifier.classify(query)
        self.assertIn(result, ["Simple Information Retrieval", "Contextual Information Retrieval", "General Query", "Hybrid Query", "Complex Query"])

if __name__ == "__main__":
    unittest.main()
