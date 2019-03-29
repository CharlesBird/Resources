class Solution:
    def removeElement(self, nums, val) -> int:
        # while val in nums:
        #     nums.remove(val)
        # return len(nums)
        k = 0
        for v in nums:
            if v != val:
                nums[k] = v
                k += 1
        return k

