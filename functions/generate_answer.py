def generate_answer(query, retrieved_text):
    """
    query: the user question
    retrieved_text: string containing the most relevant chunk(s)
    """
    prompt = f"""
    Your aim is to analyze the input and answer any input-specific questions using ONLY the information provided below.
    If the information is not in the context, say you don't know. 

    Context:
    {retrieved_text}

    Question:
    {query}

    Answer:
    """

    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {"role": "system", "content": "You are helpful with humans."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()
