from collections import defaultdict, OrderedDict


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val = {}
        self.key_to_freq = {}
        self.freq_to_keys = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1

        # Get the current frequency of the key
        freq = self.key_to_freq[key]
        # Remove the key from the current frequency list
        del self.freq_to_keys[freq][key]

        # If the current frequency list is empty and it was the minimum frequency, increment min_freq
        if not self.freq_to_keys[freq]:
            if self.min_freq == freq:
                self.min_freq += 1
            del self.freq_to_keys[freq]

        # Increment the key's frequency
        self.key_to_freq[key] += 1
        freq = self.key_to_freq[key]
        self.freq_to_keys[freq][key] = True

        return self.key_to_val[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key in self.key_to_val:
            # Update the value of the key
            self.key_to_val[key] = value
            # Update the frequency of the key
            self.get(key)
            return

        if len(self.key_to_val) >= self.capacity:
            # Evict the least frequently used key
            k, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val[k]
            del self.key_to_freq[k]

        # Insert the new key
        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        self.freq_to_keys[1][key] = True
        self.min_freq = 1
