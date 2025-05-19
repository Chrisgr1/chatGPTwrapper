import uuid
from datetime import datetime

class ConversationManager:
    def __init__(self, conversation_id: str = None):
        self.conversation_id = conversation_id or str(uuid.uuid4())
        self.messages = [{"role": "system", "content": "You are a helpful assistant."}]
        self.title = None
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def add_user_message(self, content):
        self.messages.append({"role": "user", "content": content})
        self.updated_at = datetime.now().isoformat()

    def add_assistant_message(self, content):
        self.messages.append({"role": "assistant", "content": content})
        self.updated_at = datetime.now().isoformat()

    def get_conversation(self):
        return self.messages

    def reset(self):
        self.conversation_id = str(uuid.uuid4())
        self.messages = [{"role": "system", "content": "You are a helpful assistant."}]
        self.title = None
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
 