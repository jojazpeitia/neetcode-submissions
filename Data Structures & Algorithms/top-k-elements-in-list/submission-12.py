class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_list = [[] for i in range(len(nums) + 1)]

        occurances = defaultdict(int)
        for i in nums:
            occurances[i] += 1

        for key in occurances:
            index  =  occurances[key]
            count_list[index].append(key)

        ans = []  
        for list_item in reversed(count_list):
            for num in list_item:
                if len(ans) == k:
                    return ans
                ans.append(num)

        return ans

        



            

