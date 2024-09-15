def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array)-i -1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

num_array = [2, 5, 6 , 8, 14, 15, 31, 45, 67, 99, 102, 73, 28, 86, 1]

print("\nArray não ordenado:")
print(num_array)

bubbleSort(num_array)
print("\nArray ordenado de forma bubbleSort: ")
print(num_array)