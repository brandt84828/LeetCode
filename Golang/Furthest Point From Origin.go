func furthestDistanceFromOrigin(moves string) int {
    res := 0
    temp := 0
    for _, v := range moves {
        if v == 'L' {
            res++
        } else if v == 'R' {
            res--
        } else {
            temp++
        }
    }

    return abs(res) + temp
}

func abs(a int) int {
    if a > 0 {
        return a
    }

    return -a
}