func searchRange(nums []int, target int) []int {
    return []int{lower_bound(nums, target), upper_bound(nums, target)}
}

func lower_bound(nums []int, target int) int {
    l, r := 0, len(nums) - 1
    for l <= r {
        mid := l + (r - l) / 2
        if nums[mid] < target {
            l = mid + 1
        } else {
            r = mid - 1
        }
    }
    if l >= 0 && l < len(nums) && nums[l] == target {
        return l
    } else {
        return -1
    }
}

func upper_bound(nums []int, target int) int {
    l, r := 0, len(nums) - 1
    for l <= r {
        mid := l + (r - l) / 2
        if nums[mid] <= target {
            l = mid + 1
        } else {
            r = mid - 1
        }
    }
    if r >= 0 && r < len(nums) && nums[r] == target {
        return r
    } else {
        return -1
    }   
}