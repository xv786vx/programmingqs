class TopVotedCandidate:

    def __init__(self, persons: list[int], times: list[int]):
        self.times = times
        self.leaders = []
        vote_count = {}
        last_vote = {}
        cur_leader = -1
        max_votes = 0

        for i in range(len(persons)):
            person = persons[i]
            time = times[i]

            if person not in vote_count:
                vote_count[person] = 1
            else:
                vote_count[person] += 1
            last_vote[person] = time

            if vote_count[person] > max_votes:
                cur_leader = person
                max_votes = vote_count[person]

            elif vote_count[person] == max_votes:
                if last_vote[person] > last_vote[cur_leader]:
                    cur_leader = person
            
            self.leaders.append(cur_leader)

    def bs_right(self, lst, x):
        low, high = 0, len(lst)
        while low < high:
            mid = (low + high) // 2
            if x >= lst[mid]:
                low = mid + 1
            else:
                high = mid
        return low

    def q(self, t: int) -> int:
        i = self.bs_right(self.times, t) - 1
        return self.leaders[i]

