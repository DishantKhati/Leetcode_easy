class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        x=nums[i]
        n=len(nums)
        for j in range(1,n):
            if x!=nums[j]:
                i+=1
                x=nums[j]
                nums[i]=x
        return i+1
