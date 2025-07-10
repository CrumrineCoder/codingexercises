# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        pointer_hare = pointer_turtle = head
        prev = None

        while pointer_hare and pointer_hare.next:
            pointer_hare = pointer_hare.next.next

            next_temp = pointer_turtle.next
            pointer_turtle.next = prev
            prev = pointer_turtle
            pointer_turtle = next_temp

        if pointer_hare:
            pointer_turtle = pointer_turtle.next

        left = prev
        right = pointer_turtle

        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True