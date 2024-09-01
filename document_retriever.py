from elasticsearch import Elasticsearch, helpers
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Elasticsearch client
es = Elasticsearch([{'host': os.getenv('ELASTICSEARCH_HOST'), 'port': os.getenv('ELASTICSEARCH_PORT')}])

def index_documents(index_name, documents):
    """
    Indexes a list of documents into Elasticsearch.
    
    Args:
        index_name (str): The name of the Elasticsearch index.
        documents (list): A list of document strings to index.
    """
    # Create the index with appropriate mappings if it doesn't exist
    es.indices.create(index=index_name, ignore=400, body={
        "mappings": {
            "properties": {
                "content": {
                    "type": "text",
                    "fields": {
                        "keyword": {"type": "keyword"}
                    }
                }
            }
        }
    })
    
    # Prepare actions for bulk indexing
    actions = [{"_index": index_name, "_source": {"content": doc}} for doc in documents]
    
    # Bulk index the documents
    helpers.bulk(es, actions)

def search_documents(index_name, query):
    """
    Searches for documents in the specified index that match the query.
    
    Args:
        index_name (str): The name of the Elasticsearch index.
        query (str): The search query string.
    
    Returns:
        list: A list of matching document contents.
    """
    # Perform a search query on the specified index
    response = es.search(
        index=index_name,
        body={
            "query": {
                "bool": {
                    "should": [
                        {"match": {"content": query}},
                        {"match": {"content": query, "boost": 0.5}}  # Query expansion
                    ]
                }
            }
        }
    )
    
    # Return the content of the matching documents
    return [hit['_source']['content'] for hit in response['hits']['hits']]

# Example usage
if __name__ == "__main__":
    # Example documents to index
    documents = [
        "Google's revenue in 2022 was $257 billion.",
        "Amazon's revenue in 2022 was $469 billion.",
        "Apple's revenue in 2022 was $365 billion."
    ]
    
    # Index documents
    index_name = "documents"
    index_documents(index_name, documents)
    print(f"Indexed {len(documents)} documents into the '{index_name}' index.")
    
    # Search for documents
    query = "Google's revenue in 2022"
    retrieved_docs = search_documents(index_name, query)
    print("Search Results:")
    for doc in retrieved_docs:
        print(f"- {doc}")
