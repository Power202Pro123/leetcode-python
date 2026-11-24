class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        Array = []
        for x in range(1,len(nums)):
            for y in range(0,x):
                if nums[x] + nums[y] == target:
                    Array.append(x)
                    Array.append(y)
                    return Array


            

        