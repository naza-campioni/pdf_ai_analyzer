# main function
import os
from openai import OpenAI
from langdetect import detect

from functions.embeddings import get_embedding
from functions.sort_index import sort_index
from functions.generate_answer import generate_answer
from functions.tokenize_pdf import tokenize_pdf

def main(text, query, k=5):
  """
  Parameters:
  text: input file
  query: question to answer
  k: first k indeces that match question to input

  when streamlit is coded, we'll pass the tokenized and embedded text directly, only the query will need embedding
  """
  my_key = os.getenv("OPENAI_API_KEY")
  client = OpenAI(api_key=my_key)
  
  lang = detect(query)

  token_pdf = tokenize_pdf(text)
  embeddings = get_embedding(token_pdf)
  retrieved_text = sort_index(query, token_pdf, embeddings, k=k)
  answer = generate_answer(query, retrieved_text, lang)
  return answer
