func findMiddleIndex(nums []int) int {
    totalSum := 0
    for _,v := range nums {
        totalSum += v 
    }
    
    leftSum := 0
    for k, v := range nums {
        totalSum -= v
        if totalSum == leftSum { return k }
        leftSum += v
    }
  
  return -1
}