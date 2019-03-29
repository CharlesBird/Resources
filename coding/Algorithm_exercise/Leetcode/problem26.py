class Solution:
    def removeDuplicates(self, nums) -> int:
        k = 0
        if len(nums) == 0:
            return k
        for v in nums:
            if nums[k] != v:
                k+=1
                nums[k] = v
        #
        # while k < len(nums)-1:
        #     print(k, len(nums))
        #     if nums[k] == nums[k+1]:
        #         nums.pop(k+1)
        #     else:
        #         k+=1
        return k+1


Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4,4])

# Solution().removeDuplicates([1,1,2])