from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        dic = {}
        dic1 = {}
        for index, value in enumerate(nums):
            dic[index] = value
        if target in dic.values():
            new_dic = {index:value for value,index in dic.items()}
            return new_dic.get(target)
        else:
            nums.append(target)
            nums = sorted(nums)
            for i, v in enumerate(nums):
                dic1[i] = v
            new_dic = {i:v for v,i in dic1.items()}
            return new_dic.get(target)
print(int(5/2))