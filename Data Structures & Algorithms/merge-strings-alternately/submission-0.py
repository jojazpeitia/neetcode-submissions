class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        newString = ""

        p1, p2 = 0, 0

        while p1 < len(word1) and p2 < len(word2):
            newString += word1[p1]
            newString += word2[p2]
            p1 += 1
            p2 += 1

        # if word1 still has words
        while p1 < len(word1):
            newString += word1[p1]
            p1 += 1

        while p2 < len(word2):
            newString += word2[p2]
            p2 += 1

        return newString
            


        