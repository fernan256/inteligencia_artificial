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

		checked = set()
		nodesExpanded = deque()
		nodesExpanded.append(bfs.Node(start, None, None))
		count = 0
		while nodesExpanded:
			count += 1
			nodo = nodesExpanded.popleft()

			if tuple(nodo.currentState) not in checked:
				checked.add(tuple(nodo.currentState))
			else:
				continue
			if nodo.currentState == goal:
				return list(nodo.currentState), count
			else:
				nodesExpanded.extend(nodo.expandNode())
		else:
			return [],count

	def biderecionalMethod(self, start, goal):
		start = tuple(start)
		goal = tuple(goal)

		checkedStart = set()
		checkedGoal = set()
		nodesExpandedFromStart = deque()
		nodesExpandedFromGoal = deque()
		nodesExpandedFromStart.append(bfs.Node(start, None, None))
		nodesExpandedFromGoal.append(bfs.Node(goal, None, None))
		count = 0

		while nodesExpandedFromStart and nodesExpandedFromGoal:
			count += 1
			nodeStart = nodesExpandedFromStart.popleft()
			nodeGoal = nodesExpandedFromGoal.popleft()
			nodesExpandedFromGoal.extend(nodeGoal.expandNode())
			nodesExpandedFromStart.extend(nodeStart.expandNode())
			for startNodes in nodesExpandedFromStart:
				for goalNodes in nodesExpandedFromGoal:
					print(f"startNodes.currentState: {startNodes.currentState}")
					print(f"goalNodes.currentState: {goalNodes.currentState}")
					if startNodes.currentState == goalNodes.currentState:
						return list(nodeStart.currentState), list(nodeGoal.currentState), count
					else:
						checkedStart.add(tuple(nodeStart.currentState))
						checkedGoal.add(tuple(nodeGoal.currentState))
		else:
			return [],count
