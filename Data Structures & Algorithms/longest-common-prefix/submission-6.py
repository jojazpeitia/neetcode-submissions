class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # can use 1 string to compare all others since 
        # we are comparing all others 

        ans = ""

        for i in range(len(strs[0])):
            for string in strs:
                if i == len(string):
                    return ans

                if strs[0][i] != string[i]:
                    return ans
            
            ans += strs[0][i]

        return ans

        