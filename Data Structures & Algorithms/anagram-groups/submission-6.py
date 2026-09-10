class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        # create a list that captures the count of characters in a word
        # use that list as a key 
        # attach the word to be the value

        # return the list of all values

        my_dict = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            my_dict[tuple(count)].append(s)

        ans = []

        for i in my_dict.values():
            ans.append(i)

        return ans

            

        