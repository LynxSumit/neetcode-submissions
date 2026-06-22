class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((timestamp, value))
        else:
            time_tup = (timestamp, value)
            self.store[key] = []
            self.store[key].append(time_tup)

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
                i = 0
                j = len(self.store[key]) - 1
                smaller = (0, "") if self.store[key][0][0] > timestamp else self.store[key][0]
                while i <= j:
                    mid = (i+j) // 2
                    if self.store[key][mid][0] < timestamp:
                        smaller = self.store[key][mid]
                        i = mid+1
                    elif self.store[key][mid][0] > timestamp:
                        j = mid-1
                    else:
                        return self.store[key][mid][1]
                print(smaller[1])
                return smaller[1]
        else:
            return ""

        
