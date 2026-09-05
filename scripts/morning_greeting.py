import os
import sys
from datetime import datetime
from gtts import gTTS

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.bt_manager import ensure_bluetooth_connected
from utils.listener import listen_for_speech
from utils.brain import Brain

def speak(text):
    """Converts text to speech and plays it using PulseAudio backend."""
    print(f"[Pet]: {text}")
    tts = gTTS(text=text, lang='en')
    filename = "greeting.mp3"
    tts.save(filename)
    os.system(f"mpg123 -o pulse -q {filename}")
    if os.path.exists(filename):
        os.remove(filename)

def main():
    current_time = datetime.now().strftime("%I:%M %p")
    print("--- Starting AI Pet Morning Routine ---")
    
    # 1. Ensure Bluetooth speaker/mic is active
    ensure_bluetooth_connected()
    
    # 2. Initialize Gemini Brain
    brain = Brain()
    
    # 3. Morning Greeting
    greeting = f"Good morning! It is {current_time}. Time to wake up! How are you feeling today?"
    speak(greeting)
    
    # 4. Listen for user response
    user_input = listen_for_speech(timeout=8, phrase_time_limit=8)
    
    if user_input:
        # Generate dynamic LLM response
        response = brain.think(user_input)
        speak(response)
    else:
        speak("Looks like you're still sleepy. Have a great morning!")

if __name__ == "__main__":
    main()