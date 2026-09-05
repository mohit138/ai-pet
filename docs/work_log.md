# AI Pet - Work Log

## Quick Reference
- Bluetooth & Audio Config: See `docs/bluetooth_setup.md`

---

## [2026-09-03] - Audio I/O, Environment & BT Reconnect Setup
- **Status:** Complete
- **Summary:** Verified two-way audio on Sony SRS-XB13. Created isolated Python `.venv`, `requirements.txt` (`gTTS`, `python-dotenv`), and `.env` for MAC address abstraction. Implemented modular `utils/bt_manager.py` for auto-reconnect/profile switching integrated into `scripts/morning_greeting.py`.
- **Next Step:** Implement voice listening module using microphone input.

---

## [2026-09-05] - BT Management, Timezone, Cron & Voice Listener
- **Status:** Complete
- **Summary:**
  - Updated `utils/bt_manager.py` with explicit session variables (`XDG_RUNTIME_DIR`, `DBUS_SESSION_BUS_ADDRESS`) and `pactl` volume boosts for background execution in Cron.
  - Set system timezone using `timedatectl`.
  - Configured 8:00 AM daily cron job for `morning_greeting.py`.
  - Built modular microphone listening loop in `utils/listener.py` using `SpeechRecognition` and `PyAudio`, including ALSA noise suppression.
  - Updated `requirements.txt` and `README.md` with system audio dependencies (`portaudio19-dev`, `flac`).
- **Next Step:** Integrate dynamic LLM response generation or local API calls.