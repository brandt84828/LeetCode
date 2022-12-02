package main

import "fmt"

type A struct {
	Name string
	Age  int
}

type B struct {
	Name string
	Age  int
}

type C struct {
	A
	B
}

type D struct {
	a A //?????
}

type Goods struct {
	Name  string
	Price float64
}

type Brand struct {
	Name    string
	Address string
}

type TV struct {
	Goods
	Brand
}

type TV2 struct {
	*Goods
	*Brand
}

// ??C????????????,?C???????????????????,????????????????,?????
func main() {
	var c C

	//Error
	//c.Name = "cris"
	//fmt.Println(c.Name)

	//Correct
	c.A.Name = "cris"
	fmt.Println(c.A.Name)

	var d D
	//Error,????????????????
	//d.Name = "Jack"

	//Correct,?????????????????????????
	d.a.Name = "jack"

	//??????????????????(??)?,???????????????

	tv := TV{Goods{"TV001", 5000.99}, Brand{"ABC", "Taipei"}}

	tv2 := TV{
		Goods{
			Price: 5000.99,
			Name:  "TV002",
		},
		Brand{
			Name:    "ABC",
			Address: "Taipei",
		},
	}
	fmt.Println(tv)
	fmt.Println(tv2)

	tv3 := TV2{&Goods{"TV003", 7000.99}, &Brand{"DEF", "Tainan"}}
	fmt.Println(*tv3.Goods, *tv3.Brand)
}
