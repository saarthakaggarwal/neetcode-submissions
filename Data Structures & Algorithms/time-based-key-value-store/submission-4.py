class TimeMap:

    def __init__(self):
        self.hm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hm:
            self.hm[key].append([value, timestamp])
        else:
            self.hm[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hm:
            array = self.hm[key]
        else:
            return ""

        l, r = 0, len(array) - 1

        while l < r:
            mid = (l + r + 1) // 2

            if array[mid][1] < timestamp:
                l = mid
            elif array[mid][1] > timestamp:
                r = mid - 1
            else:
                return array[mid][0]

        return array[l][0] if array[l][1] <= timestamp else ""

