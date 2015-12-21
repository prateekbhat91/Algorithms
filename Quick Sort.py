"""
Quick Sort Algorithm
@author: Prateek Bhat
"""

def swap(a,b):
    return b,a

def Partition(arr,p,r):
    ran = arr[r]
    j = p-1
    for i in range(p,r):
        if arr[i] < ran:
            j+=1
            arr[i],arr[j] = swap(arr[i],arr[j])
    arr[j+1], arr[r] = swap(arr[j+1], arr[r])

    return j+1


def Quicksort(arr,p,r):
    if p<r:
        q = Partition(arr,p,r)
        Quicksort(arr,p,q-1)
        Quicksort(arr,q+1,r)

if __name__== '__main__':
    print "Enter the elements of array separated with space"
    s = raw_input()
    arr = map(int, s.split())
    print arr
    n = len(arr)
    Quicksort(arr,0,n-1)
    print arr