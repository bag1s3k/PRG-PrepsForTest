class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if len(ip := queryIP.split(".")) == 4:
            if [num for num in ip if not num.isnumeric() or not (0 <= int(num) <= 255) or (num[0] == "0" and len(num) > 1)]:
                return "Neither"
            else:
                return "IPv4"
        elif len(ip := queryIP.split(":")) == 8:
            if not [letter for letter in [*ip] if not letter.isalnum()]:
                for ip_part in ip:
                    to_check = ""
                    for letter in ip_part:
                        if letter.isalpha():
                            letter = letter.upper()
                            if letter not in ["A", "B", "C", "D", "E", "F"]:
                                return "Neither"
                        to_check += letter
                    if not (1 <= len(to_check) <= 4):
                        return "Neither"
                return "IPv6"
        return "Neither"

solution = Solution()
print(solution.validIPAddress("172.16.254.1"))
print(solution.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
print(solution.validIPAddress("256.256.256.256"))
print(solution.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334:"))
print(solution.validIPAddress("01.01.01.01"))
print(solution.validIPAddress("0.0.0.0"))