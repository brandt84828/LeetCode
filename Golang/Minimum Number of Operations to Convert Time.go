func convertTime(current string, correct string) int {
    diff := convertToMinutes(correct) - convertToMinutes(current)
    order := [4]int{60,15,5,1}
    ops := 0
    for i := 0 ; i < 4 ; i++ {
        ops+=(diff/order[i])
        diff%=order[i]
    }

    return ops
}

func convertToMinutes(s string) int {
    split := strings.Split(s, ":")
    hours, _ := strconv.Atoi(split[0])
    minutes, _ := strconv.Atoi(split[1])

    return hours * 60 + minutes 
}