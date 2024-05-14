//1
func sumOfBeauties(nums []int) int {
    right :=make([]int,len(nums))
    for j:=len(nums)-2;j>=0;j-- {
      if j==len(nums)-2 {
        right[j]=nums[j+1]
      }else {
        if nums[j+1]<right[j+1] {
          right[j]=nums[j+1]
        }else {
          right[j]=right[j+1]
        }
      }
    }

    max := nums[0]
    sum :=0
    for i:=1;i<=len(nums)-2;i++ {
      if max<nums[i] && nums[i]<right[i] {
        sum+=2
      }else if nums[i-1]<nums[i] && nums[i]<nums[i+1] {
        sum+=1
      }

      if nums[i]>max {
        max=nums[i]
      }


    }

    return sum

}


//2
func sumOfBeauties(nums []int) int {
    right :=make([]int,len(nums))
    for j:=len(nums)-2;j>=0;j-- {
      if j==len(nums)-2 {
        right[j]=nums[j+1]
      }else {
        if nums[j+1]<right[j+1] {
          right[j]=nums[j+1]
        }else {
          right[j]=right[j+1]
        }
      }
    }

    max := nums[0]
    sum :=0
    for i:=1;i<=len(nums)-2;i++ {
      if max<nums[i] && nums[i]<right[i] {
        sum+=2
      }else if nums[i-1]<nums[i] && nums[i]<nums[i+1] {
        sum+=1
      }

      if nums[i]>max {
        max=nums[i]
      }


    }

    return sum

}