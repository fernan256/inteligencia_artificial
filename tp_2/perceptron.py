import argparse
import math
import matplotlib.pyplot as plt
import numpy as np
import random


def get_initial_weights():
  # w0 = float.__round__(random.random(),2)
  # w1 = float.__round__(random.random(),2)
  # w2 = float.__round__(random.random(),2)
  weights = [
    0.9,
    0.66,
    -0.2,
  ]
  return weights


def get_x(inputs, weights):
  x = 0
  for index, input in enumerate(inputs):
    x += input * weights[index]
  return x


def training(desired_ouput, Lr, inputs, weights, errors, all_time_errors, all_time_real_outputs, all_time_weights):
  real_output_response = [1] * 4
  for i in range(len(desired_ouput)):
    sum_x = get_x(inputs[i], weights)
    real_output = 1 / (1 + math.exp(-sum_x))
    real_output_response[i] = real_output
    all_time_real_outputs.append(real_output)
    errorValue = desired_ouput[i] - real_output
    all_time_errors.append(errorValue)
    errors[i] = errorValue
    delta_calculo = real_output * (1 - real_output) * errorValue
    for j in range(len(weights)):
      deltaX = Lr * inputs[i][j] * delta_calculo
      weights[j] = weights[j] + deltaX
      all_time_weights[j].append(weights[j])
  return errors, weights, real_output_response, all_time_errors, all_time_real_outputs, all_time_weights


def create_graph(elements,title):  
  x = np.arange(0, len(elements))
  y = elements

  fig, ax = plt.subplots()
  fig.suptitle(title, fontsize=20)
  # plt.xlabel('xlabel', fontsize=18)
  # plt.ylabel('ylabel', fontsize=16)
  ax.plot(x, y)
  plt.show()


def check_error(errorList, tolerance):
  sum_err = 0
  for x in errorList:
    sum_err += abs(x)
  final_err = sum_err / 3
  if final_err <= tolerance:
    return True


def main(desired_ouput, Lr, inputs):
  count = 0
  weights = get_initial_weights()

  errors = [0] * 4
  all_time_errors = []
  all_time_real_outputs = []
  all_time_weights = [[],[],[]]
  while True:
    count += 1
    errors, weights, real_output_response, all_time_errors, all_time_real_outputs, all_time_weights = training(desired_ouput, Lr, inputs, weights, errors, all_time_errors, all_time_real_outputs, all_time_weights)
    err = check_error(errors, 0.1)
    if err:
      return errors, weights, real_output_response, all_time_errors, all_time_real_outputs, all_time_weights, count


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

  inputs = [
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 1]
  ]
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
  
  errors, weights, real_output_response, all_time_errors, all_time_real_outputs, all_time_weights, count = main(gateToLearn, learning_rate, inputs)
  
  print(f"Iteraciones: {count}")
  print(f"Pesos finales: {weights}")
  print(f"Salida Real: {real_output_response}")
  print(f"Errores finales: {errors}")
  create_graph(all_time_errors,"Errores")
  for idx, elem in enumerate(all_time_weights):
    create_graph(elem,f"w{idx}")
