import os
import sys
import time
from datetime import datetime
from gtts import gTTS

# Import Bluetooth utility and speech listener
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.bt_manager import ensure_bluetooth_connected
from utils.listener import listen_for_speech

def speak(text):
    """Converts text to speech and plays it using PulseAudio backend."""
    print(f"[Pet]: {text}")
    tts = gTTS(text=text, lang='en')
    filename = "greeting.mp3"
    tts.save(filename)
    # '-o pulse' forces mpg123 to use PulseAudio directly, avoiding JACK segfaults
    os.system(f"mpg123 -o pulse -q {filename}")
    if os.path.exists(filename):
        os.remove(filename)

def main():
    current_time = datetime.now().strftime("%I:%M %p")
    print("--- Starting AI Pet Morning Routine ---")
    
    # 1. Ensure Bluetooth speaker/mic headset profile is reconnected
    ensure_bluetooth_connected()
    
    # 2. Spoken Alarm Greeting
    greeting = f"Good morning! It is {current_time}. Time to wake up and get moving. How are you feeling today?"
    speak(greeting)
    
    # 3. Voice interaction loop
    user_input = listen_for_speech(timeout=8, phrase_time_limit=10)
    
    if user_input:
        user_input_lower = user_input.lower()
        if "good" in user_input_lower or "great" in user_input_lower:
            response = "That is awesome! Let's have a productive day ahead."
        elif "tired" in user_input_lower or "sleepy" in user_input_lower:
            response = "I hear you. Go grab a warm cup of coffee or water!"
        else:
            response = f"Got it, you said {user_input}. Have a great start to your morning!"
        
        speak(response)
    else:
        speak("Looks like you're still sleepy. Have a good morning!")

if __name__ == "__main__":
    main()