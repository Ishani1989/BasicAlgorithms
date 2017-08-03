#BinarySearchIterative

arr = raw_input().split()
data = raw_input()
arr.sort()

def binarySearchIterative(A, data):
    print A
    low = 0
    high = len(A)-1
    mid = 0
    while(low<=high):
        #print "mid", mid
        mid = low+(high-low)/2
        #print "A[mid]", A[mid]
        if A[mid]==data:
            return mid
        elif A[mid]>data:
            high = mid - 1
        elif A[mid]<data:
            low = mid + 1
    return -1

print binarySearchIterative(arr, data)




