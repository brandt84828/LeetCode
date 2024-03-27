func findDuplicates(nums []int) []int {
    var res []int
    for i:=0;i<len(nums);i++{
        n := abs(nums[i])
        if nums[n-1] < 0 {
            res = append(res,  n)
        } else {
            nums[n - 1] *= -1
        }
    }
    return res
}

func abs(a int) int {
    if a < 0 {
        return -a
    }
    return a
}