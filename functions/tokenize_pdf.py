from pypdf import PdfReader
from functions.tokenizer import tok_and_chunk

def tokenize_pdf(pdf, model="text-embedding-3-small", max_tokens=500, overlap=50):
  reader = PdfReader(pdf)
  all_chunks = []
  for page_num, page in enumerate(reader.pages):
    text = page.extract_text()
    page_chunks = tok_and_chunk(text, model=model, max_tokens=max_tokens, overlap=overlap)
    # for i, chunk_text in enumerate(page_chunks):
    #     all_chunks.append({
    #         "page": page_num,
    #         "chunk_id": i,
    #         "text": chunk_text
    #     })

    for _, chunk_text in enumerate(page_chunks):
        all_chunks.append(chunk_text)
  return all_chunks
