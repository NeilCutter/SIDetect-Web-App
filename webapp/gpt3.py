import openai
import os
# openai.api_key = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")

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

