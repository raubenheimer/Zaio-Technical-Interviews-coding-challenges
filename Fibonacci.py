def fibonacci(up_to):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(up_to-2):
        b_store = b
        b += a
        a = b_store
        print(b)
fibonacci(100)
