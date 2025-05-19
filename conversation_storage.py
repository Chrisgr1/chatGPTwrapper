import json
import os
from datetime import datetime
from typing import List, Dict, Optional

class ConversationStorage:
    def __init__(self, storage_dir: str = "conversations"):
        self.storage_dir = storage_dir
        os.makedirs(storage_dir, exist_ok=True)

    def save_conversation(self, conversation_id: str, messages: List[Dict], title: Optional[str] = None) -> str:
        """Save a conversation to a file"""
        if not title:
            # Create a title from the first user message
            for msg in messages:
                if msg["role"] == "user":
                    title = msg["content"][:50] + "..." if len(msg["content"]) > 50 else msg["content"]
                    break
            if not title:
                title = f"Conversation {conversation_id}"

        data = {
            "id": conversation_id,
            "title": title,
            "messages": messages,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }

        file_path = os.path.join(self.storage_dir, f"{conversation_id}.json")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return title

    def load_conversation(self, conversation_id: str) -> Dict:
        """Load a conversation from a file"""
        file_path = os.path.join(self.storage_dir, f"{conversation_id}.json")
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_conversations(self) -> List[Dict]:
        """List all saved conversations"""
        conversations = []
        for filename in os.listdir(self.storage_dir):
            if filename.endswith('.json'):
                file_path = os.path.join(self.storage_dir, filename)
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    conversations.append({
                        "id": data["id"],
                        "title": data["title"],
                        "created_at": data["created_at"],
                        "updated_at": data["updated_at"]
                    })
        return sorted(conversations, key=lambda x: x["updated_at"], reverse=True)

    def delete_conversation(self, conversation_id: str):
        """Delete a conversation file"""
        file_path = os.path.join(self.storage_dir, f"{conversation_id}.json")
        if os.path.exists(file_path):
            os.remove(file_path) 