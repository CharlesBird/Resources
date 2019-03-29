class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # method one
        # k = 0
        # for num in nums:
        #     if num:
        #         nums[k] = num
        #         k += 1
        # for i in range(k, len(nums)):
        #     nums[i] = 0
        # print(nums)
        # method two
        k = 0
        for i, num in enumerate(nums):
            if num:
                if k != i:
                    nums[k], nums[i] = nums[i], nums[k]
                    k += 1
                else:
                    k += 1
        print(nums)


# Solution().moveZeroes([0,1,0,3,12])
Solution().moveZeroes([0,1,0])
