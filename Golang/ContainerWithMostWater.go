func maxArea(height []int) int {
    
    l, r, maxArea := 0, len(height) - 1, 0

    for l < r {
        width := r - l
        maxArea = max(maxArea, min(height[l], height[r]) * width)

        if height[l] <= height[r] {
            l = l + 1
        } else {
            r = r - 1
        }
    }
    
    return maxArea
}

func max(a int, b int) int {
    if a < b {
        return b
    }
    return a
}

func min(a int, b int) int {
    if a < b {
        return a
    }
    return b
}