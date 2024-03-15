func validPath(n int, edges [][]int, source int, destination int) bool {
    adjacency := make(map[int][]int, n-1)
	visited := make(map[int]bool, n-1)

    for _, edge := range edges {
		adjacency[edge[0]] = append(adjacency[edge[0]], edge[1])
		adjacency[edge[1]] = append(adjacency[edge[1]], edge[0])
	}

    q := []int{source}
    visited[source] = true
    for len(q) > 0 {
        node := q[0]
        q = q[1:]
        if node == destination {
            return true
        }
        
        for _, v := range adjacency[node] {
            if !visited[v] {
                visited[v] = true
                q = append(q, v)
            }
        }
    }
    return false
}