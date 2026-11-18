class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        
        largest = nums[0]
        nums.sort()
        nums_sorted = []
        i = len(nums) - 1
        
        while i >= 0:
            if i > 0 and nums[i] == nums[i - 1]:
                i -= 1
            else:
                nums_sorted.append(nums[i])
                i -= 1

        if len(nums_sorted) < 3:
            return nums_sorted[0]
        else:
            return nums_sorted[2]

