def string_reverce(string):
    reverse = []
    for i in range(len(string)):
        a = len(string)
        reverse.append(string[a-1-i])
    print(''.join(reverse))
string_reverse('Hello_World')
