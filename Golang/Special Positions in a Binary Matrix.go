//1
func numSpecial(mat [][]int) int {
    rows := len(mat)
    cols := len(mat[0])
    count := 0
    rowSum := make([]int, rows)
    colSum := make([]int, cols)
    for i := 0; i < rows; i++ {
        for j := 0; j < cols; j++ {
            rowSum[i] += mat[i][j]
            colSum[j] += mat[i][j]
        }
    }
    for i := 0; i < rows; i++ {
        for j := 0; j < cols; j++ {
            if mat[i][j] == 1 && rowSum[i] == 1 && colSum[j] == 1 {
                count++
            }
        }
    }

    return count
}

//2
func numSpecial(mat [][]int) int {
    rows, columns := len(mat),len(mat[0])
    specials := 0
    for i := 0; i < rows; i++ {
        checkCol := -1
        for j := 0; j < columns; j++ {
            if mat[i][j] == 1 {
                if checkCol == -1 {
                    checkCol = j
                } else {
                    checkCol = -1
                    break
                }
            }
        }
        if checkCol == -1 {
            continue
        }
        special := 1
        for k := 0; k < rows; k++ {
            if k == i {
                continue
            }
            if mat[k][checkCol] == 1 {
                special = 0
				mat[0][checkCol] = 1  // speed up future checkings
                break
            }
        }
        specials += special
    }
    return specials 
}