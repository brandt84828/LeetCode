

A = [0,1]

start = 0
end = len(A) - 1

for i in range(0,len(A)):
    if start < end: #避免交錯
        if A[start] % 2 == 1 and A[end] % 2 == 0:#執行交換
            temp = A[start]
            A[start] = A[end]
            A[end] = temp
        elif A[start] % 2 == 0 and A[end] % 2 == 1:
            start = start + 1;
            end = end - 1;
        elif A[end] % 2 == 1:
            end = end - 1;
        else :
            start = start + 1;

print(A)





