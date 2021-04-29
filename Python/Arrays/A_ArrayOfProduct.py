def ArrayOfProduct(arr):
    prod = [1 for _ in range(len(arr))]
    leftprod = [1 for _ in range(len(arr))]
    rightprod = [1 for _ in range(len(arr))]

    leftRunProd = 1
    for i in range(len(arr)):
        leftprod[i] = leftRunProd
        leftRunProd *= arr[i]

    rightRunProd = 1
    for i in reversed(range(len(arr))):
        rightprod[i] = rightRunProd
        rightRunProd *= arr[i]

    for i in range(len(arr)):
        prod[i] = leftprod[i] * rightprod[i]

    return prod
