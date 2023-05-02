import openai

openai.api_key = "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"


def text_process(prompt, engine="text-davinci-003", temperature=0.6, max_tokens=2000, top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0):
    response = openai.Completion.create(
    engine= engine,
    prompt= prompt,
    temperature=temperature,
    max_tokens= max_tokens,
    top_p= top_p,
    frequency_penalty= frequency_penalty,
    presence_penalty= presence_penalty
    )
    return response.choices[0]['text'].strip()

def context(prompt, engine="text-davinci-003", temperature=0.7, max_tokens=256, top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0):
    response = openai.Completion.create(
    engine= engine,
    prompt= prompt,
    temperature=temperature,
    max_tokens= max_tokens,
    top_p= top_p,
    frequency_penalty= frequency_penalty,
    presence_penalty= presence_penalty
    )
    return response.choices[0]['text'].strip()

def chat(prompt, engine="text-davinci-003", temperature=0.6, max_tokens=1000, top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0):
    response = openai.Completion.create(
    engine= engine,
    prompt= prompt,
    temperature=temperature,
    max_tokens= max_tokens,
    top_p= top_p,
    frequency_penalty= frequency_penalty,
    presence_penalty= presence_penalty
    )
    return response.choices[0]['text'].strip()

