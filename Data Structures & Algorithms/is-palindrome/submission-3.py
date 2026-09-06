class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newString = ""

        for c in s: 
            if c.isalnum():
                newString += c.lower()

        print(newString)

        l = 0
        r = len(newString) - 1

        while l < r:
            if newString[l] != newString[r]:
                return False
            l+=1
            r -= 1

        return True

        # return newString == newString[-1]

