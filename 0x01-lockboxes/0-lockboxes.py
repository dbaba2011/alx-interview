#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    n = len(boxes)
    unlock_boxes = set([0])
    lock_boxes = set(boxes[0]).difference(set([0]))
    while len(lock_boxes) > 0:
        boxIdx = lock_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in unlock_boxes:
            lock_boxes = lock_boxes.union(boxes[boxIdx])
            unlock_boxes.add(boxIdx)
    return n == len(unlock_boxes)
