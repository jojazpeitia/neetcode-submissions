class Solution:

    def encode(self, strs: List[str]) -> str:

        # delimiter that marks the beggining and end of words
        # we do this by encoding with the a special symbol and the length of the string
        output = ""
        for s in strs:
            output += str(len(s)) + "#" + s

        return output

    def decode(self, s: str) -> List[str]:

        # "2#hi5#world"
        ans = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])

            ans.append(s[j + 1 : j + 1 + length])

            i = j + 1 + length 

        return ans


                
            

