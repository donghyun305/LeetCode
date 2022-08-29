from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    values = {}
    for idx, value in enumerate(nums):
        if target - value in values:
            return [values[target - value], idx]
        else:
            values[value] = idx

twoSum([2,5,7,9], 9)