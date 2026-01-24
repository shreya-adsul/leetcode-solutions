class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        i=0
        while i<len(nums):
            if nums[k]==nums[i]:
                i+=1
            else:
                nums[k+1]=nums[i]
                k+=1
                i+=1
        return k+1
