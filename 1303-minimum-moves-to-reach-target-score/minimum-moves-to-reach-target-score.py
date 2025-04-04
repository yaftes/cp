class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if maxDoubles == 0:
            return target - 1
        ans = 0
        
        while maxDoubles > 0 and target > 1:
            if target % 2 == 0:
                ans += 1
            else:
                ans += 2
            target = target // 2
            maxDoubles -= 1

        if target > 1:
            ans += target - 1
        return ans
    
        