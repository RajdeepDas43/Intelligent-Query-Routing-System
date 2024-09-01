# **Complex Retrieval-Augmented Generation (RAG) Architecture**

## **Overview**

This project implements a sophisticated Retrieval-Augmented Generation (RAG) system, designed to handle complex queries by combining information retrieval with text generation. The architecture is capable of managing different types of queries, retrieving relevant documents from diverse collections, generating context-aware responses, and continuously improving through a feedback loop.

### **Key Features:**

- **Multi-Stage Query Classification:** Classifies queries into simple, contextual, general, hybrid, or complex.
- **Context Management:** Maintains and retrieves user-specific context to enhance query understanding.
- **Document Retrieval:** Uses both keyword and semantic search to retrieve relevant documents.
- **Response Generation:** Utilizes pre-trained language models to generate accurate and contextually relevant responses.
- **Continuous Learning:** Integrates a feedback loop to refine models and improve performance over time.

## **Architecture**

### **1. Query Input and Preprocessing**
- **User Interface:** Captures user queries via an API or chat interface.
- **Text Normalization:** Preprocesses input by normalizing text, extracting entities, and detecting intent.

### **2. Query Classification**
- **Multi-Stage Classifier:** Classifies queries into categories for appropriate handling.
- **Collection Routing:** Directs queries to the correct document collection.

### **3. Context Management**
- **Session and Persistent Context:** Tracks and retrieves session-specific and long-term user context.
- **Contextual Embeddings:** Generates embeddings for dynamic context management.

### **4. Document Retrieval**
- **Search Engine Integration:** Uses ElasticSearch or FAISS for retrieving documents based on query type.
- **Relevance Scoring:** Ranks documents using TF-IDF, BM25, or neural-based scoring.

### **5. Response Generation**
- **Direct and Hybrid Generation:** Generates responses using pre-trained models, optionally combining retrieval results.
- **Post-Processing:** Validates and formats the generated responses for final output.

### **6. Feedback and Learning**
- **Continuous Learning Loop:** Refines the system using user feedback and model retraining.
- **Data Management:** Stores feedback for future model improvements and error analysis.
.

### **Flowchart: Retrieval-Augmented Generation (RAG) System**

```plaintext
+------------------+
| User Query Input |
+------------------+
        |
        v
+----------------------+
| Query Preprocessing  |
| - Tokenization       |
| - Entity Recognition |
| - Spell Check        |
+----------------------+
        |
        v
+---------------------------+
| Query Classification      |
| - Simple Retrieval        |
| - Contextual Retrieval    |
| - General Query           |
| - Hybrid/Complex Query    |
+---------------------------+
        |
        v
+----------------------------------+
|          Context Manager         |
| - Retrieve Previous Context      |
| - Add New Context                |
| - Generate Contextual Embeddings |
+----------------------------------+
        |
        v
+------------------------------+
|    Document Retriever        |
| - Search Indexed Documents   |
| - Relevance Scoring          |
| - Retrieve Relevant Docs     |
+------------------------------+
        |
        v
+--------------------------------------+
|  Response Generation (OpenAI GPT-4) |
| - Combine Query and Context         |
| - Incorporate Retrieved Documents   |
| - Generate Response                 |
+--------------------------------------+
        |
        v
+-----------------------------+
|  Post-Processing & Output   |
| - Format Response           |
| - Validation                |
+-----------------------------+
        |
        v
+----------------------+
| Deliver Final Output |
+----------------------+
        |
        v
+----------------------------------+
|   Continuous Learning Loop       |
| - Collect User Feedback          |
| - Update Models/Index            |
| - Error Analysis & Correction    |
+----------------------------------+
```

## **Setup Instructions**

### **1. Clone the Repository**

```bash
git clone https://github.com/RajdeepDas43/Intelligent-Query-Routing-System.git
cd Intelligent-Query-Routing-System
```

### **2. Create a Virtual Environment**

It is recommended to create a virtual environment to manage dependencies:

#### **For Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate
```

#### **For macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### **3. Install Dependencies**

With the virtual environment activated, install the necessary Python packages:

```bash
pip install -r requirements.txt
```

### **4. Setup Elasticsearch**

1. **Install Elasticsearch**:
   - Download and install Elasticsearch from the [official website](https://www.elastic.co/downloads/elasticsearch).

2. **Start Elasticsearch**:
   - Run the following command to start the Elasticsearch server:
     ```bash
     ./bin/elasticsearch
     ```

3. **Index Documents**:
   - Populate your Elasticsearch index with documents by using the provided script:
     ```bash
     python index_documents.py
     ```

### **5. Set Up Environment Variables**

Create a `.env` file in the root directory to configure environment variables:

```plaintext
ELASTICSEARCH_HOST=localhost
ELASTICSEARCH_PORT=9200
OPENAI_API_KEY=your_openai_api_key
```

Replace `your_openai_api_key` with your actual OpenAI API key.

### **6. Run the Project**

You can now run the different components of the project:

#### **Query Classification**

```bash
python query_classifier.py
```

#### **Context Management**

```bash
python context_manager.py
```

#### **Document Retrieval**

```bash
python document_retriever.py
```

#### **Response Generation**

```bash
python response_generator.py
```

#### **Run the Entire Pipeline**

You can run the entire RAG pipeline by executing the following script:

```bash
python run_pipeline.py
```

### **7. Running Tests**

Unit tests are provided to validate the functionality of each component. Run the tests with:

```bash
python -m unittest discover -s tests
```

## **Usage**

### **1. Running the Complete Pipeline**

You can run the entire RAG pipeline by executing the following script:

```bash
python run_pipeline.py
```

This script will:

- Accept a user query.
- Classify the query.
- Retrieve the relevant documents.
- Manage and inject context.
- Generate a response.
- Return the final output to the user.

### **2. Example Query**

```bash
python run_pipeline.py
```

**Input**:  
```plaintext
What is the revenue of Google in 2023?
```

**Output**:  
```plaintext
Google's revenue in 2023 was approximately $280 billion. This information was retrieved from multiple sources, including financial reports and recent news articles.
```

## **Contributing**

Contributions are welcome! Please follow the steps below to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Open a pull request.

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## **Acknowledgments**

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [ElasticSearch](https://www.elastic.co/)
