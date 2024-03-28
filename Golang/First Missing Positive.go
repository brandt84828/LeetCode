func firstMissingPositive(nums []int) int {
    for i, v :=  range nums {
        if v <= 0 {
            nums[i] = 0
        }
    }

    for _, v := range nums {
        index := abs(v) - 1
        if index >= 0 && index < len(nums){
            if nums[index] == 0 {
            nums[index] = math.MinInt
            } else if nums[index] > 0 {
                nums[index] *= -1
            }
        }
    }

    for i, v := range nums {
        if v >= 0 {
            return i + 1
        }
    }
    
    return len(nums) + 1
}

func abs(a int) int {
    if a < 0 {
        return -a
    }
    return a
}