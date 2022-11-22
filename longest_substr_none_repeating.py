"""
We can create a hash map of all characters?
abcabcbb
{
    a: 2
    b: 4
    c: 2
}

hash_map.lenght = max output

Two pointer (brute force) -> O(m * k) 
where k <= lenght of hash_map.

Space complexity: O(k)

1. The first pointer will point to the first letter/character of the word.
E.g.
ptr1 = "a"

2. The second pointer will traverse the word, and it will stop if it reaches a duplicate character.
It will also stop if it reaches the maximum length/output.
"""


class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        updated_max: int = 0
        sliding_set = set()
        left_pointer = 0
        
        for right_pointer in range(len(s)):
            while (s[right_pointer] in sliding_set):
                sliding_set.remove(s[left_pointer])
                left_pointer += 1
            
            sliding_set.add(s[right_pointer])
            right_pointer += 1
            updated_max = max(updated_max, len(sliding_set))
        
    

if __name__ == '__main__':
    Solution().length_of_longest_substring("pwwkew")