def parse_incoming_packet(data: bytearray):
    data_bytes = [data[i] for i in range(0, len(data))]

    match data_bytes:
        case [0x00, 0x01, 0x10, 0x00, 0x21, scene, *extra]:
            return {
                "cmd": "scene_activated",
                "scene": scene,
                "triggered": True,
            }

        case [0x00, 0x01, 0x10, 0x00, 0x16, addr, button, *extra]:
            return {
                "cmd": "button_press",
                "address": addr,
                "button": button,
                "action": "release" if len(extra) and not extra[0] else "press",
            }

        case [addr, 0x01, 0x10, 0x00, 0xC8, state, dim1, dim2, *extra] | [
            addr,
            0x01,
            0x10,
            0x00,
            0x98,
            state,
            dim1,
            dim2,
            *extra,
        ]:
            return {
                "cmd": "dim",
                "address": addr,
                "state": state,
                "dim": dim2
            }

        case [addr, 0x01, 0x10, 0x00, 0x97, state, *extra]:
            return {
                "cmd": "change_state", # Turn on/off
                "address": addr,
                "state": state,
            }

        case [addr, 0x01, 0x10, 0x04, 0x20, a, 0x01, 0x11, *color_temp]:
            color_temp = int.from_bytes(color_temp, "big")
            return {
                "cmd": "color_temperature",
                "address": addr,
                "temperature": color_temp,
            }

        case [addr, 0x01, 0x10, 0x04, 0x20, a, 0x03, b, *extra, ll1, ll2]:
            # Motion
            lightlevel = int.from_bytes([ll1, ll2], "big")
            return {
                "cmd": "motion",
                "address": addr,
                "lightlevel": lightlevel,
            }

    return None