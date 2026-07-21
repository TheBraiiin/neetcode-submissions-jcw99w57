class TimeMap:

    def __init__(self):
        self.kvs = defaultdict(list)        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kvs[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        entry = ""

        if key not in self.kvs:
            return entry

        kvsval = self.kvs[key]
        l = 0
        r = len(kvsval) - 1
        while l <= r:
            m = (r + l) // 2
            midts = kvsval[m][1]

            if timestamp == midts:
                entry = kvsval[m][0]
                break
            elif timestamp > midts:
                entry = kvsval[m][0]
                l = m + 1
            else:
                r = m - 1

        return entry



                
