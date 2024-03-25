func sortByBits(arr []int) []int {
    sort.Slice(arr, func(i, j int) bool {
        iCount, jCount := getBit1Count(arr[i]), getBit1Count(arr[j])
        if iCount == jCount {
            return arr[i] < arr[j]
	    // same bit -> compare original value
        }
        return iCount < jCount
    })
    return arr
}

func getBit1Count(val int) (count int) {
    for val != 0 {
        count += val & 0x1
        val >>= 1
    }
    return
}