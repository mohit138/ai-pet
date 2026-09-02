# AI Pet - Work Log

## Quick Reference
- Bluetooth & Audio Config: See `docs/bluetooth_setup.md`

---

## [2026-09-03] - Audio I/O, Environment & BT Reconnect Setup
- **Status:** Complete
- **Summary:** Verified two-way audio on Sony SRS-XB13. Created isolated Python `.venv`, `requirements.txt` (`gTTS`, `python-dotenv`), and `.env` for MAC address abstraction. Implemented modular `utils/bt_manager.py` for auto-reconnect/profile switching integrated into `scripts/morning_greeting.py`.
- **Next Step:** Implement voice listening module using microphone input.