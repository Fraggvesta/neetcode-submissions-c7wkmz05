class TimeMap:

    def __init__(self):
        self.heap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.heap:
            self.heap[key] = [(value, timestamp)]
        else:
            self.heap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.heap:
            return ""

        if timestamp > self.heap[key][-1][1]:
            return self.heap[key][-1][0]

        elif timestamp < self.heap[key][0][1]:
            return ""

        l =  0
        r = len(self.heap[key])-1
        while(l<=r):
            m = (l + r)//2
            if self.heap[key][m][1] <= timestamp:
                l = m + 1
            else:
                r = m - 1
        
        return self.heap[key][r][0]