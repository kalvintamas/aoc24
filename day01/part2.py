from util import *

data = get_matrix()
data = invert_matrix(data)
[row.sort() for row in data]
sum = 0
for n in data[0]:
    for m in data[1]:
        if n == m:
            sum += n
print(sum)
