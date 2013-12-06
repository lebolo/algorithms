"""
Naive implementation of selection sort (illustrating how correct data structure,
heaps here, can improve algorithm's performance).

Runtime complexity of selection sort: O(n ^ 2)
Runtime complexity of heapsort: O(n log n)

It is important to understand that in heapsort the only change is data structure,
algorithm is essentially the same.
"""

def selection_sort(L):
    '''Dumb implementation of selection sort.
    Inner loop can be optimized to search for min in sub-range: L[i:],
    so instead of n it will be bound by n/2 (on average). However, total
    running time will still be O(n * n/2) = O(n^2).
    '''
    sorted = []
    for i in range(len(L)):
        k = L.index(min(L))  # find index of minimum el from L
        sorted.append(L.pop(k))

    return sorted


if __name__ == '__main__':
    L = [42, 13, 15, 2, 7, 98, 2]
    print L
    print selection_sort(L)
