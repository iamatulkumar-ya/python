li = [60, 1, 8, 4, 6, 92, 12, 74, 45, 15, 20 ]
 
for i in range(len(li)):
    for j in range(0, len(li)-i-1):
        if li[j] > li[j+1]:
            li[j] , li[j+1] = li[j+1], li[j]

     


print(li)
