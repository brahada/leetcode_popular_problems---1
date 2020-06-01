class Solution():
    def singleNonDuplicate(self, nums):
        bottom, top = 0,len(nums)-1
        while bottom < top:
            middle = int((bottom + top) / 2)
            if nums[middle] == nums[middle ^ 1]:
                botton = middle+1
            else:
                top = middle
        return nums[bottom]
