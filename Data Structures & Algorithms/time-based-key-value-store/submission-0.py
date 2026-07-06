class TimeMap:

    def __init__(self):
        # Dictionary:
        # key -> list of [value, timestamp]
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        # If key doesn't exist, create an empty list
        if key not in self.store:
            self.store[key] = []

        # Append new value and timestamp
        # Timestamps are guaranteed to be increasing
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:

        # If key doesn't exist
        if key not in self.store:
            return ""

        values = self.store[key]

        left, right = 0, len(values) - 1

        # Stores the latest valid answer
        res = ""

        while left <= right:

            mid = (left + right) // 2

            # values[mid] = [value, timestamp]

            if values[mid][1] <= timestamp:

                # Valid timestamp
                res = values[mid][0]

                # Try to find a later valid timestamp
                left = mid + 1

            else:
                # Timestamp too large
                right = mid - 1

        return res