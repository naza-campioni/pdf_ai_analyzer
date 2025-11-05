from embedding import get_embedding

def sort_index(query, text, embeddings, k):
  dim = embeddings.shape[1]
  index = faiss.IndexFlatL2(dim)
  index.add(embeddings)
  query_emb = get_embedding(query).reshape(1, -1)
  D, I = index.search(query_emb, k)

  retrieved_text = list(text[i] for i in I.flatten())
  return retrieved_text
  # retrieved_text = list(sentences[i] for i in I.flatten())
