class Solution:
    def hammingWeight(self, n: int) -> int:
        new=bin(n)[2:]
        count=0
        for i in new:
            if i=='1':
                count+=1
        return count