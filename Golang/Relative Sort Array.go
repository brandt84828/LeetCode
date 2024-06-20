//1
func rank(mp map[int]int, a int) int {
	if val, ok := mp[a]; ok {
		return val
	}
	return len(mp)
}

func relativeSortArray(arr1 []int, arr2 []int) []int {
    mp := make(map[int]int)
	for i, num := range arr2 {
		mp[num] = i
	}

	sort.Slice(arr1, func(i, j int) bool {
		rankA := rank(mp, arr1[i])
		rankB := rank(mp, arr1[j])
		if rankA == rankB {
			return arr1[i] < arr1[j]
		}
		return rankA < rankB
	})

	return arr1
}

//2
func relativeSortArray(arr1 []int, arr2 []int) []int {
    arr2Set := make([]int, 1001)
    
    for _, num := range arr2 {
        arr2Set[num]++
    }
    
    countMap := make([]int, 1001)
    
    var remainingArr []int
    
    for _, num := range arr1 {
        if arr2Set[num] == 0 {
            remainingArr = append(remainingArr, num)
        } else {
            countMap[num]++
        }
    }
    
    sort.Ints(remainingArr)
    
    var res []int
    
    for _, num := range arr2 {
        for i := 0; i < countMap[num]; i++ {
            res = append(res, num)
        }
    }
    
    res = append(res, remainingArr...)
    
    return res
}