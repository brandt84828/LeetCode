func specialArray(nums []int) int {
	var mp [1001]int
	for i := 0; i < len(nums); i++ {
		mp[nums[i]]++
	}
	var cnt int
	for i := 1000; i > 0; i-- {
		cnt += mp[i]
		if cnt == i {
			return i
		}
	}
	return -1
}