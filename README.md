# Plejd Python API

Control your Plejd devices from Python! This package lets you connect to your Plejd setup, list rooms/scenes/devices, listen to changes, and perhaps most importantly - send commands to your devices.

## 🚀 Example

```python
import asyncio
import commands
from plejd import Plejd

async def main():
    plejd = Plejd(email='foo@bar.com', password='s3cret')
    await plejd.connect()

    site = plejd.get_site()
    print("Found the following devices:")
    print(site.devices)

    print("Found the following scenes:")
    print(site.scenes)

    plejd.on_change(lambda event: print(f"Got event: {event}"))

    await plejd.run(commands.turn_off(39)) # 39 being the device address
    await plejd.run(commands.turn_on(39))
    await plejd.run(commands.dim(39, 182)) # 182 being a number between 0 (off) to 255 (on)
    await plejd.run(commands.activate_scene(1)) # 1 being the scene address

    try:
        # Wait indefinitely for on_change events
        await asyncio.Event().wait()
    except asyncio.CancelledError:
        print("Exiting...")
    finally:
        await plejd.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
```

## 🔧 Installation

```
git clone https://github.com/yourusername/plejd-python.git
cd plejd-python

# Install dependencies (preferably in a virtual environment):
pip install -r requirements.txt
```

## 🙏 Credits & Inspiration

Big shoutout to [PyPlejd](https://github.com/thomasloven/pyplejd) 0 a lot of this project is inspired (okay, also borrowed) from their excellent work.

The main innovation here is simply just a workaround to extract the Plejd device's MAC address directly from its Bluetooth advertisement. This makes it possible to run the library on macOS and iOS, where traditional access to Bluetooth MAC addresses is restricted due to system-level obfuscation.
