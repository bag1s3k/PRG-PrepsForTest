from itertools import permutations
from math import factorial

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        return [list(item) for item in permutations(nums)]

solution = Solution()
print(solution.permute([1,2,3]))
print(solution.permute([0,1]))
print(solution.permute([1]))
print(solution.permute([5,4,6,2]))