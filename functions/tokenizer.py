import tiktoken

def tok_and_chunk(text, model, max_tokens, overlap):
  """
  Encodes the input text into tokens and chunks it into smaller pieces.
  First encode, then chunk then decode so that the chunks are readable
  for embeddings.

  Parameters:
  text: the text to chunk
  model: the name of the encoding to use
  max_tokens: the maximum number of tokens per chunk
  overlap: the number of tokens to overlap between chunks
  
  Returns:
  A list of chunks of text.
  """

  enc = tiktoken.encoding_for_model(model)    # specify encoder
  tokens = enc.encode(text)

  chunks = []
  start = 0
  while start < len(tokens):
    end = start + max_tokens
    chunk_tokens = tokens[start:end]
    chunk_text = enc.decode(chunk_tokens)
    chunks.append(chunk_text)
    start += max_tokens - overlap

  return chunks
