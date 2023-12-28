func numberOfSteps(num int) int {
    count := 0
    if num > 0 {
        count = -1
    }
    for (num>0) {
        count = count + 1 + (num & 1)
        num >>=1
    }
    return count
}