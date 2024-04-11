#1  Moving from left to right, sort the points based on end point.
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        res, curEnd = 1, points[0][1]
        for start,end in points:
            if start>curEnd:
                curEnd = end
                res += 1
        return res

#2  Moving from right to left, sort the points based on start point.
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        print(points)
        res, curStart = 1, points[-1][0]
        for start,end in reversed(points):
            print(end)
            if end<curStart:
                curStart = start
                res += 1
        return res