func numSteps(s string) int {
    var meetOne bool
    ans := 0
    for i := len(s) - 1; i >= 0; i--{
        if s[i] == '0'{
            if meetOne{
                ans += 2
            }else{
                ans++
            }
        }else{
            if meetOne{
                ans++
            }else{
                if i != 0{
                    ans += 2
                }
                meetOne = true
            }
        }
    }
    return ans
}