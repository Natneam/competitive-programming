class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        """
        remove all the hyphes from the string and put every other chracter in a list
        capitalize every letter
        start from the end of the array and make a string of k sized until running out of character
        attach all the strings with hypehn 
        reverse the attached string
        """
        arr = [x.upper() for x in s if x != "-"]
        end = len(arr)
        start = len(arr) - k
        ans = []
        while end > 0:
            if start < 0:
                ans.append("".join(arr[0:end]))
            else:
                ans.append("".join(arr[start:end]))
            end = start
            start = start - k
        # print(ans)
        return "-".join(reversed(ans))