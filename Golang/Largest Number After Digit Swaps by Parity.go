//1
func largestInteger(num int) int {
    digits := []byte(strconv.Itoa(num))

    for i, _ := range digits {
        for j := i+1; j < len(digits); j++ {
            if digits[i] %2 == digits[j] %2 && digits[i] < digits[j] {
                digits[i], digits[j] = digits[j], digits[i]
            }
        }
    }

    ans, _ := strconv.Atoi(string(digits))
    return ans    
}

//2

func largestInteger(num int) int {
    if num <= 12 {
		return num
	}

	s := strconv.Itoa(num)
	var odd []byte
	var even []byte

	for i := range s {
		if s[i] & 1 == 1 {
			odd = append(odd, s[i])
		} else {
			even = append(even, s[i])
		}
	}

	sort.Slice(odd, func(i, j int) bool {
		return odd[i] > odd[j]
	})

	sort.Slice(even, func(i, j int) bool {
		return even[i] > even[j]
	})

	r := make([]byte, len(s))

	for i := range s {
		if s[i]&1 == 1 {
			r[i] = odd[0]
			odd = odd[1:]
		} else {
			r[i] = even[0]
			even = even[1:]
		}
	}

	num, _ = strconv.Atoi(string(r))
	return num
}