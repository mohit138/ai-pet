# ai-pet

This project is a Ai Pet which would run on Raspberry Pi. 

## Quick Setup

Run these 3 commands to set up the Python environment after cloning:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Note: Requires python3-full and mpg123 installed via apt on the host system.
```bash
sudo apt update && sudo apt install -y python3-full mpg123
```