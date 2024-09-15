array = [1, 9, 2, 8, 33, 25, 56, 63, 34, 83, 22, 65, 98, 87, 73]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1,len(array)):
        if array[min_index] >array[j]:
            min_index = j 

    array[i], array[min_index] = array[min_index], array[i]

print("Array ordenado:", array)