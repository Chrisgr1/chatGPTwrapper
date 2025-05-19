AVAILABLE_MODELS = {
    "GPT-3.5 Turbo": "gpt-3.5-turbo",
    "GPT-4": "gpt-4",
    "GPT-4 Turbo": "gpt-4-turbo-preview"
}

def get_model_name(model_id: str) -> str:
    """Get the display name for a model ID."""
    for name, id in AVAILABLE_MODELS.items():
        if id == model_id:
            return name
    return model_id 