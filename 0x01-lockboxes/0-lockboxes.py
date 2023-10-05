#!/usr/bin/python3

def canUnlockAll(boxes):
    # Create a list to keep track of the keys we have initially.
    keys = [0]

    # Iterate through the keys we have and try to open more boxes.
    for key in keys:
        # Iterate through the keys in the current box.
        for box_key in boxes[key]:
            # If the key in the box can open a new box, and we haven't opened it yet, add it to the keys list.
            if box_key < len(boxes) and box_key not in keys:
                keys.append(box_key)

    # If we have keys for all boxes, return True; otherwise, return False.
    return len(keys) == len(boxes)
