import random

def merge(vetor, start, end, middle):
    n1 = middle - start + 1
    n2 = end - middle

    left = [0] * n1
    right = [0] * n2

    for i in range(0, n1):
        left[i] = vetor[start + i]

    for j in range(0, n2):
        right[j] = vetor[middle + 1 + j]

    i = 0
    j = 0
    k = start

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            vetor[k] = left[i]
            i += 1
        else:
            vetor[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        vetor[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        vetor[k] = right[j]
        j += 1
        k += 1


def mergesort(vetor, start, end):
    middle = int((start + end) / 2)

    if start < end:
        mergesort(vetor, start, middle)
        mergesort(vetor, middle + 1, end)
        merge(vetor, start, end, middle)


x = int(input('Digite o tamanho do vetor: '))
n = [0] * x

for k in range(x):
    n[k] = random.randint(1, 100)

print('\nVetor de entrada: {}'.format(n))
g = len(n)
mergesort(n, 0, g-1)
print('\n\nVetor de saida: {}'.format(n))
