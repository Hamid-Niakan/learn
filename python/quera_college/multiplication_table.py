def multiplication_table(n):
    table = ''
    for i in range(1, 11):
        table = table + str(i) + ' x ' + str(n) + ' = ' + \
            str(i * n)
        if i != 10:
            table = table + '\n'
    print(table)

multiplication_table(0)