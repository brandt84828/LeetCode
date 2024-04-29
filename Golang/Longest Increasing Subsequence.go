func lengthOfLIS(nums []int) int {
    //binary search with tail array
    tail := []int{}
    idx := 0
    for _, num := range nums {
        idx = binarySearch(tail, num)
        if idx == len(tail) {
            tail = append(tail, num)
        } else {
            tail[idx] = num
        }
    }
    return len(tail)
}

func binarySearch(tail []int, target int) int {
    n := len(tail)
    left, right := 0, n
    for left < right {
        mid := left + (right - left) / 2
        if tail[mid] < target {
            left = mid+1
        } else if tail[mid] > target {
            right = mid
        } else {
            return mid
        }
    }
    return left
}