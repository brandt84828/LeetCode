func twoSum(nums []int, target int) []int {

    m := make(map[int]int)

    for i := 0; i < len(nums); i++ {
        diff := target - nums[i]

        if _, ok := m[diff]; ok {
            return []int{m[diff],i}
        } else {
            m[nums[i]] = i
        }
    }
    
    return nil
}