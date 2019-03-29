class Solution:
    def removeDuplicates(self, nums) -> int:
        k = 0
        if len(nums) == 0:
            return k
        start_i = k
        for i in range(1, len(nums)):


            if nums[start_i] == nums[i]:
                continue
            else:
                if i - start_i > 1:
                    nums[k], nums[k+1] = nums[start_i], nums[start_i+1]
                    start_i = i
                    k+=2
                else:
                    nums[k] = nums[i]
                    k += 1
            print(nums)
        print(k)

Solution().removeDuplicates([1,1,1,2,2,3])