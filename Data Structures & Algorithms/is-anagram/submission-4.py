class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_count = [0] * 26
        for c in s:
            s_count[ord(c) - ord('a')] += 1

        t_count = [0] * 26
        for c in t:
            t_count[ord(c) - ord('a')] += 1

        if s_count == t_count:
            return True
        else:
            return False


            


