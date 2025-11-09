import random
import streamlit as st
from dotenv import load_dotenv
import os

from functions.tokenize_pdf import tokenize_pdf
from functions.embeddings import get_embedding
from functions.sort_index import sort_index

load_dotenv()

headers = ["Hi, how can I help you?", "Hi, how can I assist you?", "What are we learning today?"]
index = random.randint(0, len(headers) - 1)

st.title(headers[index])
pdf = st.file_uploader("Upload your PDF file", type=['pdf'])

if pdf:
	

	token_pdf = tokenize_pdf(pdf)
	# outputs a decoded (human language) tokenized version of the input 

	# 3) embed tokenized pdf (easier and safer to embed after tokenization)
	embeddings = get_embedding(token_pdf)

	# 4) input query and output retrieved text from the query
	query = st.text_input("What's your question?")
	retrieved_text = sort_index(query, token_pdf, embeddings, k=3)

	st.write(retrieved_text)
	#st.write(token_pdf)