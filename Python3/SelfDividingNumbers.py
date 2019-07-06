
left = 1
right = 22

#Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

ans = True
final = []
for i in range(left,right+1):   #可以把left直接換成i 就好了
    for y in range(0,len(str(left))):

        if int(str(left)[y]) == 0:
            ans = False
        elif left % int(str(left)[y]) != 0 :
            ans = False

    if ans == True:
        final.append(left)
    left = left + 1
    ans = True


print(final)


