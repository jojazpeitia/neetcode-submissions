class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l, r = 0, 0
        longest = 0
        my_set = set()


        while r < len(s):

            if s[r] not in my_set:
                my_set.add(s[r])
                longest = max(len(my_set), longest)
                r += 1
            elif s[r] in my_set:

                while s[l] != s[r]:
                    if s[l] in my_set:
                        my_set.remove(s[l])
                    l += 1

                my_set.remove(s[l])
                l += 1
                my_set.add(s[r])
                longest = max(len(my_set), longest)
                r+=1
        
        return longest
