class Solution:
    def rotate(self, nums: list[int], k: int) -> list[int]:
        k %= len(nums)
        return [*nums[-k:], *nums[:-k]]


solution = Solution()
print([*solution.rotate([1,2,3,4,5,6,7], 3)])
print([*solution.rotate([-1,-100,3,99], 2)])