class Solution:
	def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
		if not list1 and not list2: return None
		if not list1: return list2
		if not list2: return list1
		if list1.val <= list2.val:
			root = ListNode(list1.val, None)
			root.next = self.mergeTwoLists(list1.next,list2)
		else:
			root = ListNode(list2.val, None)
			root.next = self.mergeTwoLists(list1,list2.next)
		return root
