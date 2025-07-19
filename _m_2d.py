matrix: list[list[int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10]
] # 2D

_: list[int] = [
    num
    for sublist in [
        [
            row[col] ** 2 
            if (row_idx + col) % 2 == 1 and row[col] % 2 == 0 
            else None
            for col in range(len(row))
        ]
        # Add a matrix (2D) to iterate over
        for row_idx, row in enumerate(matrix)
    ]
    for num in sublist
    if num is not None
]

if __name__ == "__main__":
    from json import dumps
    print(dumps(_, indent=4))
