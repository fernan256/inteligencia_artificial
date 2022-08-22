import utils as Utils
import random

class Puzzle():

		def __init__(self, cols=3, rows=3, nmix=50):
				self.cols = cols
				self.rows = rows
				self.nmix = nmix
				self.goal_state = [0,1,2,3,4,5,6,7,8]

	
		def mixMatrix(self):
				matrixToOrder = self.goal_state.copy()
				for n in range(self.nmix):
						n += 1
						curr_order = random.randrange(9)
						random.choice([Utils.move_right, Utils.move_left, Utils.move_up, Utils.move_down])(matrixToOrder, curr_order)
						matrixToOrder = matrixToOrder
				return matrixToOrder


		def randomSolve(self, randomMatrix):
				n = 0
				matrixToOrder = randomMatrix.copy()
				while matrixToOrder != self.goal_state:
						n += 1
						curr_order = random.randrange(9)
						random.choice([Utils.move_right, Utils.move_left, Utils.move_up, Utils.move_down])(matrixToOrder, curr_order)
						matrixToOrder = matrixToOrder
						Utils.represent_board(matrixToOrder, n)

				return matrixToOrder, n

		def busquedaEnAnchura():
				pass
