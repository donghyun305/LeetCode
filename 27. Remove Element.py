from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer = 0
        while pointer + 1 <= len(nums) - 1:
            if nums[pointer] == val:
                nums.remove(nums[pointer])
            else:
                pointer += 1
        return len(nums)
