func minimumMoves(s string) int {
    move := 0
    i := 0

    for i < len(s){
        if s[i] == 'X'{
            move++
            i = i + 3
        } else {
            i++
        }
    }
    return  move
}