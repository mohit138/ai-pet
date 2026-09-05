# ai-pet

This project is a Ai Pet which would run on Raspberry Pi. 

## System Dependencies

Install required system libraries for audio playback, recording, and Python environment management:

`sudo apt update && sudo apt install -y python3-full mpg123 portaudio19-dev flac`

## Python Setup

1. Create and activate a virtual environment:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

2. Install Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure environment variables in .env:
    ```
        BT_MAC_ADDRESS=XX:XX:XX:XX:XX:XX
        GEMINI_API_KEY=<key>
    ```

## Running the Pet

To run the morning routine manually:
```bash
python3 scripts/morning_greeting.py
```

## Automated Cron Setup

To run automatically every morning at 8:00 AM, add this line to `crontab -e`:

`0 8 * * * /home/pi/Projects/ai-pet/.venv/bin/python /home/pi/Projects/ai-pet/scripts/morning_greeting.py >> /home/pi/Projects/ai-pet/cron_output.log 2>&1`