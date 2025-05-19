from openai import OpenAI
from config import OPENAI_API_KEY, DEFAULT_MODEL, get_available_models

client = OpenAI(api_key=OPENAI_API_KEY)

def chat_with_gpt(messages, model=DEFAULT_MODEL):
    if not OPENAI_API_KEY:
        raise ValueError("OpenAI API key not found. Please set it in your .env file.")
    
    # Validate model
    available_models = get_available_models()
    if model not in available_models:
        raise ValueError(f"Model {model} is not available. Please select from: {', '.join(available_models)}")
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"Error communicating with OpenAI API: {str(e)}")
