//1
func sumOfUnique(nums []int) int {
    count := make(map[int]int, len(nums))
    for _, n := range nums {
        count[n]++
    }
    res := 0
    for k, v := range count {
        if v == 1 {
            res += k
        }
    }
    return res
}

//2
func sumOfUnique(nums []int) int {
    unE := make(map[int]int)
    sum := 0
    for _, num := range nums {
        if unE[num] == 0 {
            sum += num
        } else if unE[num] == 1 {
            sum -= num
        }
        unE[num] += 1
    }
    return sum
}