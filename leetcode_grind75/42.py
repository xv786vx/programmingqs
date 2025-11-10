# 42. Trapping Rain Water
class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        maxl, maxr = height[0], height[len(height) - 1]
        l, r = 1, len(height) - 2

        while l <= r:
            if maxl <= maxr:
                if maxl - height[l] > 0:
                    water += maxl - height[l]
                if height[l] > maxl:
                    maxl = height[l]
                l += 1
                
            else:
                if maxr - height[r] > 0:
                    water += maxr - height[r]
                if height[r] > maxr:
                    maxr = height[r]

                r -= 1
        
        
        return water

            