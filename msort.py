#hi
def merge(left, right):
    # store merged arr in this list
    result = []
    # compare smallest term and append to result
    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    while left:
        result.append(left[0])
        left = left[1:]
    while right:
        result.append(right[0])
        right = right[1:]
    return result

def msort(m):
    # base case
    if len(m) <= 1:
        return m
    # recursive case
    left = []
    right = []
    for i in range(len(m)):
        if i < len(m)/2:
            left.append(m[i])
        else:
            right.append(m[i])

    # left = m[:len(m)//2]
    # right = m[len(m)//2+1:]

    # recursively sort both sublists
    left = msort(left)
    right = msort(right)

    # merge the sorted sublists
    return merge(left, right)

# random unsorted array
arr = [4,-1,22,1,4,54,22,1,45,0]
print(msort(arr))
