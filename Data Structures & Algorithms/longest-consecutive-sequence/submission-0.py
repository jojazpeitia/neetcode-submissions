class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        longest = 0

        for value in nums_set:

            if value - 1 not in nums_set:
                length = 0

                while value in nums_set:
                    length += 1
                    value += 1

                if length > longest:
                    longest = length

        return longest