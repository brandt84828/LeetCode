func canPlaceFlowers(flowerbed []int, n int) bool {
    count := 0
    for i:=0;i<len(flowerbed);i++ {
        if flowerbed[i] == 0 {
            empty_left_plot := (i == 0) || (flowerbed[i-1] == 0)
            empty_right_plot := (i == len(flowerbed)-1) || (flowerbed[i+1] == 0)

            if empty_left_plot && empty_right_plot {
                flowerbed[i] = 1
                count = count + 1
                if count >= n {
                    return true
                }
            }
        }
    }

    return count >= n
}