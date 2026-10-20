def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    for tab in matrix:
        tab = tab.reverse()
    return matrix

