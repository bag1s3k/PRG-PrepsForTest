class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        tmp = {}
        for string in strs:
            key = "".join(sorted(string))
            if key not in tmp:
                tmp[key] = []
            tmp[key].append(string)

        return list(tmp.values())

solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(solution.groupAnagrams([""]))
print(solution.groupAnagrams(["a"]))