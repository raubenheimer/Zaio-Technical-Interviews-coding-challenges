def buck_fizz(up_to):
    for j in range(up_to):
        i = j + 1
        string = str(i)
        if i % 3 == 0 or i % 5 == 0:
            string = ""
            if i % 3 == 0:
                string = 'Fizz'
            if i % 5 == 0:
                string = string + 'Buzz'
        print(f'{string}')

buck_fizz(100)
