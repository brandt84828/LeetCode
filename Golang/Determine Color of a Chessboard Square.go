func squareIsWhite(coordinates string) bool {
    x := int(coordinates[0] - 'a') + 1
    y := int(coordinates[1])

    if x % 2 == y % 2 {
        return false
    }
    return true
}