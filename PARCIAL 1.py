import random

def reversar_numero(valor):
    return int(str(valor)[::-1])

def suma_de_cifras(valor):
    return sum(int(cifra) for cifra in str(valor))

total_numeros = int(input("Ingrese la cantidad de números a generar: "))

lista_numeros = [random.randint(100, 99999) for _ in range(total_numeros)]

print("Números generados:", ", ".join(map(str, lista_numeros)))
print("Resultados:")

for valor in lista_numeros:
    suma_es_par = suma_de_cifras(valor) % 2 == 0
    invertido_divisible_por_3 = reversar_numero(valor) % 3 == 0

    if suma_es_par and invertido_divisible_por_3:
        print(f"{valor} -> Si")
    else:
        print(f"{valor} -> No")
