import numpy as np

def minswaps(arr):
    count = 0
    while True:
        boole = np.invert(np.equal(np.sort(arr), arr))
        arr = arr[boole]
        if arr.size == 0:
            break
        arr[[0, np.argmin(arr)]] = arr[[np.argmin(arr), 0]]
        count += 1
    print(count)

minswaps(np.array([1, 5, 4, 3, 2]))
minswaps(np.array([4, 5, 2, 3, 1]))
