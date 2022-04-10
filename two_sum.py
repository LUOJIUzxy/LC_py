#use the foolest method
#6462ms

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        returnList = [0, 0]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums), 1):
                if nums[i] + nums[j] == target:
                    returnList[0] = i
                    returnList[1] = j
                    return returnList

#first optimization