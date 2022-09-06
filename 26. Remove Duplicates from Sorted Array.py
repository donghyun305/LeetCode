from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 0
        unique = []
        while pointer + 1 <= len(nums) - 1:
            if nums[pointer] == nums[pointer+1]:
                nums.remove(nums[pointer])
            else:
                pointer += 1
        return len(nums)

Solution.removeDuplicates(Solution, [1,1,2])

# 2nd Trial
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         pointer = 0
#         unique = []
#         while pointer + 1 <= len(nums)-1:
#             if nums[pointer] != nums[pointer+1]:
#                 unique.append(nums[pointer])
#                 pointer += 1
#             else:
#                 pointer += 1
#         if nums[-1] != nums[-2]:
#             unique.append(nums[-1])
#         result = len(unique)
#         return result



