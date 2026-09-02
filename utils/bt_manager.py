import os
import time
import subprocess
from dotenv import load_dotenv

# Load local environment variables from .env
load_dotenv()

MAC_ADDRESS = os.getenv("BT_MAC_ADDRESS")

def ensure_bluetooth_connected():
    """Forces Bluetooth reconnection and sets headset mode (mic + speaker)."""
    if not MAC_ADDRESS:
        print("[BT Error] BT_MAC_ADDRESS not set in .env file.")
        return False

    card_name = f"bluez_card.{MAC_ADDRESS.replace(':', '_')}"
    print(f"[BT] Attempting connection to {MAC_ADDRESS}...")
    
    # 1. Trigger connection via bluetoothctl
    subprocess.run(f"bluetoothctl connect {MAC_ADDRESS}", shell=True, capture_output=True)
    time.sleep(2)  # Give bluetooth stack time to initialize handshake
    
    # 2. Force PipeWire card profile to headset mode (enables mic)
    profile_cmd = f"pactl set-card-profile {card_name} headset-head-unit"
    result = subprocess.run(profile_cmd, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("[BT] Speaker connected & Headset profile active.")
        return True
    else:
        print("[BT Warning] Speaker unreachable or profile switch failed.")
        return False
