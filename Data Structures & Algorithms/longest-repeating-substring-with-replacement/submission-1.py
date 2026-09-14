class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # main idea here is to have to create a window where the k can be valid
        # if k cant exist we shift the left pointer until k can be valid again
        # we can check for a valid solution by doing
        # window - max number <= K

        l, r = 0 , 0
        count = [0] * 26
        longest = 0

        while r < len(s):
            count[ord(s[r]) - ord('A')] += 1    
            window_length = (r-l) + 1
            
            if window_length - max(count) <= k:
                longest = max(longest, window_length)
            else:
                while (r-l+ 1) - max(count) > k :
                    count[ord(s[l]) - ord('A')] -= 1
                    l += 1
            r += 1

        return longest


