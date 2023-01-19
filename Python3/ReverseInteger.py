class Solution:
    def reverse(self, x: int) -> int:

        tmp = 0
        sign = True
        if (x < 0):
            sign = False
            x = x * -1

        while (x != 0):
            tmp = tmp * 10 + x % 10
            x = x // 10

        if (sign == False):
            tmp = tmp * -1
            
        if (tmp > 2 ** 31 - 1 or tmp < -2 ** 31):
            return 0

        return tmp


#Tips： 正負數的取餘數，Python算餘數的方式不一樣 (處理負數要注意)
#一般程序是用： Truncated Division
#可是Python用： Floored Division