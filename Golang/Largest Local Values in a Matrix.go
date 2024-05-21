func largestLocal(grid [][]int) [][]int {
	n := len(grid)
	ans := make([][]int, n-2)  //intializing to store answer
	for i := 0; i < len(grid)-2; i++ {
		ans[i] = make([]int, n-2)           //initailizing to store ans for one 3*3
		for j := 0; j < len(grid[i])-2; j++ {
			a := 0
			for k := i; k < i+3; k++ {          
				for d := j; d < j+3; d++ {
					if grid[k][d] > a {
						a = grid[k][d]       //iterating over all elements in 3*3 
					}
				}
			}
			ans[i][j] = a
		}
	}
	return ans
}