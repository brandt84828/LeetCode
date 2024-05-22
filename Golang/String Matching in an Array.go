func stringMatching(words []string) []string {
    res := []string{}
    key := make(map[string]int)

    for i, s := range words {
        for j, str := range words {
            if i != j {
                if strings.Contains(s, str){
                    key[str]++
                }
            }
        }
    }


    for k := range key{
        res = append(res, k)
    }

   return res
}