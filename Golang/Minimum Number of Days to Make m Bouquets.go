func minDays(bloomDay []int, m int, k int) int {
    l, r := 1, int(1e9)
    ans := -1
    for l <= r {
        mid := l + (r - l) / 2
        consecutiveLength, bouquets := 0, 0
        for _, bloom := range bloomDay {
            if bloom <= mid {
                consecutiveLength++
                if consecutiveLength >= k {
                    consecutiveLength = 0
                    bouquets++
                }
            } else {
                consecutiveLength = 0
            }
        }
        if bouquets >= m {
            ans = mid
            r = mid - 1
        } else {
            l = mid + 1
        }
    }
    return ans
}