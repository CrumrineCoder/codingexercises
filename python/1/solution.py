from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        leftCounter = 0
        
        while leftCounter < len(nums) - 1:
            rightCounter = leftCounter + 1
            
            while rightCounter < len(nums):
                if nums[leftCounter] + nums[rightCounter] == target:
                    return [leftCounter, rightCounter]
                rightCounter += 1
            
            leftCounter += 1
        
        return []  