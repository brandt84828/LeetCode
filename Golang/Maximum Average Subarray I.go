func findMaxAverage(nums []int, k int) float64 {
    total := 0
    for i := 0; i < k; i++ {
    	total = total + nums[i]    
    }

    maxAvg := total
    index := 0
    for i := k; i < len(nums); i++ {
	total = total + nums[i] - nums[index]
        index++
        if total > maxAvg {
	    maxAvg = total
        }
    }

    return float64(maxAvg) / float64(k)
}



#total can replace by sum += nums[i] - nums[i - k];