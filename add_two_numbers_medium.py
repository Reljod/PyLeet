"""
Problem: https://leetcode.com/problems/add-two-numbers/
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        return str(self._get_number_from_list_node())
    
    def _get_number_from_list_node(self) -> int:
        number: int = 0
        current_node: ListNode = self
        
        multiplier = 1
        while current_node is not None:
            current_number = current_node.val
            number += current_number * multiplier
            
            multiplier *= 10
            current_node = current_node.next
        
        return number
    
class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_number: int = self._get_number_from_list_node(l1)
        second_number: int = self._get_number_from_list_node(l2)
        
        added_number = first_number + second_number
        
        multiplier = self._get_multiplier_from_number(added_number)
        l_node = self._make_list_node_from_number(added_number, multiplier)
        return l_node
    
    def _get_number_from_list_node(self, list_node: ListNode) -> int:
        number: int = 0
        current_node: ListNode = list_node
        
        multiplier = 1
        while current_node is not None:
            current_number = current_node.val
            number += current_number * multiplier
            
            multiplier *= 10
            current_node = current_node.next
        
        return number
    
    def _get_multiplier_from_number(self, number: int) -> int:
        multiplier = 1
        while number >= multiplier*10:
            multiplier *= 10
        
        return multiplier

    def _make_list_node_from_number(self, number: int, multiplier: int) -> ListNode:
        first_number = number % 10
        l_node = ListNode(first_number)
        
        current_multiplier = 10
        cur_node: ListNode = l_node
        while(multiplier >= current_multiplier):
            
            current_number = number // current_multiplier
            current_number %= 10
            
            new_node = ListNode(current_number)
            cur_node.next = new_node
            cur_node = new_node
            
            current_multiplier *= 10
        
        return l_node
    
def create_node_from_list(l: list[int]) -> ListNode:
    if len(l) == 0:
        return ListNode(0)
    
    l_node = ListNode(l[0])
    
    cur_node = l_node
    for ind in range(1, len(l)):
        new_node = ListNode(l[ind])
        cur_node.next = new_node
        cur_node = new_node
        
    return l_node
        

if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    l_ans_1 = Solution().add_two_numbers(l1, l2)
    
    print(l_ans_1)
    
    l3 = create_node_from_list([0])
    l4 = create_node_from_list([0])
    l_ans_2 = Solution().add_two_numbers(l3, l4)
    
    print(l_ans_2)
    
    l5 = create_node_from_list([9,9,9,9,9,9,9])
    l6 = create_node_from_list([9,9,9,9])
    l_ans_3 = Solution().add_two_numbers(l5, l6)
    
    print(l_ans_3)
    
    l7 = create_node_from_list([5])
    l8 = create_node_from_list([5])
    l_ans_4 = Solution().add_two_numbers(l7, l8)
    
    print(l_ans_4)
        