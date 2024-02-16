class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        cnt = mx = 0
        for l, w in rectangles:
            side = min(l, w)
            if side > mx:
                cnt, mx = 1, side
            elif side == mx:
                cnt += 1
        return cnt