func minIncrementForUnique(nums []int) int {
    // Sort the slice first
	sort.Ints(nums)

	numTracker := 0   // Tracks the next unique number that should be set.
	minIncrement := 0 // Counts the total increments required.

	for _, num := range nums {
		if numTracker < num {
			numTracker = num
		}
		minIncrement += numTracker - num
		numTracker++ // Increment the tracker for the next number.
	}

	return minIncrement
}