Nums = [2, 5, 7, 3, 9]
target = 5

class Solution:
    def twoSum(self, nums:list[int], taregt:int)-> int:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i