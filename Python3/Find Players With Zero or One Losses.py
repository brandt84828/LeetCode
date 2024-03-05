#1
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost = {}
        lost_zero = []
        lost_one = []
        for match  in matches:
            if match[1] in lost:
                lost[match[1]] = lost[match[1]] + 1
            else:
                lost[match[1]] = 1

        for match in matches:
            if lost[match[1]] == 1:
                lost_one.append(match[1])
            if match[0] not in lost and match[0] not in lost_zero:
                lost_zero.append(match[0])
        
        return [sorted(lost_zero), sorted(lost_one)]

#2
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = [0] * 100001

        for winner, loser in matches:
            if losses[winner] == 0:
                losses[winner] = -1

            if losses[loser] == -1:
                losses[loser] = 1
            else:
                losses[loser] += 1

        zero_loss = [i for i in range(1, 100001) if losses[i] == -1]
        one_loss = [i for i in range(1, 100001) if losses[i] == 1]

        return [zero_loss, one_loss]