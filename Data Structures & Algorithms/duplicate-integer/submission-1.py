class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums = set (nums)

        for i in range (len(nums)):
            curr_num = nums[i]

            if curr_num in set_nums:
                set_nums.discard(curr_num)
            else:
                return True
        return False