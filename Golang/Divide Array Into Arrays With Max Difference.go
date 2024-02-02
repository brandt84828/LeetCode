func divideArray(nums []int, k int) [][]int {
	res:= make([][]int, 0)
	sort.Ints(nums)

    for i:=0 ; i<len(nums) ; i+=3 {
        if i + 2 < len(nums) && nums[i+2] - nums[i] <= k {
            res = append(res, []int{nums[i], nums[i+1], nums[i+2]})
        } else {
            return [][]int{}
        }
    }
    
    return res
}