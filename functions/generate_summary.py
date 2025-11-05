from functions.tokenize_pdf import tokenize_pdf

def generate_summary(pdf):
    """
    Generates extensive summary of the input pdf.
    """
  
    token_pdf = tokenize_pdf(pdf)
    query = 'Give an extensive summary of the content'
    prompt = f"""
    Your aim is to analyze the input and give a detailed summary of the content. You should start by saying "The document 
    discusses/the document talks about" etc and give an overview on the topic. Then you should summarize in details the content.
    The summary should be so that when reading it the person knows everything important and nothing is left out. Stick to the information 
    provided in the input Avoid commenting the input - just state objectively what's written, do not write opinions about it.

    Context:
    {token_pdf}

    Question:
    {query}

    Answer:
    """

    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {"role": "system", "content": "You are helpful to humans."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()
