# Remove Duplicates from Sorted Array II
class Solution:
    def removeDuplicates(self, nums) -> int:
        # Method One
        for i, v in enumerate(nums):
            while i+2 < len(nums) and nums[i+2] == v:
                del nums[i+2]
            return len(nums)

        # Method Two
        l = len(nums)
        i = 2
        while i < l:
            if nums[i] == nums[i-1] == nums[i-2]:
                del nums[i]
                l -= 1
            else:
                i += 1
        return l


# Solution().removeDuplicates([1,1,1,2,2,3])
Solution().removeDuplicates([1,2,2])
# Solution().removeDuplicates([0,0,1,1,1,1,2,3,3])