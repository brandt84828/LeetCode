func minPatches(nums []int, n int) int {
    covered, res := 0, 0
    for _, num := range nums {
        for num > covered + 1 {
            res++
            covered = 2 * covered + 1
            if covered >= n {
                return res
            }
        }
        covered += num
        if covered >= n {
            return res
        }
    }
    for covered < n {
        res++
        covered = 2 * covered + 1
    }
    return res
}