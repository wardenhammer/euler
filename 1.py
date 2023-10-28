total = 0
for i in range(1, 1000):
    # print(i)
    threes = i % 3
    fives = i % 5
    if threes == 0 or fives == 0:
        print (i)
        total += i
print ("Total:"+str(total))