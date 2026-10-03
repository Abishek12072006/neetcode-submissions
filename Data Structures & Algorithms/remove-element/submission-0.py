class Solution:
    def removeElement(self, nums, val):
        count = 0

        for i in nums:
            if i != val:
                nums[count] = i
                count += 1

        return count