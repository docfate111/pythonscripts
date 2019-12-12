def bubbleSort(l):
    while(not isSorted(l)):
        for i in range(len(l)-1):
            if(l[i]>l[i+1]):
                temp=l[i]
                l[i]=l[i+1]
                l[i+1]=temp
    return l
def isSorted(l):
    for i in range(len(l)-1):
        if(l[i]>l[i+1]):
            return False
    return True
def mergeSort(l):
    if(len(l)==2):
        return mergeHalves([l[0]], [l[1]])
    if(len(l)==1):
        return [l[0]]
    mid=(len(l)//2)+1
    left=l[0:mid]
    right=l[mid:]
    return mergeHalves(mergeSort(left), mergeSort(right))
def mergeHalves(a, b):
    if(len(a)==0):
        return b
    if(len(b)==0):
        return a
    if(a[0]<=b[0]):
        return [a[0]]+list(mergeHalves(a[1:], b))
    if(a[0]>b[0]):
        return [b[0]]+list(mergeHalves(a, b[1:]))
def selectionSort(l):
    max=-100000
    ind=0
    last=len(l)-1
    for j in range(len(l)):
        for i in range(len(l)-j):
            if(l[i]>max):
                max=l[i]
                ind=i
        temp=l[ind]
        l[ind]=l[last]
        l[last]=temp
        last-=1
        max=-100000
    return l
def insertionSort(l):
    curr=0
    for i in range(len(l)-1):
        curr=i
        while(l[curr]>l[curr+1] and curr>=0):
            temp=l[curr]
            l[curr]=l[curr+1]
            l[curr+1]=temp
            curr-=1
    return l
def radixSort(l):
    #separating all the numbers by their ones digit
    count=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(l)):
        count[(l[i]%10)]+=1
    count[0]-=1
    for i in range(len(count)-1):
        count[i+1]+=count[i]
    aux=[0]*len(l)
    ind=len(l)-1
    while(ind>=0):
        aux[count[l[ind]%10]]=l[ind]
        count[l[ind]%10]-=1
        ind-=1
    l=aux
    #same but for the tens digit
    count=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(l)):
        count[(l[i]//10)]+=1
    count[0]-=1
    for i in range(len(count)-1):
        count[i+1]+=count[i]
    aux=[0]*len(l)
    ind=len(l)-1
    while(ind>=0):
        aux[count[l[ind]//10]]=l[ind]
        count[l[ind]//10]-=1
        ind-=1
    return aux
if __name__=='__main__':
    assert radixSort([27, 35, 76, 31, 44])==[27, 31, 35, 44, 76]
    #quickSort, heapSort
    assert insertionSort([10, 5, 6, 2, 1])==[1, 2, 5, 6, 10]
    assert insertionSort([10, 11, 5, 4, 2])==[2, 4, 5, 10, 11]
    assert selectionSort([9, 5, 3, 1, 11])==[1, 3, 5, 9, 11]
    assert selectionSort([10, 5, 6, 2, 1])==[1, 2, 5, 6, 10]
    assert bubbleSort([10, -2, 8, 6, 3, 1, 2])==[-2, 1, 2, 3, 6, 8, 10]
    assert bubbleSort([4, 7, 8, 3, 1])==[1, 3, 4, 7, 8]
    assert mergeSort([10, 8, 6, 7, 3, 8, 1, 5])==[1, 3, 5, 6, 7, 8, 8, 10]
    assert mergeSort([3, 7, 1, 9, 3])==[1, 3, 3, 7, 9]
    assert mergeSort([10, 4, 7, 2, 9])==[2, 4, 7, 9, 10]
    assert mergeHalves([2, 4, 5, 7, 9, 10], [1, 3, 6, 8, 11, 12])==[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]