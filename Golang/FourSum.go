func fourSum(nums []int, target int) [][]int {

    //corner case
    if len(nums) < 4 {
        return [][]int{}
    }
    sort.Ints(nums)
    res := make([][]int, 0)

    for i:=0; i < len(nums)-3; i++ {
        if i > 0 && nums[i] == nums[i-1] {
	    //avoid duplicate res
            continue
        }
        for j:=i+1; j < len(nums)-2;j++ {
            if j > i + 1 && nums[j] == nums[j-1] {
		//avoid duplicate res
                continue
            }
            left := j + 1
            right := len(nums) - 1
            find := target - nums[i] - nums[j]
            for left < right {
                if nums[left] + nums[right] < find {
                    left = left + 1
                } else if nums[left] + nums[right] > find {
                    right = right - 1
                } else {
                    res = append(res,[]int{nums[i], nums[j], nums[left], nums[right]})
                    left = left + 1
                    for left < right && nums[left] == nums[left-1] {
                        left = left + 1
                    }
                }
            }
        }
    }
    return res
}