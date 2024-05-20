#1
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
         # Prepare a medal list, an empty result list and an empty dictionary
        Medal = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        size = len(score)
        res = [""]*size
        my_map = {}
        
        # Set the dictionary
        # Key is the number, value is the index of the number in the orginal input list
        for i in range(size):
            my_map[score[i]] = i
            
        # Sort the input list in the descending order
        score.sort(reverse=True)
        
        # Set the result list using the sorted input list and the dictionary
        for i in range(size):
            if i < 3:
                res[my_map[score[i]]] = Medal[i]            
            else:
                res[my_map[score[i]]] = str(i+1)
                
        return res

#2
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rankings = []
        for i, val in enumerate(score):
            heappush(rankings, (-val, i))
        ans = [''] * len(score)
        r = 1
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        while len(rankings) != 0:
            _, i = heappop(rankings)
            if r <= 3:
                ans[i] = rank[r-1]
            else:
                ans[i] = f'{r}'
            r += 1
        return ans