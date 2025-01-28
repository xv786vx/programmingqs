class RecentCounter:

    def __init__(self):
        self.reqs = []

    def ping(self, t: int) -> int:
        self.reqs.append(t)
        while self.reqs and self.reqs[0] < t - 3000:
            self.reqs.pop(0)
        return len(self.reqs) 
            
