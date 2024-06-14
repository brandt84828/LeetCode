func isNStraightHand(hand []int, groupSize int) bool {
    l := len(hand)
	if l%groupSize != 0 {
		return false
	}
	sort.Ints(hand)

	for i := 0; i < l; i++ {
		if hand[i] == -1 {
			continue
		}
		k := 1
		tmp := hand[i]
		hand[i] = -1
		for j := i + 1; j < l && k < groupSize; j++ {
			if tmp+k == hand[j] && hand[j] != -1 {
				hand[j] = -1
				k++
			}
		}
		if k != groupSize {
			return false
		}
	}
	return true
}