func sortColors(nums []int)  {
    nZeros, nOnes, nTwos := 0, 0, 0
    
    for i := 0; i < len(nums); i++ {
        if nums[i] == 0 {
            nZeros++
        } else if nums[i] == 1{
            nOnes++
        } else {
            nTwos++
        }
    }
    
    i := 0

    for nZeros > 0 {
        nums[i] = 0
        nZeros--
        i++
    }
    
    for nOnes > 0 {
        nums[i] = 1
        nOnes--
        i++
    }
    
    for nTwos > 0 {
        nums[i] = 2
        nTwos--
        i++
    }
}