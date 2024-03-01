func findContentChildren(g []int, s []int) int {
	count := 0

        sort.Ints(g)
	sort.Ints(s)


	for _, cookie := range s {
		if count < len(g) && cookie >= g[count] {
			count++
		}
	}

	return count
}