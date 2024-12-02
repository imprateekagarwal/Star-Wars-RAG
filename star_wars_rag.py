import os
from dotenv import load_dotenv
from openai import OpenAI
from sentence_transformers import SentenceTransformer
import numpy as np
import json

class StarWarsRAG:
    def __init__(self, corpus_path='star_wars_corpus.txt'):
        load_dotenv()
        self.client = OpenAI(base_url=os.getenv('OPENAI_BASE_URL'), api_key=os.getenv('OPENAI_API_KEY'))
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
        
        with open(corpus_path, 'r') as f:
            self.corpus_sentences = [s.strip() for s in f.read().split('.') if s.strip()]
            self.corpus_embeddings = self.embedder.encode(self.corpus_sentences)

    def semantic_retrieve(self, query, top_k=1):
        query_embedding = self.embedder.encode([query])[0]
        similarities = np.dot(self.corpus_embeddings, query_embedding) / (
            np.linalg.norm(self.corpus_embeddings, axis=1) * np.linalg.norm(query_embedding)
        )
        top_indices = similarities.argsort()[-top_k:][::-1]
        return '. '.join([self.corpus_sentences[i] for i in top_indices])

    def process_query(self, query):
        try:
            context = self.semantic_retrieve(query)
            response = self.client.chat.completions.create(
                model="Gpt4o",
                messages=[
                    {"role": "system", "content": "You are Yoda. Speak in Yoda's unique style."},
                    {"role": "user", "content": f"Context: {context}\n\nQuestion: {query}"}
                ]
            ).choices[0].message.content.strip()

            return {
                "user_prompt": query,
                "retrieved_context": context,
                "system_response": response
            }
        except Exception as e:
            return {"error": str(e)}

def main():
    rag = StarWarsRAG()
    queries = [
        "Who is Luke Skywalker's father?",
        "Tell me about the Rebel Alliance",
        "Who trains Luke Skywalker?"
    ]
    
    for query in queries:
        result = rag.process_query(query)
        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()