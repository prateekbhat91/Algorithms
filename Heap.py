"""
Building Heaps, Max.Heap, Heapsort implementation

@author: Prateek Bhat
"""
import math

def parent(i):
    return int(math.floor((i-1)/2))

def left(i):
    return int(math.floor((i*2)+1))

def right(i):
    return int(math.floor((i*2)+2))

def swap(a,b):
    return b,a

def maxheapify(arr, i):
    largest = i
    l = left(i)
    r = right(i)
    if l<len(arr):
        if arr[l] > arr[i]:
            largest = l

    if r<len(arr):
        if arr[r] > arr[largest]:
            largest = r

    if largest != i:
        arr[largest], arr[i] = swap(arr[largest], arr[i])
        maxheapify(arr, largest)

def buildmaxheap(arr):
    l = int(math.floor((len(arr))/2)) -1
    for i in range(l, -1, -1):
        maxheapify(arr,i)

def heapheight(arr):
    return int(math.floor(math.log(len(arr), 2)))

def insert(arr,i):
    arr.append(i)
    buildmaxheap(arr)

def heapsort(arr, sorted):
    l = len(arr)-1
    arr[0], arr[l] = swap(arr[0], arr[l])
    sorted.append(arr[l])
    del arr[l]
    if l != 0:
        maxheapify(arr, 0)
        heapsort(arr, sorted)


if __name__ == "__main__":
    print "Enter the elements of array separated with space"
    s = raw_input()
    arr = map(int, s.split())
    print arr
    buildmaxheap(arr)
    print arr
    print "Heap Height =",heapheight(arr)
    insert(arr,23)
    print arr
    sorted = []
    heapsort(arr, sorted)
    print sorted