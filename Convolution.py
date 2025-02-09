# Convolution
import numpy as np

arr1 = np.array([1, 2, 1, -1])
arr2 = np.array([1, 2, 3, 1])


len1 = len(arr1)
len2 = len(arr2)

arr = np.empty((len1, len2))

for i in range(len1):
    for j in range(len2):
        arr[i][j] = arr1[i] * arr2[j]

print("Matrix:")
print(arr)

origin1 = 3
origin2 = 2

if(origin1>len1 or origin2>len2):
  print("wrong values")

l3 = len1 + len2 - 1


convolve_arr = np.zeros(l3)


for i in range(len1):
    for j in range(len2):
        convolve_arr[i + j] = convolve_arr[i + j] + arr1[i] * arr2[j]

print("Convolution Result:")
print(convolve_arr)
print("final origin:", convolve_arr[origin1+origin2] )
