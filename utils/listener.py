import os
import sys
import ctypes
import speech_recognition as sr

# Suppress low-level ALSA / PortAudio stderr messages
ERROR_HANDLER_FUNC = ctypes.CFUNCTYPE(None, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p)
def py_error_handler(filename, line, function, err, fmt):
    pass
c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

try:
    asound = ctypes.cdll.LoadLibrary('libasound.so.2')
    asound.snd_lib_error_set_handler(c_error_handler)
except Exception:
    pass

def listen_for_speech(timeout=8, phrase_time_limit=12):
    """
    Calibrates for ambient noise and captures spoken audio from the Bluetooth microphone.
    Returns the recognized text string or None.
    """
    recognizer = sr.Recognizer()
    
    # --- Tuned Sensitivity Settings ---
    recognizer.dynamic_energy_threshold = True
    recognizer.energy_threshold = 300       # Baseline sensitivity
    recognizer.pause_threshold = 1.2         # Silence duration (sec) before ending turn
    
    try:
        # Explicitly use system mic managed by PipeWire
        with sr.Microphone(sample_rate=16000) as source:
            print("[Pet Listening]: Calibrating background noise...")
            # Snappy 0.5s noise calibration for faster response start
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            
            print("[Pet Listening]: Listening now (speak into your Sony speaker)...")
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            
            print("[Pet Listening]: Processing speech...")
            text = recognizer.recognize_google(audio)
            print(f"[User Said]: \"{text}\"")
            return text

    except sr.WaitTimeoutError:
        print("[Pet Listening]: No speech detected within timeout.")
        return None
    except sr.UnknownValueError:
        print("[Pet Listening]: Could not understand audio (check mic input level or distance).")
        return None
    except Exception as e:
        print(f"[Pet Error]: Error during listening: {e}")
        return None

if __name__ == "__main__":
    result = listen_for_speech()
    print("Result:", result)