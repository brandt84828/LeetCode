func isPowerOfTwo(n int) bool {
    count := 0
    for n > 0 {
        count += (n & 1)
        n = n >> 1
    }
    return count == 1
}