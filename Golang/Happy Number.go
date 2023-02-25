func isHappy(n int) bool {
	visited := make(map[int]bool)
    for n != 1 {
        total := 0
        for n > 0 {
            digit := n % 10
            total = total + digit * digit
            n = n / 10
        }
        if seen := visited[total]; seen {
            return false
        }
        visited[total] = true
        n = total
    }
    return true
}