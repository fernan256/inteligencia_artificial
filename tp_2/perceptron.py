from os import get_inheritable
import random



def getInitialWeights():
  # w0 = random.random(-1, 1)
  # w1 = random.random(-1, 1)
  # w2 = random.random(-1, 1)
  w0 = 0.86
  w1 = -0.66
  w2 = 0.22
  return w0,w1,w2

def errorCalculation(desO, realO):
  print(desO,realO)
  error = desO - realO
  return error

def training(input, output, Lr):
  desired_ouput = output
  w0,w1,w2 = getInitialWeights()
  print(w0,w1,w2)
  error = 1
  count = 0
  while True:
    count += 1
    # real_output = w0 + w1 + w2
    amountOfEntries = len(input)
    for i in range(amountOfEntries):
      currentEntries = len(input[i])
      for j in range(currentEntries):
        real_output = (1 * w0) + (input[i][j] * w1) + (input[i][j] * w2)
        errorValue = errorCalculation(input[i][j], real_output)
        print(f"error: {errorValue}")
        if(errorValue <= 0.1):
          print("e")
          return count
        else:
          delta_calculo = real_output * (1-real_output) * error
          print(delta_calculo)
          deltaX = Lr * 1 * delta_calculo
          if j == 0:
            w0 = w0 + deltaX
          elif j == 1:
            w1 = w1 + deltaX
          else:
            w2 = w2 + deltaX 
      


if __name__ == "__main__":
  orGate = [[0,0,1,1],[0,1,0,1]]
  orGateOutput = [0,1,1,1]
  learning_rate = 0.1
  
  count = training(orGate, orGateOutput, learning_rate)

  print(f"Iteraciones: {count}")




