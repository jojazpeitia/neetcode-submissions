class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # fixed sliding window problem!!
        # create a sliding window of size s1
        # do valid anagram inside that window
        # return true if there a anagram substring, else return false

        if len(s1) > len(s2): return False

        s1list = [0] * 26
        s2window = [0] * 26

        for c in s1:
            s1list[ord(c) - ord('a')] += 1

        l = 0
        r = len(s1) - 1

        # FILL OUT THE WINDOW !!
        for i in range(len(s1)):
            c = s2[i]
            s2window[ord(c) - ord('a')] += 1

        # print(s2window)

        while r < len(s2) - 1:
            if s2window == s1list:
                return True
            
            r += 1
            s2window[ord(s2[r]) - ord('a')] += 1

            s2window[ord(s2[l]) - ord('a')] -= 1
            l += 1

        if s2window == s1list:
            return True 
        else:
            return False
            


