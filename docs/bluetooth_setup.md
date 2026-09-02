# Bluetooth Audio & Microphone Setup (Sony SRS-XB13)

Hardware configuration to enable two-way audio (Speaker + Mic) over Bluetooth on Raspberry Pi 5.

## 1. Pair & Connect Speaker
Run bluetoothctl and execute:
  power on
  agent on
  default-agent
  scan on

Locate the MAC address (e.g., 78:5E:A2:35:11:11) and run:
  scan off
  pair 78:5E:A2:35:11:11
  trust 78:5E:A2:35:11:11
  connect 78:5E:A2:35:11:11
  exit

## 2. Enable Microphone Profile
By default, Linux connects in A2DP mode (Output only). Switch to Headset mode (HFP/HSP) to activate the microphone:

  pactl set-card-profile bluez_card.78_5E_A2_35_11_11 headset-head-unit

## 3. Quick Verification Commands
- Test Speaker Output:
    speaker-test -t wav -c 2 -l 1

- Test Microphone Input:
    arecord -d 5 -f cd test_mic.wav && aplay test_mic.wav

