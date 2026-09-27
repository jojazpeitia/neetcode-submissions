class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # loop through the first word!
        # since we are bounded by the soluition requiring all strinsg to have the same common prefix, we can do it

        ans = ""

        for i in range(len(strs[0])):
            for string in strs:

                # if we reach the end of the string we return
                if i == len(string):
                    return ans

                if string[i] != strs[0][i]:
                    return ans
            ans += strs[0][i]

        return ans
