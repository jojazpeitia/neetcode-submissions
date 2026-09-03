class Solution:

    # we should implement a delimiter here!!
    # gonna use number followed by the pound symbol 
    # encoding should be easy...
    # thats where we add the delimiter appendment

    def encode(self, strs: List[str]) -> str:

        output = ""
        for i in strs:
            output += str(len(i)) + "#" + i
        return output

    def decode(self, s: str) -> List[str]:
        
        # "5#hello5#world"
        # ^ ["hello","world"]
        ans = []
        i = 0

        while i < len(s):

            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])

            ans.append(s[j + 1 : j + 1 + length])

            i = j + 1 + length

        return ans
