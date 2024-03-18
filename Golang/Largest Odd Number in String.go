//1 Bit Operation
func largestOddNumber(num string) string {
    i := len(num) - 1

    // Since I need to find the odd feather, I iterate until I find it. 
    // Therefore, the condition for iteration is that the number is even
    for i >= 0 && num[i] & 1 == 0 {
        i--
    }

    return num[:i+1]
}

//2
func largestOddNumber(num string) string {
    return strings.TrimRight(num, "02468")
}