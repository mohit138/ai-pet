import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

SYSTEM_PROMPT = (
    "You are an affectionate, witty AI desk pet living on a Raspberry Pi. "
    "Respond in plain spoken English only. "
    "Do NOT use markdown, bold text, asterisks, emojis, bullet points, or special formatting. "
    "Keep responses under 25 words."
)

class Brain:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env file.")
        
        # Initialize Google GenAI Client
        self.client = genai.Client(api_key=api_key)
        self.model = "gemini-3.6-flash"
        
        # Initialize chat session with system instruction
        self.chat = self.client.chats.create(
            model=self.model,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                max_output_tokens=600
            )
        )

    def think(self, user_text: str) -> str:
        """Sends user speech to Gemini chat session and safely extracts response text."""
        try:
            response = self.chat.send_message(user_text)
            
            # Guard against NoneType before calling .strip()
            if response and getattr(response, "text", None):
                return response.text.strip()
            
            return "I heard you, but I wasn't sure how to respond!"
            
        except Exception as e:
            print(f"[Brain Error]: {e}")
            return "Oops, my brain glitched for a second!"

if __name__ == "__main__":
    print("Testing Gemini Brain...")
    brain = Brain()
    reply = brain.think("Good morning buddy! What is on our agenda today?")
    print(f"Pet Response: {reply}")