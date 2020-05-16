
array = [0, 1, 2, 3]
# summe array 6
sum = 0

for i in range(len(array)-1):
    zwischenergebnis = array[i-1] + array[i]
    sum = zwischenergebnis + array[i+1]


print(sum)