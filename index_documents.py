import os
import json
import fitz  # PyMuPDF for handling PDFs
from elasticsearch import Elasticsearch, helpers
from dotenv import load_dotenv

load_dotenv()

es = Elasticsearch([{'host': os.getenv('ELASTICSEARCH_HOST'), 'port': os.getenv('ELASTICSEARCH_PORT')}])

def extract_text_from_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext == ".md" or ext == ".txt":
        return extract_text_from_text(file_path)
    elif ext == ".json":
        return extract_text_from_json(file_path)
    else:
        return None

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_text_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return json.dumps(data, indent=4)

def index_documents(index_name, documents):
    es.indices.create(index=index_name, ignore=400)
    actions = [{"_index": index_name, "_source": {"content": doc}} for doc in documents]
    helpers.bulk(es, actions)

def process_files_in_directory(directory):
    documents = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            text = extract_text_from_file(file_path)
            if text:
                documents.append(text)
    return documents

# Example usage
if __name__ == "__main__":
    root_directory = "./"  # Root directory of the project
    documents = process_files_in_directory(root_directory)
    index_documents("documents", documents)
    print(f"Indexed {len(documents)} documents.")
