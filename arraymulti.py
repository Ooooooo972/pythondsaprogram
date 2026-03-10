arr=[2,7,8,6,8,7]
def productExceptSelf(arr):
    n = len(arr)
    res = [1] * n
    for i in range(n):
        for j in range(n):
            if i != j:
                res[i] *= arr[j]
    return res

print(productExceptSelf(arr))