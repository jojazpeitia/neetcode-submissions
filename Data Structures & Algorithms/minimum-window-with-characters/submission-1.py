class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        # variable length window problem!

        window, t_map = defaultdict(int), defaultdict(int)

        for c in t:
            t_map[c] += 1

        have, need = 0, len(t_map)
        
        minimum = float("infinity")



        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in t_map and window[c] == t_map[c]:
                have += 1
            
            while have == need:
                # if a minimum was found we need to save the variables
                # for we can properly make our output
                window_size = (r - l) + 1
                if window_size < minimum:
                    minimum = window_size
                    minimum_l = l
                    minimum_r = r

                window[s[l]] -= 1
                if s[l] in t_map and window[s[l]] < t_map[s[l]]:
                    have -= 1
                l+=1
        
        if minimum == float("infinity"):
            return ""
        else:
            return s[minimum_l : minimum_r + 1]

            

                

                


            


            

        



