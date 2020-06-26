class Solution:
	def findDuplicate(self, nums: List[int]) -> int:
		slow, fast = nums[0], nums[0]
		while True:
			slow = nums[slow]
			fast = nums[nums[fast]]
			if slow == fast:
				break

		nums1 = nums[0]
		nums2 = slow
		while nums1 != nums2:
			nums1 = nums[nums1]
			nums2 = nums[nums2]
		return nums2