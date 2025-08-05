# Just Plejd - A plejd Python API

Control your Plejd devices from Python! This package lets you connect to your Plejd setup, list rooms/scenes/devices, listen to changes, and perhaps most importantly - send commands to your devices.

## ⚡️ Installation

```
git clone https://github.com/peterssonjesper/just_plejd.git
cd just_plejd
pip install .
```

## 🚀 Example

To try to test it, put something like this in example.py:

```python
import asyncio
from just_plejd import Plejd, commands

async def main():
    plejd = Plejd(email='your@email.com', password='your-password')
    await plejd.connect()

    await plejd.run(commands.turn_on(39))  # Replace 39 with your device address
    #await plejd.run(commands.turn_off(39)) # 39 being the device address
    #await plejd.run(commands.dim(39, 182)) # 182 being a number between 0 (off) to 255 (on)
    #await plejd.run(commands.activate_scene(1)) # 1 being the scene address

    try:
        # Wait indefinitely for on_change events
        await asyncio.Event().wait()
    except asyncio.CancelledError:
        print("Exiting...")
    finally:
        await plejd.disconnect()

asyncio.run(main())
```

### Then run it

```bash
EMAIL="your@email.com" PASSWORD="your-plejd-password" python example.py
```

## 🙏 Credits & Inspiration

Big shoutout to [PyPlejd](https://github.com/thomasloven/pyplejd) - a lot of this project is inspired (okay, also borrowed) from their excellent work.

The main innovation here is simply just a workaround to extract the Plejd device's MAC address directly from its Bluetooth advertisement. This makes it possible to run the library on macOS and iOS, where traditional access to Bluetooth MAC addresses is restricted due to system-level obfuscation.
