import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i 
        for j in range(i +1 , n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    


def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

words = []
with open('texto.txt', 'r') as file:
    for line in file:
        words.extend(line.split()) 



bubble_arr = words.copy()
selection_arr = words.copy()
sort_arr = words.copy()


bubble_time = measure_time(bubble_sort, bubble_arr)
print(f"Bubble Sort ordenado: {bubble_arr}")
print(f"Tempo de execução do Bubble Sort: {bubble_time:.6f} segundos\n")

selection_time = measure_time(selection_sort, selection_arr)
print(f"Selection Sort ordenado: {selection_arr}")
print(f"Tempo de execução do Selection Sort: {selection_time:.6f} segundos\n")

start_time = time.time()
sort_arr.sort()
end_time = time.time()
sort_time = end_time - start_time
print(f"Sort nativo ordenado: {sort_arr}")
print(f"Tempo de execução do sort nativo: {sort_time:.6f} segundos\n")

with open('palavras_ordenadas.txt', 'w') as file:
    for word in sort_arr:
        file.write(word + "\n")