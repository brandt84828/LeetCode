//1
func maximumOddBinaryNumber(s string) string {
    n := len(s)
    oneCnt := strings.Count(s, "1")
    zeroCnt := n-oneCnt
    return strings.Repeat("1", oneCnt-1) + strings.Repeat("0", zeroCnt) + "1"
}

//2
func maximumOddBinaryNumber(s string) string {
    ones := strings.Count(s, "1")

	startedOnes := ones - 1
	v := make([]byte, len(s))
	for i := 0; i < len(s); i++ {
		if i < startedOnes {
			v[i] = '1'
			continue
		}

		v[i] = '0'

	}

	v[len(v)-1] = '1'

	return string(v)
}