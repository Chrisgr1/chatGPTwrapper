from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Define valid models
AVAILABLE_MODELS = {
    "GPT-3.5 Turbo": "gpt-3.5-turbo",
    "GPT-4": "gpt-4",
    "GPT-4 Turbo": "gpt-4-turbo-preview"
}

# Set default model
DEFAULT_MODEL = AVAILABLE_MODELS["GPT-3.5 Turbo"]  # This ensures we always have a valid model

def get_available_models():
    """Fetch all available models from OpenAI API"""
    client = OpenAI(api_key=OPENAI_API_KEY)
    try:
        models = client.models.list()
        # Filter for chat completion models and sort by name
        chat_models = [
            model.id for model in models.data 
            if model.id.startswith(('gpt-3.5', 'gpt-4'))
        ]
        return sorted(chat_models)
    except Exception as e:
        print(f"Error fetching models: {e}")
        # Fallback to basic models if API call fails
        return ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo-preview"]
