class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode list of strings into string
        # we use a delimiter

        # ["Hello", "World"]
        # -->
        # "5#Hello5#World"

        encoded_string = ""
        for s in strs:
            length = str(len(s))
            encoded_string += length + "#" + s

        return encoded_string

    def decode(self, s: str) -> List[str]:

        # "5#Hello5#World"
        # -->
        # ["Hello", "World"]
        print(s)

        ans = []

        l = 0
        r = 0

        while r < len(s):
            while s[r] != "#":
                r+=1

            print(l,r)
            length = int(s[l : r])

            string = ""
            for i in range(length):
                r+=1
                string += s[r]
            ans.append(string)

            r += 1
            l = r

        return ans


