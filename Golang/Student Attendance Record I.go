//1
func checkRecord(s string) bool {
    return strings.Count(s, "A") < 2 && strings.Index(s, "LLL") == -1
}

//2
func checkRecord(s string) bool {
    absent := 0

    for _, ch := range s {

        if ch == 'A' {
            absent += 1
        }

        if absent >= 2 {
            return false
        }
    }


    return !strings.Contains(s, "LLL")
}