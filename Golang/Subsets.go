func subsets(nums []int) [][]int {
    var queue [][]int
    queue = append(queue, []int{})
    
    for i := 0; i < len(nums); i++ {
        length := len(queue)
        
        for j := 0; j < length; j++ {
            item := queue[j]
            
            tmp := make([]int, len(item))
            copy(tmp, item)
            tmp = append(tmp, nums[i])
            
            queue = append(queue, tmp)
        }
    }
    
    return queue
}