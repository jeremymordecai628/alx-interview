#!/usr/bin/python3
"""
This module provides a function to check if all the boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Parameters:
    boxes (list of lists): A list where each index represents a box, and the values
                           inside the lists represent keys to other boxes.

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.
    """
    # Create a list to keep track of which boxes are unlocked; initially only
    # box 0 is unlocked
    unlocked = [False] * len(boxes)
    unlocked[0] = True

    # Start by collecting the keys from the first box (box 0)
    keys = [0]

    # Process all the collected keys
    while keys:
        key = keys.pop(0)  # Get the next key

        # Iterate over the keys inside the box that corresponds to the current
        # key
        for new_key in boxes[key]:
            # Check if the new_key opens a valid box and if that box is not
            # already unlocked
            if new_key < len(boxes) and not unlocked[new_key]:
                unlocked[new_key] = True  # Unlock the box
                # Add this key to the list to check its keys
                keys.append(new_key)

    # Return True if all boxes are unlocked, otherwise False
    return all(unlocked)
