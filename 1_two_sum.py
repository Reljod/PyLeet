"""
Problem: https://leetcode.com/problems/two-sum/
"""

class Solution:
    def two_sum(self, nums: list[int], target: int) -> tuple[int, int]:
        num_dict = {}  # Space: O(N)
        
        for ind in range(len(nums)):  # Time: O(N)
            val = nums[ind]
            pair_val = target - val
            
            if (pair_ind := num_dict.get(pair_val)) != None:  # O(1)
                return (pair_ind, ind)
            
            num_dict[val] = ind  # O(1)
        
        return (None, None)
    

if __name__ == '__main__':
    print(Solution().two_sum(nums=[3, 1, 6, 9, 2], target=4))