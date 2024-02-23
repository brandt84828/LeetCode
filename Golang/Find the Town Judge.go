func findJudge(n int, trust [][]int) int {
    count := make([]int, n + 1)
    for _, v := range trust {
        count[v[0]]--
        count[v[1]]++
    }

    for i:=1;i<=n;i++ {
        if count[i] == n-1 {
            return i
        }
    }

    return -1
}