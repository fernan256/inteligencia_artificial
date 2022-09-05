class Node():
	def __init__(self, currentState, parent, movement):
		self.currentState = currentState
		self.parent = parent
		self.movement = movement

	def movements(self,move):
		state = list(self.currentState)
		idx_zero = state.index(0)
		if(move == "moveRight"):
			if idx_zero not in [0, 3, 6]:
				temp = state[idx_zero - 1]
				state[idx_zero - 1] = state[idx_zero]
				state[idx_zero] = temp
				return tuple(state)
			else:
				return None

		if(move == "moveLeft"):
			if idx_zero not in [2, 5, 8]:
				temp = state[idx_zero + 1]
				state[idx_zero + 1] = state[idx_zero]
				state[idx_zero] = temp
				return tuple(state)
			else:
				return None


		if(move == "moveUp"):
			if idx_zero not in [6, 7, 8]:
				temp = state[idx_zero + 3]
				state[idx_zero + 3] = state[idx_zero]
				state[idx_zero] = temp
				return tuple(state)
			else:
				return None


		if(move == "moveDown"):
			if idx_zero not in [0, 1, 2]:
				temp = state[idx_zero - 3]
				state[idx_zero - 3] = state[idx_zero]
				state[idx_zero] = temp
				return tuple(state)
			else:
				return None


	def expandNode(self):
			nodesExpanded = []
			expandUp = self.movements("moveUp")
			nodesExpanded.append(Node(expandUp, self, "moveUp"))
			expandDown = self.movements("moveDown")
			nodesExpanded.append(Node(expandDown, self, "moveDown"))
			expandRight = self.movements("moveRight")
			nodesExpanded.append(Node(expandRight, self, "moveRight"))
			expandLeft = self.movements("moveLeft")
			nodesExpanded.append(Node(expandLeft, self, "moveLeft"))

			nodesExpanded = [nodo for nodo in nodesExpanded if nodo.currentState != None]
			return nodesExpanded
