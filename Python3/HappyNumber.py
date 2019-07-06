
total = 0
def ishappy(n):
    a = []
    while n not in a:
        a.append(n)
        for x in str(n):
            global total
            total = total + int(x) ** 2
            n = total
        total = 0

    if n == 1:
        return 'happy'
    else:
        return 'unhappy'

ans = ishappy(3)

print(ans)

#最快解法 縮一起

def ishappy(n):
    a = []
    while n not in a:
        a.append(n)
        n = sum([int(x) ** 2 for x in str(n)])

    return 'happy' if n == 1 else 'unhappy'