//1
func isUgly(n int) bool {
    for n >= 1 {
        if n % 2 == 0 {
            n = n / 2
        } else if n % 3 == 0 {
            n = n / 3
        } else if n % 5 == 0 {
            n = n / 5
        } else if n == 1 {
            return true
        } else {
            return false
        }
    }

    return false
}

//2
func isUgly(num int) bool {
    if num <=0{
        return false
    }
    
    for num!=1{
        if num%2==0{
            num/=2
        }else if num%3==0{
            num/=3
        }else if num%5==0{
            num/=5
        }else{
            return false
        }
    }
    
    return true
}

//3
func isUgly(n int) bool {
    if n <= 0 {
        return false
    }

    for n % 5 == 0 {
        n /= 5
    }
    for n % 3 == 0 {
        n /= 3
    }
    for n % 2 == 0 {
        n /= 2
    }

    return n == 1
}