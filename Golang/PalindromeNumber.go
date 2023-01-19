func isPalindrome(x int) bool {

    y := x
    tmp := 0

    if x < 0 {
        return false
    }

    for y != 0 {
        tmp = tmp * 10 + y % 10
        y = y / 10
    }

    if x == tmp {
        return true
    }

    return false
    
}