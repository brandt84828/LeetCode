func generateParenthesis(n int) []string {
    var res []string
    dfs(&res, 0, 0, "", n)
    return res
}

func dfs(res *[]string, left int ,right int, s string, n int) {
    if len(s) == n * 2 {
        *res = append(*res, s)
        return
    }

    if left < n {
        dfs(res, left + 1, right, s + "(", n)
    }
    if right < left {
        dfs(res, left , right + 1, s + ")", n)
    }

}