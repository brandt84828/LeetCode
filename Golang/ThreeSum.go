func threeSum(nums []int) [][]int {

    sort.Ints(nums)
    res := make([][]int, 0)

    for i := 0; i < len(nums) - 2; i++ {
        if i == 0 || (i > 0 && nums[i] != nums[i-1]) {
            j, k, target := i + 1, len(nums) - 1, 0 - nums[i]
            for j < k {
                if nums[j] + nums[k] == target {
                    res = append(res, []int{nums[i], nums[j], nums[k]})
                    for j < k && nums[j] == nums[j+1] {
                        j = j + 1
                    }
                    for j < k && nums[k] == nums[k-1] {
                        k = k - 1
                    }
                    j = j + 1
                    k = k - 1
                } else if nums[j] + nums[k] < target {
                    j = j + 1
                } else {
                    k = k - 1
                }
            }
        }
    }
    return res
}