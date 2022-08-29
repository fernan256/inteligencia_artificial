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