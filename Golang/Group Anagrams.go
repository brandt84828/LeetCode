//1
func groupAnagrams(strs []string) [][]string {
	kb := make(map[string][]string)

	for _, str := range strs {
		key := sortString(str)
		if _, ok := kb[key]; !ok {
			kb[key] = []string{}
		}

		kb[key] = append(kb[key], str)
	}

	res := make([][]string, len(kb))
	i := 0
	for _, anagrams := range kb {
		res[i] = anagrams
		i++
	}

	return res
}

func sortString(str string) string {
	strArr := strings.Split(str, "")
	sort.Strings(strArr)
	return strings.Join(strArr, "")
}

//2
func word_stats(w string) [26]uint16 {
  res := [26]uint16{}
  for _, c := range w {
    res[c - 'a']++
  }
  
  return res
}

func groupAnagrams(words []string) [][]string {
  data := map[[26]uint16][]string{}
  
  for _, w := range words {
    stats := word_stats(w)
    data[stats] = append(data[stats], w)
  }
  
  res, p := make([][]string, len(data)), 0
  for _, val := range data {
    res[p] = val
    p++
  }
  return res
}