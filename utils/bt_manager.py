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
    
    # 1. Setup session environment variables so cron background jobs can access PipeWire/PulseAudio
    uid = os.getuid()
    xdg_dir = f"/run/user/{uid}"
    dbus_addr = f"unix:path=/run/user/{uid}/bus"

    os.environ["XDG_RUNTIME_DIR"] = xdg_dir
    os.environ["DBUS_SESSION_BUS_ADDRESS"] = dbus_addr

    env = os.environ.copy()
    
    # 2. Trigger connection via bluetoothctl
    subprocess.run(f"bluetoothctl connect {MAC_ADDRESS}", shell=True, capture_output=True, env=env)
    time.sleep(2)  # Give bluetooth stack time to initialize handshake
    
    # 3. Force PipeWire card profile to headset mode (enables mic)
    profile_cmd = f"pactl set-card-profile {card_name} headset-head-unit"
    result = subprocess.run(profile_cmd, shell=True, capture_output=True, text=True, env=env)
    
    if result.returncode == 0:
        print("[BT] Speaker connected & Headset profile active.")
        # Unmute and set playback volume to 85% for clear audio output
        subprocess.run("pactl set-sink-mute @DEFAULT_SINK@ 0", shell=True, env=env)
        subprocess.run("pactl set-sink-volume @DEFAULT_SINK@ 75%", shell=True, env=env)
        
        # Microphone input volume
        subprocess.run("pactl set-source-mute @DEFAULT_SOURCE@ 0", shell=True, env=env)
        subprocess.run("pactl set-source-volume @DEFAULT_SOURCE@ 100%", shell=True, env=env)
        return True
    else:
        print("[BT Warning] Speaker unreachable or profile switch failed.")
        return False
