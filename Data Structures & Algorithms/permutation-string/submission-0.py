class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1count, s2count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1count[ ord(s1[i]) - ord('a')] += 1
            s2count[ ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(len(s2count)):
            if s2count[i] == s1count[i]:
                matches += 1
        

        l = 0
        r = len(s1) - 1
        

        print(s1count)
        print(s2count)

        while r < len(s2) - 1:
            if matches == 26: 
                return True

            r += 1
            index = ord(s2[r]) - ord('a')
            s2count[index] += 1

            if s2count[index] == s1count[index]:
                matches += 1
            elif s2count[index] == s1count[index] + 1:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2count[index] -= 1

            if s2count[index] == s1count[index]:
                matches += 1
            elif s2count[index] == s1count[index] - 1:
                matches -= 1

            l += 1

        return matches == 26