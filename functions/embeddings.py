def get_embedding(text):
  """
  Returns a stacked list of embeddings for the given text.

  Parameters:
  text: a dictionary of strings to embed

  Returns:
  A list of embeddings.  
  """

  # texts = [t['text'] for t in text] # strings only for embeddings
  response = client.embeddings.create(
      model="text-embedding-3-small",
      input=text
  )
  return np.array([d.embedding for d in response.data], dtype=np.float32)  # .embedding because output is an embedding object
