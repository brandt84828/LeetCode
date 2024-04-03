func transpose(matrix [][]int) [][]int {
  Y, X := len(matrix), len(matrix[0])

  M := make([][]int, X)
  for x := 0; x < X; x++ {
    M[x] = make([]int, Y)
    for y := 0; y < Y; y++ {
      M[x][y] = matrix[y][x]
    }
  }

  return M
}