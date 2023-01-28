func threeSumClosest(nums []int, target int) int {
    
    sort.Ints(nums)
    res := 0
    diff := math.MaxInt32

    for i := 0; i < len(nums) - 2; i++ {
        j, k := i + 1, len(nums) - 1

        if i > 0 && nums[i] == nums[i-1] {
            continue
        }
        for j < k {
            sum := nums[i] + nums[j] + nums[k]

            if abs(sum - target) < diff {
                diff = abs(sum - target)
                res = sum
            }

            if sum == target {
                return res
            } else if sum < target {
                j = j + 1
            } else {
                k = k - 1
            }
        }
    }
    return res
}

func abs(a int) int {
	if a > 0 {
		return a
	}
	return -a
}