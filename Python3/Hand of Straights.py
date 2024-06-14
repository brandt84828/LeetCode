class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c = collections.Counter(hand)
        for i in sorted(c):
            if c[i] > 0:
                for j in range(groupSize)[::-1]:
                    c[i + j] -= c[i]
                    if c[i + j] < 0:
                        return False
        return True

#Count number of different cards to a map c
#Loop from the smallest card number.
#Everytime we meet a new card i, we cut off i - i + W - 1 from the counter.