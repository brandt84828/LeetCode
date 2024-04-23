func islandPerimeter(grid [][]int) int {
    m := len(grid)
    n := len(grid[0])
    perimeter := 0

    for i:=0;i<m;i++{
        for j:=0;j<n;j++{
            perimeter += 4*grid[i][j]
            if i > 0 {
                perimeter -= grid[i][j] * grid[i-1][j]
            }
            if i < m-1 {
                perimeter -= grid[i][j] * grid[i+1][j]
            }
            if j > 0 {
                perimeter -= grid[i][j] * grid[i][j-1]
            }
            if j < n-1 {
                perimeter -= grid[i][j] * grid[i][j+1]
            }
        }
    }
    return perimeter
}