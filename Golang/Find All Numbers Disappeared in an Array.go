//1
func findDisappearedNumbers(nums []int) []int {
    var res []int
    for i:=0;i<len(nums);i++{
        temp := abs(nums[i]) - 1
        if nums[temp] > 0{
            nums[temp] *= -1
        }
    }

    for i, v := range nums{
        if v > 0 {
            res = append(res , i+1)
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

//2
func findDisappearedNumbers(nums []int) []int {
    length := len(nums)
    if length == 0 { return nil }
    res := make([]int, length)
    for _, v := range nums {
        res[v-1] = v
    }
    fmt.Print(res)
    j := 0
    for i := 0; i < length; i++ {
        if res[i] == 0 { 
            res[j] = i + 1
            j++
        }
    } 
    return res[:j]
}