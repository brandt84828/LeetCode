package main

import "fmt"

func main() {
	var x interface{}
	var b float32 = 1.1
	x = b //empty interface can accept any type

	//這樣寫不會因為類型轉換失敗而直接結束程式
	if y, ok := x.(float32); ok {
		fmt.Printf("y的類型是%T,值是%v", y, y)
	} else {
		fmt.Println("convert fail")
	}

}
