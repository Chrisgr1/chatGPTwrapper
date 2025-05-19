# ChatGPT Wrapper

A Streamlit-based wrapper for the OpenAI ChatGPT API with conversation history management and model selection.

## Features

- Multiple model support (GPT-3.5, GPT-4, etc.)
- Conversation history management
- Searchable conversation history
- Persistent storage of conversations
- User-friendly interface with sidebar navigation

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ChatGPTWrapper.git
cd ChatGPTWrapper
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your OpenAI API key:
```plaintext
OPENAI_API_KEY=your_api_key_here
```

5. Run the application:
```bash
streamlit run app.py
```

## Project Structure

- `app.py`: Main Streamlit application
- `config.py`: Configuration settings
- `conversation.py`: Conversation management
- `conversation_storage.py`: Conversation persistence
- `gpt_client.py`: OpenAI API client
- `models.py`: Model definitions and utilities

## Usage

1. Select a model from the dropdown menu
2. Type your message in the input box
3. Click "Send" to get a response
4. Use the sidebar to:
   - Search through conversation history
   - Load previous conversations
   - Start new conversations
   - Delete old conversations

## Requirements

- Python 3.8+
- Streamlit
- OpenAI Python package
- python-dotenv

## License

MIT License 