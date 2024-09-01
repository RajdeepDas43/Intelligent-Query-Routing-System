from sentence_transformers import SentenceTransformer, util
import numpy as np

class ContextManager:
    def __init__(self):
        self.model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
        self.context_store = {}

    def add_context(self, user_id, context):
        if user_id not in self.context_store:
            self.context_store[user_id] = []
        self.context_store[user_id].append(context)

    def get_context(self, user_id, current_query):
        if user_id in self.context_store:
            contexts = self.context_store[user_id]
            query_embedding = self.model.encode(current_query, convert_to_tensor=True)
            context_embeddings = self.model.encode(contexts, convert_to_tensor=True)
            similarities = util.pytorch_cos_sim(query_embedding, context_embeddings)
            best_context_idx = np.argmax(similarities)
            return contexts[best_context_idx]
        return None

# Example usage
if __name__ == "__main__":
    context_manager = ContextManager()
    context_manager.add_context(user_id='user123', context='Google revenue in 2022 was $257 billion')
    current_context = context_manager.get_context(user_id='user123', current_query='What about 2023?')
    print(f"Retrieved context: {current_context}")
