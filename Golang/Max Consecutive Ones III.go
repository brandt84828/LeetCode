func longestOnes(nums []int, k int) int {
    var res int
    
    numberOfOnes, windowBegin := 0, 0
    
    for windowEnd := 0; windowEnd < len(nums); windowEnd++ {
        if nums[windowEnd] == 1 {
            numberOfOnes++
        }
        
        for windowEnd - windowBegin + 1 - numberOfOnes > k {
            if nums[windowBegin] == 1 {
                numberOfOnes--
            }
            
            windowBegin++
        }
        
        if windowEnd - windowBegin + 1  > res {
            res = windowEnd - windowBegin + 1 
        }
    }
    
    return res
}