class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return nlargest(k,nums)[k - 1]
        
        
        