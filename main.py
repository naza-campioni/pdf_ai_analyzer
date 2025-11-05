# main function
from embedding import get_embedding
from sort_index import sort_index
from generate_answer import generate_answer
from tokenize_pdf import tokenize_pdf

def main(text, query, k=5):
  """
  Parameters:
  text: input file
  query: question to answer
  k: first k indeces that match question to input

  when streamlit is coded, we'll pass the tokenized and embedded text directly, only the query will need embedding
  """
  token_pdf = tokenize_pdf(text)
  embeddings = get_embedding(token_pdf)
  retrieved_text = sort_index(query, token_pdf, embeddings, k=k)
  answer = generate_answer(query, retrieved_text)
  return answer
