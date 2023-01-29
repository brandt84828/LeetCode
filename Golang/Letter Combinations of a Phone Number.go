func letterCombinations(digits string) []string {
    res := make([]string, 0)
    sb := ""
    letters := []string {
		" ",    //0
		"",     //1
		"abc",  //2
		"def",  //3
		"ghi",  //4
		"jkl",  //5
		"mno",  //6
		"pqrs", //7
		"tuv",  //8
		"wxyz", //9
	}

    //corner case
    if len(digits) == 0 {
        return res
    }
    dfs(digits, 0, letters, sb, &res)
    return res
}

func dfs(digits string, index int, letters []string, sb string, res *[]string) {
    if index == len(digits) {
        *res = append(*res, sb)
        return
    }

    values := letters[digits[index] - '0']
    for i:=0; i < len(values); i++ {
        sb = sb + string(values[i])
        dfs(digits, index + 1, letters, sb, res)
        sb = sb[0:len(sb)-1]
    }
}



//BFS
func letterCombinations(digits string) []string {
    var res []string
    
    for i := 0; i < len(digits); i++ {
        letters := getLetter(digits[i])
        
        if i == 0 {
            res = append(res, letters...)
            continue
        }
        
        length := len(res)
        
        for i := 0; i < length; i++ {
            for _, letter := range letters {
                res = append(res, res[i]+letter)
            }
        }
        
        res = res[length:]
    }
    
    return res
}

func getLetter(a byte) []string {
    if a == '2' {
        return []string{"a", "b", "c"}
    }
    
    if a == '3' {
        return []string{"d", "e", "f"}
    }
    
    if a == '4' {
        return []string{"g", "h", "i"}
    }
    
    if a == '5' {
        return []string{"j", "k", "l"}
    }
    
    if a == '6' {
        return []string{"m", "n", "o"}
    }
    
    if a == '7' {
        return []string{"p", "q", "r", "s"}
    }
    
    if a == '8' {
        return []string{"t", "u", "v"}
    }
    
    if a == '9' {
        return []string{"w", "x", "y", "z"}
    }
    
    return []string{}
}