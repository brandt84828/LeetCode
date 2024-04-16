func trap(height []int) int {
	left, right := 0, len(height)-1
	leftMax, rightMax, ans := 0, 0, 0
	for left <= right {
		if height[left] < height[right] {
			if leftMax > height[left] {
				ans = ans + (leftMax - height[left])
			} else {
				leftMax = height[left]
			}
			left++
		} else {
			if rightMax > height[right] {
				ans = ans + (rightMax - height[right])
			} else {
				rightMax = height[right]
			}
			right--
		}
	}
	return ans
}