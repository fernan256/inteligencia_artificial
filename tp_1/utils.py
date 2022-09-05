def moveRight(matrix, curr_order):
	original_arr = matrix.copy()
	idx_cero = curr_order
	if (idx_cero + 1) < len(original_arr):
		temp = matrix[idx_cero + 1]
		matrix[idx_cero + 1] = matrix[idx_cero]
		matrix[idx_cero] = temp
		return matrix


def moveLeft(matrix, curr_order):
	original_arr = matrix.copy()
	idx_cero = curr_order
	if (idx_cero - 1) > len(original_arr):
		temp = matrix[idx_cero - 1]
		matrix[idx_cero - 1] = matrix[idx_cero]
		matrix[idx_cero] = temp
		return matrix


def moveUp(matrix, curr_order):
	original_arr = matrix.copy()
	idx_cero = curr_order
	if (idx_cero + 3) < len(original_arr):
		temp = matrix[idx_cero + 3]
		matrix[idx_cero + 3] = matrix[idx_cero]
		matrix[idx_cero] = temp
		return matrix


def moveDown(matrix, curr_order):
	original_arr = matrix.copy()
	idx_cero = curr_order
	if (idx_cero - 3) > len(original_arr):
		temp = matrix[idx_cero - 3]
		matrix[idx_cero - 3] = matrix[idx_cero]
		matrix[idx_cero] = temp
		return matrix


def represent_board(matrix, n=0):
	if n == 0:
		print(f"Tablero desordenado con N movimientos: {n}")
	else:
		print(f"Intento numero: {n}")
	print(f"{matrix[0]} | {matrix[1]} | {matrix[2]}")
	print(f"{matrix[3]} | {matrix[4]} | {matrix[5]}")
	print(f"{matrix[6]} | {matrix[7]} | {matrix[8]}")

def represent_board_bidirectional(start, goal, n=0):
	if n == 0:
		print(f"Tablero desordenado con N movimientos: {n}")
	else:
		print(f"Intento numero: {n}")
	print(f"Nodo desde inicial")
	print(f"{start[0]} | {start[1]} | {start[2]}")
	print(f"{start[3]} | {start[4]} | {start[5]}")
	print(f"{start[6]} | {start[7]} | {start[8]}")
	print(f"Nodo desde final")
	print(f"{goal[0]} | {goal[1]} | {goal[2]}")
	print(f"{goal[3]} | {goal[4]} | {goal[5]}")
	print(f"{goal[6]} | {goal[7]} | {goal[8]}")