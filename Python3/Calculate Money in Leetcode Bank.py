#1
class Solution:
    def totalMoney(self, n: int) -> int:
        week = 0
        total = 0
        for i in range(1, n+1):
            total = total + (i - 7 * week) + week
            if i % 7 == 0:
                week = week + 1
        
        return total

#2 Math
class Solution:
    def totalMoney(self, n: int) -> int:
        w = n // 7
        money = w * 28
        money += (7 * w *( w - 1))//2

        if (n % 7):
            extra_days = n % 7
            money_to_add = w + 1
            for i in range(extra_days):
                money += money_to_add
                money_to_add += 1

        return money