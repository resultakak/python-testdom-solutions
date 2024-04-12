def route_exists(from_row, from_column, to_row, to_column, map_matrix):
    rows = len(map_matrix)
    cols = len(map_matrix[0])

    stack = [(from_row, from_column)]
    visited = set()

    while stack:
        current = stack.pop()
        if current == (to_row, to_column):
            return True
        visited.add(current)
        row, col = current
        neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        for neighbor in neighbors:
            n_row, n_col = neighbor
            if 0 <= n_row < rows and 0 <= n_col < cols and map_matrix[n_row][n_col] and neighbor not in visited:
                stack.append(neighbor)

    return False

if __name__ == '__main__':
    map_matrix = [
        [True, False, False],
        [True, True, False],
        [False, True, True]
    ]

    print(route_exists(0, 0, 2, 2, map_matrix))

