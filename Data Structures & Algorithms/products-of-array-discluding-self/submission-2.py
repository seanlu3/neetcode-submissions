class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        res = [0] * n

        prefix[0] = suffix[n-1] = 1

        for x in range(1, n):
            prefix[x] = nums[x-1] * prefix[x-1]
        
        for x in range(n-2, -1, -1):
            suffix[x] = nums[x+1] * suffix[x+1]

        for x in range(n):
            res[x] = prefix[x] * suffix[x]

        return res