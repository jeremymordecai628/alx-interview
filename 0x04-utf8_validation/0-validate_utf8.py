#!/usr/bin/python3
"""
Module to validate UTF-8 encoding.
"""


def validUTF8(data):
    """
    Check if a given data set represents a valid UTF-8 encoding.

    Args:
        data (List[int]): A list of integers representing bytes in UTF-8.

    Returns:
        bool: True if the data is valid UTF-8 encoding, otherwise False.
    """
    num_bytes = 0

    for byte in data:
        # We only need the last 8 bits, so use bitwise AND with 255
        # (0b11111111).
        byte &= 0xFF

        # If we are expecting more bytes in the current character.
        if num_bytes > 0:
            # Check that this byte starts with '10' (binary '10xxxxxx').
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1
        else:
            # Determine the number of bytes for the new character.
            if (byte >> 7) == 0b0:
                num_bytes = 0  # 1-byte character (ASCII).
            elif (byte >> 5) == 0b110:
                num_bytes = 1  # 2-byte character.
            elif (byte >> 4) == 0b1110:
                num_bytes = 2  # 3-byte character.
            elif (byte >> 3) == 0b11110:
                num_bytes = 3  # 4-byte character.
            else:
                return False

    # If we finished and have processed all expected bytes correctly.
    return num_bytes == 0
