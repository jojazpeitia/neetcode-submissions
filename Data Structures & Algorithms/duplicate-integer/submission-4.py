class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # given array nums

        # return true if any value appears more than once??
        # other wise return false

        my_set = set()

        for i in nums:
            if i in my_set:
                return True
            else: 
                my_set.add(i)

        return False


