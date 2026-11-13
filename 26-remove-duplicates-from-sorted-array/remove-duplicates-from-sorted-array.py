class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        if not nums:
            return 0

        k = 0 # tracks the last unique element found
        
        # two pointers (i and n)
        for i in range (1, len(nums)):
            if nums[k] != nums[i]:
                k += 1
                nums[k] = nums[i]
                # replace that value with nums[i]

        return k + 1 # index of last unique element + 1 to produce number of unique elements
