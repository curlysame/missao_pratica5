import random

int_array=[random.randint(1,100)for _ in range(15)]

print("Array de numeros inteiros não ordenado: ")
print(int_array)

int_array.sort()
print("\nArray de numeros inteiros ordernados de forma crescente: ")
print(int_array)

int_array.sort(key=None, reverse=True)
print("\nArray de numeros inteiros de forma decrescente: ")
print(int_array)

string_array = ["nome", "dataNascimento", "email", "cpf", "rg", "celular", "pais"]

print("\nArray de strings não ordenados:")
print(string_array)

string_array.sort()
print("\nArray de string de forma crescente:")
print(string_array)

string_array.sort(key=None, reverse=True)
print("\nArray de strings de forma decrescente: ")
print(string_array)