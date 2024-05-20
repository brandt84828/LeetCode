//1
func convert(s string, numRows int) string {
	if numRows <= 1 {
		return s
	}

	// character distance between columns
	colStep := numRows + numRows - 2

	// result
	ss := make([]uint8, len(s), len(s))
	// fill result with dots to make debugging easier
	//for i := 0; i < len(ss); i++ {
	//	ss[i] = '.'
	//}

	// diagStep is distance from column to diagonal value.
	// Reduces by two for each row
	diagStep := colStep - 2

	// i = position to write to in ss
	i := 0
	for row := 0; row < numRows; row = row + 1 {
		// does this row have diagonal cells?
		diag := row > 0 && row < numRows-1
		for j := row; j < len(ss); j += colStep {
			ss[i] = s[j] // column value
			i += 1
			if diag && j+diagStep < len(s) {
				ss[i] = s[j+diagStep] // diagonal value
				i += 1
			}
		}
		if diag {
			diagStep -= 2
		}
	}

	return string(ss)
}


//2
import (
    "strings"
)

func convert(s string, numRows int) string {
    rows := make([]strings.Builder, numRows)
    
    idx := 0
    for idx < len(s) {
        for i := 0; i < numRows && idx < len(s); i++ {
            rows[i].WriteByte(s[idx])
            idx++
        }
        for j := numRows-2; 0 < j && idx < len(s); j-- {
            rows[j].WriteByte(s[idx])
            idx++
        }
    }
    
    var zigzag strings.Builder
    for _, r := range rows {
        zigzag.WriteString(r.String())
    }
    
    return zigzag.String()
}