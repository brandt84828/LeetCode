func makeConnected(n int, connections [][]int) int {
    if len(connections) < n-1 {
        return -1
    }
    g := make([][]int, n)
    for _, conn := range connections {
        g[conn[0]] = append(g[conn[0]], conn[1])
        g[conn[1]] = append(g[conn[1]], conn[0])
    }
    visited := make([]int, n)
    total := 0

    for i:=0; i < n; i++ {
        total = total + dfs(i, g, visited)
    }
    return total - 1
}

func dfs(node int, g [][]int, visited []int) int {
    if visited[node] == 1 {
        return 0
    }
    visited[node] = 1
    for _, i := range g[node] {
        dfs(i, g, visited)
    }
    return 1
}