class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people = sorted(people)

        l, r = 0, len(people) - 1
        numberOfBoats = 0

        while l <= r:
            if l == r:
                numberOfBoats += 1
                break
            sumOfWeight = people[l] + people[r]
            if sumOfWeight > limit:
                numberOfBoats += 1
                r -= 1
            else:
                numberOfBoats += 1
                l += 1
                r -= 1

        return numberOfBoats 