class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        l=0
        h=n-1
        mid=0
        while mid<=h:
            if nums[mid]==0:
                nums[l],nums[mid]=nums[mid],nums[l]
                mid+=1
                l+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[h],nums[mid]=nums[mid],nums[h]
                h-=1