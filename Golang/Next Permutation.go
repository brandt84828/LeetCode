func nextPermutation(nums []int)  {
    length := len(nums)
    var peakIndex int = length-1
    var largeIndex int = length-1

    // Find the final index of increasing order
    for ; peakIndex > 0; peakIndex-- {
        if nums[peakIndex-1] < nums[peakIndex] {
            break
        }
    }

    // Find the largest element from the right of peak, when compared to the
    // element immediate left of the peak (peakIndex - 1)
    if peakIndex != 0 {
        for ; largeIndex >= peakIndex; largeIndex-- {
            if nums[peakIndex-1] < nums[largeIndex] {
                // Swap the elements, peakIndex-1 & largeIndex.
                nums[largeIndex], nums[peakIndex-1] = nums[peakIndex-1], nums[largeIndex]
                break
            }
        }
    }

    // Reverse the order of elements starting from the end of the array, 
    // uptill the peak
    for i:=length-1; i>peakIndex; i, peakIndex = i-1, peakIndex+1 {
        nums[i], nums[peakIndex] = nums[peakIndex], nums[i]
    }
}