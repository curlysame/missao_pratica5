import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i 
        for j in range(i +1 , n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def measure_sorting_time(sort_function, arr):
    start_time = time.time()
    sorted_arr = sort.function(arr)
    end_time = time.time()
    execution_time = end_time - start_time
    return sorted_arr, execution_time

palavras_lista = list()

with open("texto2.txt", "r") as arquivo:
    for linha in arquivo:
        palavras = linha.split()
        palavras_lista.extend(palavras)

print("Lista original de palavras:")
print(palavras_lista)

palavras_bubble = palavras_lista.copy()
palavras_selection = palavras_lista.copy()

sorted_bubble, time_bubble = measure_sorting_time(bubble_sort, palavras_bubble)
print("\nBubble sort:")
print(bubble_sort)
print(f"Tempo de execução (Bubble Sort): {time_bubble:.6f} segundos")

sorted_selection, time_selection = measure_sorting_time(selection_sort, palavras_selection)
print("\nSelection Sort")
print(sorted_selection)
print(f"Tempo de exuçaão (selectiom Sort): {time_selection:.6f} segundos")


start_time = time.time()
palavras_lista.sort()
end_time = time.time()
time_sort = end_time - start_time

print("\nSort nativo do Python:")
print(palavras_lista)
print(f"Tempo de execução (Sort nativo): {time_sort:.6f} segundos")

with open("texto2.txt", "w") as arquivo_ordenado:
    arquivo_ordenado.write(" ".join(palavras_lista))