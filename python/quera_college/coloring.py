def coloring(matrix):
    total_layers = len(matrix)
    total_inner_layers = len(matrix[0])
    total_cubes_in_layer = len(matrix[0][0])
    for i in range(total_layers):
        print(f'{i+1}th layer:')
        for index, j in enumerate(matrix[i]):
            for index_inner, k in enumerate(j):
                if (i == 0 or i + 1 == total_layers):
                    matrix[i][index][index_inner] = 1
                    print(1, end=' ')
                else:
                    if (index == 0 or index + 1 == total_inner_layers):
                        matrix[i][index][index_inner] = 1
                        print(1, end=' ')
                    else:
                        if (index_inner == 0 or index_inner + 1 == total_cubes_in_layer):
                            matrix[i][index][index_inner] = 1
                            print(1, end=' ')
                        else:
                            matrix[i][index][index_inner] = 0
                            print(0, end=' ')
            print()
    return matrix


matrix = [
    [
        [5, 5, 5],
        [5, 5, 5],
        [5, 5, 5]
    ],
    [
        [5, 5, 5],
        [5, 5, 5],
        [5, 5, 5]
    ],
    [
        [5, 5, 5],
        [5, 5, 5],
        [5, 5, 5]
    ]
]

print(coloring(matrix))
