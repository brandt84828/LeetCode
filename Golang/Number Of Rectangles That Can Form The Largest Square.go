func countGoodRectangles(rectangles [][]int) int {
    cnt := 0
    max := 0

    for _, v := range rectangles {
        side := 0
        if v[0] > v[1] {
            side = v[1]
        } else {
            side = v[0]
        }

        if side > max {
            cnt = 1
            max = side
        } else if side == max {
            cnt++
        }
    }
    return cnt
}