class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        # We shall find the first number in a sequence!!

        # We first throw these numbers into a set 
        # ^ problem doesnt specify but repeats dont count for longest consecutive

        number_set = set()

        for i in nums:
            number_set.add(i)

        longest = 0
        for index, num in enumerate(number_set):
            if (num - 1) in number_set:
                continue
            else:
                cur = num

                length = 0
                while cur in number_set:
                    length += 1
                    longest = max(longest, length)
                    cur += 1

        return longest
                




        