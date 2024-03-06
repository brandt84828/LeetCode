func findMaxLength(nums []int) int {
    maxLen, count := 0, 0
    hash := make(map[int]int)

    for i:=0;i<len(nums);i++ {
        if nums[i] == 0 {
            count -= 1
        } else {
            count += 1
        }

        if count == 0 {
            maxLen = i + 1
        }
        if _, ok := hash[count]; ok {
            if i - hash[count] > maxLen {
                maxLen = i - hash[count]
            }
        } else {
            hash[count] = i
        }
    }
    return maxLen
}