func findCenter(edges [][]int) int {
    x := edges[0][0]
    y := edges[0][1]
    if x == edges[1][0] || x == edges[1][1]{
        return x
    }
    return y
}