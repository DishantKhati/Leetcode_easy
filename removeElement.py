class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] == val:
                nums.remove(nums[i])
                length = length - 1
            else:
                i += 1
        return len(nums)
