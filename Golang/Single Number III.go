func singleNumber(nums []int) []int {
    xor, a, b := 0, 0, 0
    for _, n := range nums {
        xor ^= n
    }
    diff := xor & -xor
    
    for _, n := range nums {
        if n & diff == 0 {
            a ^= n
        } else {
            b ^= n
        }
    }

    return []int{a, b}
}