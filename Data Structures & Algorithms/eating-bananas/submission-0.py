class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # our default min is always going to be the biggest item in the list!
        # the eating rate can be infinitely big, which will give correct answer, but we need to work towards finidng the 
        # min
        
        # the biggest pile can be our default min rate
        # then from there we loop from the range of 1 to biggest pile

        # we can see current ith rate passes h, whenever it does, compare it to the min
        # do this until we checked every rate
        # ^ BUT we can avoid checking "every" rate by doing binary search

        biggest_pile = max(piles)
        min_k = biggest_pile

        l, r = 1, biggest_pile

        while l <= r:
            # math.ceil()
            k_rate = (r + l) // 2

            time_to_eat = 0
            for i in piles:
                time_to_eat += math.ceil(i / k_rate)

            # if time to eat is valid, update kth rate
            # look towards left to look for more small ones

            # else look towards right to look for a valid rate

            if time_to_eat <= h:
                min_k = min(k_rate, min_k)
                r = k_rate - 1
            elif time_to_eat > h:
                l = k_rate + 1

        return min_k



            

