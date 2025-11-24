class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        template = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        if len(digits) == 1:
            return list(template[digits])

        final_list = []
        def fnc(index, current_combination):
            if index == len(digits):
                final_list.append(current_combination)
                return

            for letter in template[digits[index]]:
                fnc(index + 1, current_combination + letter)

        fnc(0, "")
        return final_list

solution = Solution()
print(solution.letterCombinations("23"))
print(solution.letterCombinations(""))
print(solution.letterCombinations("2"))