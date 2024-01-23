func findErrorNums(nums []int) []int {
    var sum, dup int
    n:= len(nums)

    // compute the sum and find the duplicate
    // note that the elements of nums are +ve
    foundDuplicate := false
    for _, x := range nums {
        x1 := abs(x)
        sum += x1
        if !foundDuplicate {
            if nums[x1-1] < 0 {
                dup = x1
                foundDuplicate = true
            } else {
                nums[x1-1] = -nums[x1-1]
            }
        }
    }

    // assemble dup and missing
    sumExpected, sumUniq := n*(n+1)/2, sum - dup
    return []int{dup, sumExpected - sumUniq}
}

func abs(a int) int {
    if a < 0 {
        return -a
    }
    return a
}