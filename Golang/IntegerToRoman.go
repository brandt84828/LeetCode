func intToRoman(num int) string {
    symbol := []string{"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"}
    nums := []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}
    ans := ""

    for i:=0; i < len(nums); i++ {
        if num >= nums[i] {
            repeat := num / nums[i]
            for j:=1; j <= repeat; j++ {
                ans = ans + symbol[i]
            }
            num = num % nums[i]
        }
    }

    return ans
}