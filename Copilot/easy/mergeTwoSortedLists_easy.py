'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 
Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        if list1:
            current.next = list1
        else:
            current.next = list2
        
        return dummy.next

sol = Solution()
import sys

if len(sys.argv) < 2:
    num_simulations = 1
else:
    if sys.argv[1] == "1":
        num_simulations = 1
    else:
        num_simulations = 10000000

for _ in range(num_simulations):
    # Example1:
    list1 = ListNode([1, 2, 4])
    list2 = ListNode([1, 3, 4])
    merged_list = sol.mergeTwoLists(list1, list2)

    # Example1:
    list1 = ListNode([])
    list2 = ListNode([])
    merged_list = sol.mergeTwoLists(list1, list2)

    # Example1:
    list1 = ListNode([])
    list2 = ListNode([0])
    merged_list = sol.mergeTwoLists(list1, list2)

# # Example1:
# list1 = ListNode([1, 2, 4])
# list2 = ListNode([1, 3, 4])
# merged_list = sol.mergeTwoLists(list1, list2)
# print(merged_list)

# # Example1:
# list1 = ListNode([])
# list2 = ListNode([])
# merged_list = sol.mergeTwoLists(list1, list2)
# print(merged_list)

# # Example1:
# list1 = ListNode([])
# list2 = ListNode([0])
# merged_list = sol.mergeTwoLists(list1, list2)
# print(merged_list)