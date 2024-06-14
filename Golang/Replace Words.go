func replaceWords(dictionary []string, sentence string) string {
    roots := make(map[string]bool)
    for _, root := range dictionary {
        roots[root] = true
    }

    words := strings.Split(sentence, " ")
    var result []string

    for _, word := range words {
        found := false
        for i := 1; i <= len(word); i++ {
            prefix := word[:i]
            if _, exists := roots[prefix]; exists {
                result = append(result, prefix)
                found = true
                break
            }
        }

        if !found {
            result = append(result, word)
        }
    }

    return strings.Join(result, " ")
}