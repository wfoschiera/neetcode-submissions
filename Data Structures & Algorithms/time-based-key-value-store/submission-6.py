from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.keys = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values_list = self.keys.get(
            key,
        )
        if values_list is None:
            return ''

        start = 0
        end = len(values_list) - 1
        best_match = ''
        while start <= end:
            mid = (start + end) // 2
            stored_value = values_list[mid][0]
            stored_time = values_list[mid][1]
            if stored_time <= timestamp:
                best_match = stored_value
                start = mid + 1
            else:
                end = mid - 1
        return best_match
