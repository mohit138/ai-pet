# AI Pet - Work Log

## Quick Reference
- Bluetooth & Audio Config: See `docs/bluetooth_setup.md`

---

## [2026-09-03] - Audio I/O, Environment & BT Reconnect Setup
- **Status:** Complete
- **Summary:** Verified two-way audio on Sony SRS-XB13. Created isolated Python `.venv`, `requirements.txt` (`gTTS`, `python-dotenv`), and `.env` for MAC address abstraction. Implemented modular `utils/bt_manager.py` for auto-reconnect/profile switching integrated into `scripts/morning_greeting.py`.
- **Next Step:** Implement voice listening module using microphone input.

---

## [2026-09-05] - BT Management, Cron, Gemini LLM & Voice Listener Tuning
- **Status:** Complete
- **Summary:**
  - **Bluetooth & Cron (`utils/bt_manager.py`):** Configured background session environment variables (`XDG_RUNTIME_DIR`, `DBUS_SESSION_BUS_ADDRESS`) and `pactl` volume boosts to enable reliable Bluetooth audio execution via headless system cron jobs. Set system timezone using `timedatectl` and set up an 8:00 AM daily cron entry for `morning_greeting.py`.
  - **Gemini LLM Brain (`utils/brain.py`):** Integrated `google-genai` SDK using `gemini-2.5-flash` with stateful chat sessions. Solved `NoneType` and truncation issues by setting `max_output_tokens=300` to accommodate internal model reasoning ("thinking") tokens, combined with strict system instructions for plain-text spoken output (no markdown or emojis).
  - **Modular Voice Listener (`utils/listener.py`):** Built microphone capture loop using `SpeechRecognition` and `PyAudio` with ALSA noise suppression. Optimized Voice Activity Detection (VAD) sensitivity by increasing `pause_threshold` to 1.2s and `phrase_time_limit` to 12s to prevent cutting off natural human speech, while dropping ambient noise calibration down to 0.5s for faster startup response.
  - **Dependency Clean-up & Docs:** Cleaned `requirements.txt` to include only explicit top-level dependencies (`google-genai`, `python-dotenv`, `gTTS`, `PyAudio`, `SpeechRecognition`, `pygame`). Updated `README.md` with system audio dependencies (`portaudio19-dev`, `flac`, `mpg123`).
  - **End-to-End Pipeline:** Successfully validated full interaction loop in `scripts/morning_greeting.py` combining PipeWire audio capture, Google Speech-to-Text, Gemini LLM reasoning, and `gTTS` speech playback via `mpg123`.
- **Next Step:** Build a continuous multi-turn voice chat loop (`scripts/voice_loop.py`) and explore native function calling tools (Google Calendar / Spotify).