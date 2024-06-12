func appendCharacters(s string, t string) int {
	lenS, lenT, indexT, indexS := len(s), len(t), 0, 0
	for indexS < lenS && indexT < lenT {
		if s[indexS] == t[indexT] {
			indexT++
		}
		indexS++
	}
	return lenT - indexT
}