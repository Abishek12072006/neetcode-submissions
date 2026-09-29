class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        L=[]
        R=[]
        for i in nums:
            if i not in L:
                L.append(i)
            else:
                R.append(i)
        for i in L:
            if i not in R:
                return i
                

        