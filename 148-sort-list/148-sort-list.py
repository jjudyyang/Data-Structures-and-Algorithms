# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #save eveything into array, sort array and then put back into linked list
        
        cur = head
        list1 = []
    
        while cur:
            list1.append(cur.val)
            cur = cur.next
        
        list1.sort()
        
        #store into linked list again
        dummy = ListNode()
        
        cur = dummy
        for num in list1:
            cur.next = ListNode(num)
            cur = cur.next
            
        return dummy.next
            