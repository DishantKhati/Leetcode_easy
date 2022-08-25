class Solution(object):
	def searchInsert(self, nums, target):
		if target > nums[-1]:
			return len(nums)
		for index, num in enumerate(nums):
			if num == target:
				return index
			elif target < num:
				return index
