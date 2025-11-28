class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        def backtrack(start, current):
            result.append(list(current))
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                current.append(nums[i])
                backtrack(i+1, current)
                current.pop()
        backtrack(0, [])
        return result


solution = Solution()
print(solution.subsets([1,2,3]))
print(solution.subsets([0]))