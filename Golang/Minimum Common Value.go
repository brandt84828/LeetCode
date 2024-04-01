func getCommon(nums1 []int, nums2 []int) int {
    i := 0
    j :=  0
    res := -1

    for i <  len(nums1) && j < len(nums2) {
        if nums1[i] == nums2[j] {
            res = nums1[i]
            return res
        } else if nums1[i] <  nums2[j] {
            i++
        } else {
            j++
        }
    }
    return res
}