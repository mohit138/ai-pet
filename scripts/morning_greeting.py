import os
import sys
import time
from datetime import datetime
from gtts import gTTS

# Import Bluetooth utility from utils folder
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.bt_manager import ensure_bluetooth_connected

def speak(text):
    """Converts text to speech and plays it through the Bluetooth speaker."""
    print(f"[Pet]: {text}")
    tts = gTTS(text=text, lang='en')
    filename = "greeting.mp3"
    tts.save(filename)
    os.system(f"mpg123 -q {filename}")
    if os.path.exists(filename):
        os.remove(filename)

def main():
    current_time = datetime.now().strftime("%I:%M %p")
    print("--- Starting AI Pet Morning Routine ---")
    
    # Ensure Bluetooth speaker is reconnected before greeting
    ensure_bluetooth_connected()
    
    # 1. Spoken Alarm Greeting
    greeting = f"Good morning! It is {current_time}. Time to wake up and get moving."
    speak(greeting)
    
    # Placeholder for voice interaction loop (7:00 AM - 8:30 AM window)
    print("Pet is active. (Voice loop will go here next)")

if __name__ == "__main__":
    main()
