class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        ip = []
        valid = True
        if ":" in queryIP:
            ip = queryIP.split(":")
            for num in ip:
                for letter in str(num):
                    try:
                        num = str(int(letter))
                    except:
                        num = ""
                        num = num.join(letter.upper())
                if 1 <= len(num) <= 4 and int(num, 16) <= 255:
                    valid = True
                else:
                    valid = False
            return "Ipv6" if valid else "Neither"
        elif "." in queryIP:
            ip = [int(item) for item in queryIP.split(".")]
            for num in ip:
                if num <= 255:
                    valid = True
                else:
                    valid = False
            return "Ipv4" if valid else "Neither"
        else:
            return "Neither"
solution = Solution()
print(solution.validIPAddress("172.16.254.1"))
print(solution.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
print(solution.validIPAddress("256.256.256.256"))