class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # make a hastable
        h = {}
        # loop over all entries of the nums array. For each element (num) and index (i)
        for i, num in enumerate(nums):
            # find out the counter part amount for each element in nums
            n = target - num
            # if counterpart is not in the hashtable, then store that number and index in the hashtable in case it is the counterpart to something else
            if n not in h:
                h[num] = i
            # else if the counter part is in there, then return that index
            else:
                return [h[n], i]
