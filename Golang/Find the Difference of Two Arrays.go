func setDifference(a, b []int) []int {
    d := [2001]bool{}
    ans := []int{}
    for _, x := range b {
        d[x + 1000] = true
    }
    for _, x := range a {
        if !d[x + 1000] {
            ans = append(ans, x)
            d[x + 1000] = true // prevent duplicates from being added
        }
    }
    return ans
}

func findDifference(nums1 []int, nums2 []int) [][]int {
    return [][]int{ setDifference(nums1, nums2), setDifference(nums2, nums1) }
}

//Go dictinary key can't be negative, so need to +1000(base on problem description)