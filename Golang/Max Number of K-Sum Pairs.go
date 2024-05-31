//1
func maxOperations(nums []int, k int) int {
    sort.Ints(nums)
    left, right := 0, len(nums)-1

    count := 0
    for left < right {
        sum := nums[left] + nums[right]
        if sum == k {
            count++
            left++
            right--
        } else if sum < k {
            left++
        } else {
            right--
        }
    }

    return count
}

//2
func maxOperations(nums []int, k int) int {
  count := 0
	m := make(map[int]int)
	for _, num := range nums {
		if v, ok := m[k-num]; ok {
			if v > 0 {
				m[k-num]--
				m[num]--
				count++
			}
		}
		m[num]++
	}
	return count
    
}