total = 2 # this covers the first even number
pen = 1
print (pen)
last = 2
print (last)
while True:
    next = pen + last
    if next > 4000000:
        break
    print (next)
    if next % 2 == 0:
        total += next
    print ("Total:"+str(total))
    pen = last
    last = next