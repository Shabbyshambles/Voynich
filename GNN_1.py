import numpy as np

weights = []
# Creating the Laplacian matrix interpretation of our graph
Laplacian = np.matrix([[1, -1, 0, 0, 0, 0], [-1, 2, -1, 0, 0, 0],
 [0, -1, 4, -1, -1, -1], [0, 0, -1, 2, -1, 0], [0, 0, -1, -1, 2, 0],
 [0, 0, -1, 0, 0, 1]], np.int32)

 # Creating the feature vector
Features = np.array([1, 7, 3, 4, 2, 1])

# Are both arrays read into our code
#print(Features.shape)

#print(Laplacian.shape)

# Reading in the contents of our Manuscript transliteration
with open('Manuscript.txt', encoding='utf8') as f:
    lines = f.read()
charmap = []
manuscript = []
flag = 0
#getting characters from transliteration and cleaning the indices from the manuscript
for x in lines:
    if x == '<':
        flag = 1
    
    if flag == 0:
       manuscript.append(x)
       if x in charmap:
          
          continue
       else:
          charmap.append(x)
      
    if x == '>':
        if flag == 1:
           flag = 0
#print(charmap)

features = {}
count = np.zeros((len(charmap), ))
z=0
#getting our feature vector, representing how many times each character is used in the text
for x in charmap:
    n = 0
    for y in manuscript:
        if y == x:
            n=n+1
    #print(str(x) + " " +  str(n))
    count[z]=n
    z+=1
    features.update({x: n})
print(features)
print(count)
Laplace2 = np.zeros((len(charmap), len(charmap)))
#print(Laplace2)
n = -1

#getting our Laplacian representation of the graph, where the characters are nodes and their neighbors are edges
for x in charmap:
    manuindex = -1
    n += 1
    
    Laplace2[n,n] = count[n]
    for y in manuscript:
        manuindex+=1
        if y == x:
            index = -1
            for z in charmap:
                index+=1
                if manuscript[manuindex-1] == z:
                    Laplace2[n, index]-=1
                if(manuindex+1<len(manuscript)):
                   if manuscript[manuindex+1] == z:
                      Laplace2[n, index]-=1


            
        
    #print(x)
    #print(charmap[n])
print(Laplace2)

