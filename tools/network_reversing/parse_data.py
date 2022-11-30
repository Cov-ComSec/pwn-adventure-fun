import struct
import sys


def parse_quest_finished(code) -> tuple:
    packet_length = 6
    length_of_location_name = struct.unpack("h", code[2:4])[0]
    location_name = code[4:4 + length_of_location_name]
    length_of_quest_name = struct.unpack("h", code[4 + length_of_location_name:6 + length_of_location_name])[0]
    quest_name = code[6 + length_of_location_name:6 + length_of_location_name + length_of_quest_name]
    decoded = f"[Quest Finished] Location Name: {location_name}, Quest Name: {quest_name}"
    return code[packet_length + length_of_location_name + length_of_quest_name:], decoded


def parse_toggle_pvp(code) -> tuple:
    packet_length = 3
    pvp_status = struct.unpack("b", code[2:3])[0]
    decoded = f"[Toggle PvP] Enabled:" if pvp_status == 1 else f"[Toggle PvP] Disabled:"
    return code[packet_length:], decoded


def parse_set_current_quest(code) -> tuple:
    packet_length = 4
    length_of_quest_name = struct.unpack("h", code[2:4])[0]
    quest_name = code[4:4 + length_of_quest_name]
    decoded = f"[Set Current Quest] Quest Name: {quest_name}"
    return code[packet_length + length_of_quest_name:], decoded


def parse_player_state(code) -> tuple:
    packet_length = 8
    player_id = struct.unpack("i", code[2:6])[0]
    length_of_state_name = struct.unpack("h", code[6:8])[0]
    state_name = code[8:8 + length_of_state_name]
    decoded = f"[Player State] Player ID: {player_id}, State Name: {state_name}"
    return code[packet_length + length_of_state_name:], decoded


def parse_change_attack_state(code) -> tuple:
    packet_length = 10
    player_id = struct.unpack("i", code[2:6])[0]
    length_of_attack_state = struct.unpack("h", code[6:8])[0]
    attack_state = code[8:8 + length_of_attack_state]
    target_id = struct.unpack("h", code[8 + length_of_attack_state:10 + length_of_attack_state])[0]
    decoded = f"[Change Attack State] Player ID: {player_id}, Attack State: {attack_state}, Target ID: {target_id}"
    return code[packet_length + length_of_attack_state:], decoded


def parse_remove_element(code) -> tuple:
    packet_length = 6
    element_id = struct.unpack("i", code[2:6])[0]
    decoded = f"[Remove Element] Element ID: {element_id}"
    return code[packet_length:], decoded


def parse_toggle_run(code) -> tuple:
    packet_length = 3
    run_status = struct.unpack("b", code[2:3])[0]
    decoded = f"[Toggle Run] Enabled:" if run_status == 1 else f"[Toggle Run] Disabled:"
    return code[packet_length:], decoded


def parse_new_achievement(code) -> tuple:
    packet_length = 4
    length_of_achievement_name = struct.unpack("h", code[2:4])[0]
    achievement_name = code[4:4 + length_of_achievement_name]
    decoded = f"[New Achievement] Achievement Name: {achievement_name}"
    return code[packet_length + length_of_achievement_name:], decoded


def parse_enemy_position(code) -> tuple:
    packet_length = 30
    packet = code[2:packet_length - 2]
    enemy_id = struct.unpack("i", packet[:4])[0]
    x, y, z = struct.unpack("f", packet[4:8])[0], struct.unpack("f", packet[8:12])[0], \
              struct.unpack("f", packet[12:16])[0]
    r, yy, p = struct.unpack("h", packet[16:18])[0], struct.unpack("h", packet[18:20])[0], \
               struct.unpack("h", packet[20:22])[0]
    not_sure = packet[22:28]
    decoded = f"[Enemy Position] Enemy ID: {enemy_id}, X: {x}, Y: {y}, Z: {z}, R: {r}, P: {p}"
    return code[packet_length:], decoded


def parse_update_mana(code) -> tuple:
    packet_length = 6
    mana_level = struct.unpack("i", code[2:6])[0]
    decoded = f"[Updated Mana] Mana Level: {mana_level}"
    return code[packet_length:], decoded


def parse_jump(code) -> tuple:
    packet_length = 3
    decoded = f"[Jump]"
    return code[packet_length:], decoded


def parse_pick_up_item(code) -> tuple:
    packet_length = 6
    packet = code[2:packet_length - 2]
    item_id = struct.unpack("i", packet[2:6])[0]
    decoded = f"[Picked Up Item] Item ID: {item_id}"
    return code[packet_length:], decoded


def parse_new_inventory_item(code) -> tuple:
    packet_length = 8
    length_of_item_name = struct.unpack("h", code[2:4])[0]
    item_name = code[4:4 + length_of_item_name]
    quantity = struct.unpack("i", code[4 + length_of_item_name:4 + length_of_item_name + 4])[0]
    decoded = f"[New Inventory Item] Item Name: {item_name}, Quantity: {quantity}"
    return code[packet_length + length_of_item_name:], decoded


def parse_shoot(code) -> tuple:
    packet_length = 10
    length_of_weapon_name = struct.unpack("h", code[2:4])[0]
    weapon_name = code[4:4 + length_of_weapon_name]
    x, y, z = struct.unpack("f", code[4 + length_of_weapon_name:4 + length_of_weapon_name + 4])[0], \
              struct.unpack("f", code[4 + length_of_weapon_name + 4:4 + length_of_weapon_name + 8])[0], \
              struct.unpack("f", code[4 + length_of_weapon_name + 8:4 + length_of_weapon_name + 12])[0]
    decoded = f"[Shoot] Weapon: {weapon_name}, X: {x}, Y: {y}, Z: {z}"
    return code[packet_length + length_of_weapon_name:], decoded


def parse_send_message(code) -> tuple:
    packet_length = 4
    length_of_message = struct.unpack("h", code[2:4])[0]
    message = code[4:4 + length_of_message]
    decoded = f"[Sent Message] Message: {message}"
    return code[packet_length + length_of_message:], decoded


def parse_spawn_position(code) -> tuple:
    packet_length = 22
    packet = code[2:packet_length - 2]
    not_sure = packet[:2]
    x, y, z = struct.unpack("f", packet[2:6])[0], struct.unpack("f", packet[6:10])[0], \
              struct.unpack("f", packet[10:14])[0]
    r, yy, p = struct.unpack("h", packet[14:16])[0], struct.unpack("h", packet[16:18])[0], \
               struct.unpack("h", packet[18:20])[0]

    decoded = f"[Spawn Position] X: {x}, Y: {y}, Z: {z}, R: {r}, P: {p}"
    return code[packet_length:], decoded


def parse_update_health(code) -> tuple:
    packet_length = 10
    packet = code[2:packet_length - 2]
    player_id = struct.unpack("i", packet[:4])[0]
    health = struct.unpack("i", packet[4:8])[0]
    decoded = f"[Updated Health] Player ID: {player_id}, Health: {health}"
    return code[packet_length:], decoded


def parse_update_location(code) -> tuple:
    packet_length = 22
    packet = code[2:packet_length - 2]
    x, y, z = struct.unpack("f", packet[:4])[0], struct.unpack("f", packet[4:8])[0], struct.unpack("f", packet[8:12])[0]
    r, yy, p = struct.unpack("h", packet[12:14])[0], struct.unpack("h", packet[14:16])[0], \
               struct.unpack("h", packet[16:18])[0]
    constant = packet[18:22]
    decoded = f"[Updated Location] X: {x}, Y: {y}, Z: {z}, R: {r}, P: {p}, Y: {yy}"
    return code[packet_length:], decoded


def parse_new_element(code) -> tuple:
    packet_length = 32
    element_id = struct.unpack("i", code[2:6])[0]
    who_knows = code[6:11]
    element_name_length = struct.unpack("h", code[11:13])[0]
    element_name = code[13:13 + element_name_length]
    coord_base = 13 + element_name_length
    x, y, z = struct.unpack("f", code[coord_base:coord_base + 4])[0], \
              struct.unpack("f", code[coord_base + 4:coord_base + 8])[0], \
              struct.unpack("f", code[coord_base + 8:coord_base + 12])[0]
    r, yy, p = struct.unpack("h", code[coord_base + 12:coord_base + 14])[0], \
               struct.unpack("h", code[coord_base + 14:coord_base + 16])[0], \
               struct.unpack("h", code[coord_base + 16:coord_base + 18])[0]
    packet_length = packet_length + element_name_length

    decoded = f"[New Element] ID: {element_id}, Name: {element_name}, X: {x}, Y: {y}, Z: {z}, R: {r}, P: {p}, Y: {yy}"
    return code[packet_length + 3:], decoded


opcodes = {
    0x0200: {"name": "Authenticate", },
    0x1600: {"name": "Spawn position 1", "parse_func": parse_spawn_position},
    0x1700: {"name": "Spawn position 2", "parse_func": parse_spawn_position},
    0x2300: {"name": "Spawn position 3", "parse_func": parse_spawn_position},
    0x232a: {"name": "Send message", "parse_func": parse_send_message},
    0x233e: {"name": "Send answer", },
    0x2366: {"name": "Finish dialog", },
    0x2373: {"name": "Send dialog", },
    0x2462: {"name": "Purchase item", },
    0x2a69: {"name": "Fire", "parse_func": parse_shoot},
    0x2b2b: {"name": "Update health", "parse_func": parse_update_health},
    0x3003: {"name": "Spawn position 4", "parse_func": parse_spawn_position},
    0x3031: {"name": "Activate logic gate", "parse_func": parse_spawn_position},
    0x3206: {"name": "Spawn position 5", "parse_func": parse_spawn_position},
    0x4103: {"name": "Spawn position 6", "parse_func": parse_spawn_position},
    0x5e64: {"name": "Remove quest"},
    0x6368: {"name": "Change location"},
    0x6370: {"name": "New inventory item", "parse_func": parse_new_inventory_item},
    0x6565: {"name": "Pick up item", "parse_func": parse_pick_up_item},
    0x6576: {"name": "Event", },
    0x6674: {"name": "Fast travel", },
    0x6a70: {"name": "Jump", "parse_func": parse_jump},
    0x6d61: {"name": "Update mana", "parse_func": parse_update_mana},
    0x6d6b: {"name": "New element", "parse_func": parse_new_element},
    0x6d76: {"name": "Update location", "parse_func": parse_update_location},
    0x6e71: {"name": "New quest", },
    0x7073: {"name": "Enemy position", "parse_func": parse_enemy_position},
    0x7075: {"name": "New achievement", "parse_func": parse_new_achievement},
    0x7076: {"name": "Change PvP state", "parse_func": parse_toggle_pvp},
    0x713d: {"name": "Select quest", "parse_func": parse_set_current_quest},
    0x713e: {"name": "Quest done", "parse_func": parse_quest_finished},
    0x726d: {"name": "Remove inventory item", },
    0x726e: {"name": "Run", "parse_func": parse_toggle_run},
    0x7273: {"name": "Respawn", },
    0x7274: {"name": "Teleport", },
    0x7374: {"name": "Change player state", "parse_func": parse_player_state},
    0x7472: {"name": "Change attack state", "parse_func": parse_change_attack_state},
    0x7878: {"name": "Remove element", "parse_func": parse_remove_element},
}


def main(code_to_parse: bytes) -> None:
    global opcodes
    done = False
    while code_to_parse:
        opcode = struct.unpack(">h", code_to_parse[:2])[0]
        if opcode in opcodes:
            if "parse_func" not in opcodes[opcode]:
                print(f"Cannot parse packet type '{opcodes[opcode]['name']}' yet")
            code_to_parse, decoded_packet = opcodes[opcode]["parse_func"](code_to_parse)
        else:
            decoded_packet = "[Unknown Packet]"
            code_to_parse = code_to_parse[2:]
            # print(code_to_parse)
        print(decoded_packet)


if __name__ == "__main__":
    # if len(sys.argv) != 2:
    #     print("Usage: python3 parse_packets.py <packet.bin>")
    #     exit(1)
    with open("init.bin", "rb") as f:
        main(f.read())
    # with open(sys.argv[1], "rb") as f:
    #     main(f.read())
