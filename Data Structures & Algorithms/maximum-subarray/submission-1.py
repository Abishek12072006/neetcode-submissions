class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m=nums[0]
        c=0
        for i in nums:
            c+=i
            m=max(m,c)
            if c<0:
                c=0
        return m
        