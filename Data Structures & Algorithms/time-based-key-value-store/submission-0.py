
class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key, value, timestamp):
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append((timestamp, value))

    def get(self, key, timestamp):
        if key not in self.time_map:
            return ""

        pairs = self.time_map[key]
        
        while len(pairs) > 1 and pairs[1][0] <= timestamp:
            pairs.pop(0)

        first_timestamp, first_value = pairs[0]
        if first_timestamp <= timestamp:
            return first_value

        return ""

        




        