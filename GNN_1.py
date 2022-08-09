import numpy as np

weights = []
# Creating the Laplacian matrix interpretation of our graph
Laplacian = np.matrix([[1, -1, 0, 0, 0, 0], [-1, 2, -1, 0, 0, 0],
 [0, -1, 4, -1, -1, -1], [0, 0, -1, 2, -1, 0], [0, 0, -1, -1, 2, 0],
 [0, 0, -1, 0, 0, 1]], np.int32)

 # Creating the feature vector
Features = np.array([1, 7, 3, 4, 2, 1])

# Are both arrays read into our code
print(Features.shape)

print(Laplacian.shape)

with open('Manuscript.txt', encoding='utf8') as f:
    lines = f.read()
charmap = []
for x in lines:
    if x in charmap:
        continue
    else:
        charmap.append(x)
print(charmap)


