# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nextdigit = 0
        headNode = ListNode()
        sumNode = headNode
        while l1 or l2:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            #print(f"l1val : {l1val}, l2val : {l2val}")
            
            val = (l1val + l2val+nextdigit)%10
            #print(f"val : {val}")

            nextdigit = (l1val + l2val+nextdigit)//10
            #print(f"next : {nextdigit}")
            
            sumNode.val = val
            

            if l1: l1 = l1.next
            if l2: l2 = l2.next

            if l1 or l2: 
                sumNode.next = ListNode()
                sumNode = sumNode.next
            else:
                if nextdigit > 0 : sumNode.next = ListNode(nextdigit)


        return headNode

