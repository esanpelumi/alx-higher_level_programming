def bubblesort(arr=[], row =0, col=0):
    if row == 0:
        return
    if col < row:
        if arr[col] > arr[col+1]:
            temp = arr[col]
            arr[col] = arr[col+1]
            arr[col+1] = temp
        bubblesort(arr, row, col+1)
    else:
        bubblesort(arr, row-1, 0)
def selection(arr=[], row =0, col=0, max=0):
    #max is the index of the maximum
    if row == 0:
        return
    if col < row:
        if arr[col] > arr[max]:
            selection(arr, row, col+1, col)
        else:
            selection(arr,row, col+1, max)
        
    else:
        temp = arr[max]
        arr[max] = arr[row-1]
        arr[row-1] = temp
        selection(arr, row-1, 0, 0)

# arr = [4,3,2,1]
# selection(arr,len(arr), 0, 0)
# print(arr)
def mergesort(arr=[]):
    if len(arr) == 1:
        return arr
    mid = len(arr)/2
    left = mergesort(arr[0:mid+1])
    right = mergesort(arr[mid:])
    return merge(left, right)
def merge(left=[], right=[]):
    mix = []#len(left) + len(right)
    i = 0
    j = 0
    k = 0
    while (i < len(left) and j < len(right)):
        if left[i] < right[j]:
            mix.append(left[i])
            i += 1
        else:
            mix.append(right[j])
            j += 1
        j += 1

def subseq(p, up):
    if up == "":
        print(p)
        return
    ch = up[0]
    subseq(p+ch, up[1:])
    subseq(p, up[1:])


def substr(p, up):
    if up == "":
        new = []
        new.append(p)
        return new
    ch = up[0]
    left = []
    right = []
    
    left+=(substr(p+ch, up[1:]))
    right+=(substr(p, up[1:]))
    ans = left + right
    return ans

def substrascii(p, up):
    if up == "":
        print(p)
        return
    ch = up[0]
    substrascii(p+ch, up[1:])
    substrascii(p, up[1:])
    substrascii(p + str(ord(ch)), up[1:])
#print(substrascii('', "abc"))

def substrAsci(p, up):
    if up == "":
        new = []
        new.append(p)
        return new
    ch = up[0]
    left = []
    right = []
    asci = []
    
    left+=(substrAsci(p+ch, up[1:]))
    right+=(substrAsci(p, up[1:]))
    asci+=(substrAsci(p+str(ord(ch)), up[1:]))
    ans = left + right + asci
    return sorted(ans)
#print(substrAsci("", "abc"))

def subIteration(lis = list):
    outer = []
    for num in lis:
        n = len(outer)
        for i in range(n):
            internal = i[:]
            internal+=(num)
            outer.append(internal)
    return outer

def binary_search(check=list, target=0):
    start = 0
    end = len(check) - 1
    while (start <= end):
        mid = start + (end - start) // 2
        if target < check[mid]:
            end = mid - 1
        elif target > check[mid]:
            start = mid + 1
        else:
            return mid
    return -1

def binary_search_des(check=list, target=0):
    start = 0
    end = len(check) - 1
    while (start <= end):
        mid = start + (end - start) // 2
        if target < check[mid]:
            start = mid + 1
        elif target > check[mid]:
            end = mid - 1
        else:
            return mid
    return -1


def agnostic_BS(check=list, target=0):
    start = 0
    end = len(check) - 1
    is_Agnostic = check[start] < check[end]
    while (start <= end):
        mid = start + (end - start) // 2
        if check[mid] == target:
            return mid
        if is_Agnostic:
            if target < check[mid]:
                start = mid + 1
            elif target > check[mid]:
                end = mid - 1
        else:
            if target > check[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return -1

array = [121,23,5,4,0,-5,-11]
target=23
ans = agnostic_BS(array, target)
print(ans)
