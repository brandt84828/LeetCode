func countSubarrays(nums []int, k int) int64 {
    max := 0
    for _, v := range nums {
        if v > max {
            max = v
        }
    }

    cur, i := 0 ,0
    var res int64 = 0
    for j:=0;j<len(nums);j++ {
        if nums[j] == max {
            cur += 1
        }
        for cur >= k {
            if nums[i] == max {
                cur -= 1
            }
            i += 1
        }
        res += int64(i)
    }
    return res
}