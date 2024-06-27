func maxProfitAssignment(difficulty []int, profit []int, worker []int) int {
    res, j, best := 0, 0, 0
    temp := make([]pair, len(worker))

    for i := range worker {
        temp[i] = pair{difficulty[i], profit[i]}
    }

    sort.Slice(temp, func(i, j int) bool {
        return temp[i].difficulty < temp[j].difficulty
    })
    sort.Ints(worker)

    for _, work := range worker {
        for j < len(temp) && work >= temp[j].difficulty {
            best = max(best, temp[j].profit)
            j++
        }
        res += best
    }

    return res
}

type pair struct {
    difficulty, profit int
}