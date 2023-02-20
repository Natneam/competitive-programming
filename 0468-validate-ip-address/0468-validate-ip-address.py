class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if self.validIpv4(queryIP):
            return "IPv4"
        if self.validIpv6(queryIP):
            return "IPv6"
        return "Neither"
    
    def validIpv4(self, address):
        nums = address.split(".")
        if len(nums) != 4:
            return False
        
        for num in nums:
            if (len(num) > 0 and num[0] == '0' and num != '0') or not num.isnumeric()  or not(0 <= int(num) <= 255):
                return False
        return True
    
    def validIpv6(self, address):
        nums = address.split(":")
        if len(nums) != 8:
            return False
        for num in nums:
            if not(1 <= len(num) <= 4):
                return False
            for l in num:
                if l not in "0123456789abcdefABCDEF":
                    return False
        return True