func sortedSquares(nums []int) []int {
    ans := make([]int,len(nums))
    start := 0
    end := len(nums) - 1
    
    for i:=len(nums)-1;i>=0;i--{
        if abs(nums[start]) > abs(nums[end]) {
            ans[i] = nums[start] * nums[start]
            start++
        } else {
            ans[i] = nums[end] * nums[end]
            end--
        }
    }
    return ans
}

func abs(a int) int {
    if a < 0 {
        return -a
    }
    return a
}