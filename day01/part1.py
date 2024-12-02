from util import *

data = get_matrix()

data = invert_matrix(data)
[row.sort() for row in data]
data = invert_matrix(data)
data = [abs(row[0] - row[1]) for row in data]
data = sum(data)
print(data)
