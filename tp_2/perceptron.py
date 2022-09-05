import argparse
import math
import random


def getInitialWeights():
  w0 = float.__round__(random.random(),2)
  w1 = float.__round__(random.random(),2)
  w2 = float.__round__(random.random(),2)
  # w0 = 0.86
  # w1 = 0.66
  # w2 = 0.36
  return w0,w1,w2

def training(desired_ouput, Lr, A, B):
  w0,w1,w2 = getInitialWeights()
  print(f"w0: {w0}, w1: {w1}, w2: {w2}")
  count = 0
  error = True
  errorValue = 0
  while error:
    error = False
    currentEntries = len(desired_ouput)
    for i in range(currentEntries):
      real_output = (1 * w0) + (A[i] * w1) + (B[i] * w2)
      y = 1 / (1 + (math.exp(-real_output)))
      if (y != desired_ouput[i]):
        error = True
        errorValue = desired_ouput[i] - real_output
        delta_calculo = real_output * (1 - real_output) * errorValue
        deltaX = Lr * 1 * delta_calculo
        w0 = w0 + deltaX
        w1 = w1 + deltaX
        w2 = w2 + deltaX
        count += 1
      else:
        error = False
      print(f"Iteraciones: {count}")
  return count, y, real_output, errorValue


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-or", '--orGate',
                        help='Ejecutar compuerta OR', action='store_true')
  parser.add_argument("-and", '--andGate',
												help='Ejecutar compuerta AND', action='store_true')
  parser.add_argument("-xor", '--xorGate',
												help='Ejecutar compuerta XOR', action='store_true')
  args = parser.parse_args()
  orOption = args.orGate
  andOption = args.andGate
  xorOPtion = args.xorGate
  gateToLearn = ""
  A = [0,0,1,1]
  B = [0,1,0,1]
  orGateOutput = [0,1,1,1]
  andGateOutput = [0,0,0,1]
  xorGateOutput = [0,1,1,0]
  learning_rate = 0.1
  if orOption:
    gateToLearn = orGateOutput
  elif andOption:
    gateToLearn = andGateOutput
  elif xorOPtion:
    gateToLearn = xorGateOutput
  
  count, y, real_output, errorValue = training(gateToLearn, learning_rate, A, B)

  print(f"Iteraciones: {count}")
  print(f"Y: {y}")
  print(f"Salida Real: {real_output}")
  print(f"Error: {errorValue}")
