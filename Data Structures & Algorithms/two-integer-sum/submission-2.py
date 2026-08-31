class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i,num in enumerate(nums):
            diff = target-num
            if num in d:
                return [d[num],i]
            d[diff] = i
        
        return []
        