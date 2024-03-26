//1 binary search
func findDuplicate(nums []int) int {
    start, end := 1, len(nums)
    for start <= end {
        mid := start + (end-start)/2
        cnt := 0 
        for _, val := range nums {
            if val <= mid {
                cnt++
            }
        }
        if cnt > mid {
            end = mid-1    
        } else {
            start = mid+1 
        }
    }
    return start
}


//2 fast-slow pointer
func findDuplicate(nums []int) int {
    slow := nums[0]
    fast := nums[nums[0]]
    for slow != fast {
        slow = nums[slow]
        fast = nums[nums[fast]]
    }
    fmt.Print(slow)
    fmt.Print(fast)
    fast = 0
    for slow != fast {
        slow = nums[slow]
        fast = nums[fast]
    }
    return fast
}