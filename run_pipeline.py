from query_classifier import QueryClassifier
from context_manager import ContextManager
from document_retriever import retrieve_documents
from response_generator import generate_response

def run_pipeline(user_id, query):
    classifier = QueryClassifier()
    context_manager = ContextManager()
    
    # Step 1: Classify the query
    classification = classifier.classify(query)
    print(f"Query classified as: {classification}")
    
    # Step 2: Retrieve context (if needed)
    if classification in ["Contextual Information Retrieval", "Hybrid Query"]:
        context = context_manager.get_context(user_id, query)
    else:
        context = None
    
    # Step 3: Retrieve documents (if needed)
    if classification in ["Simple Information Retrieval", "Contextual Information Retrieval", "Hybrid Query"]:
        retrieved_docs = retrieve_documents(query)
    else:
        retrieved_docs = []
    
    # Step 4: Generate response
    response = generate_response(retrieved_docs, query)
    print(f"Generated Response: {response}")
    
    # Step 5: Store context for future use
    context_manager.add_context(user_id, response)

if __name__ == "__main__":
    user_id = 'user123'
    query = "What is the revenue of Google in 2023?"
    run_pipeline(user_id, query)
