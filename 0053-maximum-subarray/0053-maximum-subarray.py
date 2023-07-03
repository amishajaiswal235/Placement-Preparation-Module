class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N=len(nums)
        maxnum = nums[0]
        sumnum = maxnum
        for i in range(1,N):
            sumnum = max(nums[i],sumnum + nums[i])
            maxnum = max(maxnum,sumnum)
        return maxnum