from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def generate_response(query, retrieved_docs=None, context=None):
    # Construct the system message
    system_message = {
        "role": "system",
        "content": "You are a helpful assistant capable of generating detailed and accurate responses based on the context and retrieved documents."
    }

    # Construct the user message
    user_message = {
        "role": "user",
        "content": f"Query: {query}"
    }

    # Construct the context message if context is available
    if context:
        context_message = {
            "role": "user",
            "content": f"Context: {context}"
        }
    else:
        context_message = None

    # Construct the document retrieval message if retrieved documents are available
    if retrieved_docs:
        doc_message = {
            "role": "user",
            "content": f"Relevant Documents: {retrieved_docs}"
        }
    else:
        doc_message = None

    # Build the messages list
    messages = [system_message, user_message]

    if context_message:
        messages.append(context_message)

    if doc_message:
        messages.append(doc_message)

    # Generate response using the OpenAI API
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    # Extract the generated response text
    generated_text = response['choices'][0]['message']['content']
    
    return generated_text

# Example usage
if __name__ == "__main__":
    retrieved_docs = ["Google's revenue in 2022 was $257 billion."]
    query = "What about 2023?"
    context = "Previous discussion about Google's financials."
    response = generate_response(query, retrieved_docs, context)
    print(f"Generated Response: {response}")
