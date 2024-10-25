#!/usr/bin/python3
"""
Log Parsing Script

This script reads input from stdin line by line, extracts the file size and HTTP status codes
from each line, and calculates statistics.

- Input format:
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
    - IP Address: any valid IPv4 address
    - date: any valid date enclosed in square brackets
    - status code: one of the expected HTTP status codes (200, 301, 400, 401, 403, 404, 405, 500)
    - file size: integer representing the file size

- Output:
    - After every 10 lines or on keyboard interrupt (CTRL + C), print:
        1. Total file size so far: "File size: <total size>"
        2. Count of each HTTP status code (if it has appeared)
           in ascending order of the status codes.

- Handles incorrect input lines by skipping them.

Author: <Your Name>
"""

import sys

# Initialize total file size counter and status code dictionary
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """
    Print the current metrics:
    - Total file size so far.
    - Number of occurrences of each HTTP status code.
    Only print status codes that have appeared at least once.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


try:
    for line in sys.stdin:
        try:
            # Split the line into parts for processing
            parts = line.split()

            # Ensure the line has enough parts and matches the expected format
            if len(parts) >= 7:
                # Extract file size and status code (last two parts)
                file_size = int(parts[-1])
                status_code = int(parts[-2])

                # Update total file size
                total_size += file_size

                # Update the count of the specific status code, if it's valid
                if status_code in status_codes:
                    status_codes[status_code] += 1

                # Increment the line count for the 10-line check
                line_count += 1

                # Every 10 lines, print the statistics
                if line_count % 10 == 0:
                    print_stats()

        except (ValueError, IndexError):
            # Ignore lines that don't match the expected format (e.g., invalid
            # file size or status code)
            continue

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    # Print the statistics before the script exits
    print_stats()
    sys.exit()

# After processing all lines, print final statistics
print_stats()
