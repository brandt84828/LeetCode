func areaOfMaxDiagonal(dimensions [][]int) int {
    maxArea := 0
    maxDiagonal := 0

    for i, _ := range dimensions{
        area := dimensions[i][0] * dimensions[i][1]
        diagonal := dimensions[i][0] * dimensions[i][0] + dimensions[i][1] * dimensions[i][1]

        if diagonal > maxDiagonal || (diagonal == maxDiagonal && area > maxArea){
            maxDiagonal = diagonal
            maxArea = area
        }
    }

    return maxArea

}