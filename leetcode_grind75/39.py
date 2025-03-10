# 39. Combination Sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            # decision 1: including candidates[i]
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            # decision 2: not including any occurrences of candidates[i] from here on
            cur.pop()
            dfs(i+1, cur, total)

        dfs(0, [], 0)
        return res
