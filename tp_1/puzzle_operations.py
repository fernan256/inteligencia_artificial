import bfsUtils as bfs
import utils as Utils
import random
from collections import deque

class Puzzle():

	def __init__(self, cols=3, rows=3, nmix=50, goalState=None):
		self.cols = cols
		self.rows = rows
		self.nmix = nmix
		self.goalState = goalState

	def mixMatrix(self):
		matrixToOrder = self.goalState.copy()
		for n in range(self.nmix):
			n += 1
			curr_order = random.randrange(9)
			random.choice([Utils.moveRight, Utils.moveLeft, Utils.moveUp, Utils.moveDown])(matrixToOrder, curr_order)
			matrixToOrder = matrixToOrder
		return matrixToOrder


	def randomSolve(self, randomMatrix):
		n = 0
		matrixToOrder = randomMatrix.copy()
		while matrixToOrder != self.goalState:
			n += 1
			curr_order = random.randrange(9)
			random.choice([Utils.moveRight, Utils.moveLeft, Utils.moveUp, Utils.moveDown])(matrixToOrder, curr_order)
			matrixToOrder = matrixToOrder
			Utils.represent_board(matrixToOrder, n)

		return matrixToOrder, n

	def bfsMethod(self, start, goal):
		start = tuple(start)
		goal = tuple(goal)

		visitados = set()
		frontera = deque()
		frontera.append(bfs.Node(start, None, None))
		count = 0
		while frontera:
			count += 1
			nodo = frontera.popleft()

			if tuple(nodo.currentState) not in visitados:
				visitados.add(tuple(nodo.currentState))
			else:
				continue
			if nodo.currentState == goal:
				return list(nodo.currentState), count
			else:
				frontera.extend(nodo.expandNode())
		else:
			return [],count

	def biderecionalMethod(self, start, goal):
		pass
