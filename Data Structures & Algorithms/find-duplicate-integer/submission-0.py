class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # floyds algorithm!
        
        # 1. Detect Cycle!
        # 2. From point of detection, we increment by 1 slowly
        #       a. While this is occuring we initilaize a new pointer starting at head that increments by 1 aswell
        # 3. Return the value where these 2 pointers meet

    
        # 1.
        slow, fast = nums[0], nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # 2.
        p1 = 0

        while p1 != slow:
            slow = nums[slow]
            p1 = nums[p1]

        return p1

        