import argparse
import weights
import math

import matplotlib.pyplot as plt
import numpy as np

def get_x(inputs, weights_val):
  x = 0
  for index, input in enumerate(inputs):
    x += input * weights_val[index]
  real_output = 1 / (1 + math.exp(-x))
  return real_output


def hidden_layer(inputs, weidghts_to_use):
  first_line_outputs = [1]
  for i in range(len(weidghts_to_use)):
    responses = get_x(inputs, weidghts_to_use[i])
    first_line_outputs.append(responses)
  return first_line_outputs


def out_layer(gateToLearn, inputs, output_weidgths):
  final = 0
  outputs = []
  errors_line = []
  new_wiedths = []
  temp = []
  error1 = 0
  for a in range(len(output_weidgths)):
    final = get_x(inputs, output_weidgths[a])
    error1 = gateToLearn - final
    print(f"final: {final}")
    print(f"error: {error1}")
    outputs.append(final)
    deltaF = final * ( 1 - final) * error1
    for i in range(len(inputs)):
      deltaW = 0.5 * inputs[a] * deltaF
      weightsValues = output_weidgths[a][i] + deltaW
      errors_line.append(deltaW)
      temp.append(weightsValues)
      if(len(temp) == 4):
        new_wiedths.append(temp)
        temp = []
  return final, errors_line, new_wiedths, deltaF, error1


def get_errors_hidden_line(weights_to_calculate, deltaF, outs ,inputs):
  outs = outs[1:]
  errors_line = []
  new_wiedths = []
  temp = []

  for i in range(len(inputs)):
    deltaOc1 = outs[i] * ( 1 - outs[i]) * deltaF
    for j in range(len(weights_to_calculate[i])):
      deltaW = 0.5 * inputs[j] * deltaOc1
      weightsValues = weights_to_calculate[i][j] + deltaW
      errors_line.append(deltaW)
      temp.append(weightsValues)
      if(len(temp) == 3):
        new_wiedths.append(temp)
        temp = []
  return new_wiedths, errors_line


def create_graph(elements,inputs):
  for i in range(len(elements)):
    x = np.arange(0, len(elements[i]))
    y = elements[i]
    plt.plot(x, y, label = inputs[i])
  plt.legend()
  plt.show()


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-or", '--orGate',
                        help='Ejecutar compuerta OR', action='store_true')
  parser.add_argument("-and", '--andGate',
												help='Ejecutar compuerta AND', action='store_true')
  parser.add_argument("-xor", '--xorGate',
												help='Ejecutar compuerta XOR', action='store_true')
  parser.add_argument("-n", '--amountPr',
                        help='Ejecutar compuerta OR', action='store_true')

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

  hidden_layer_weidghts = [weights.first_line_1_wights_values(),weights.first_line_2_wights_values(),weights.second_line_1_wights_values()]
  output_weidgths = [weights.second_line_2_wights_values(),weights.second_line_2_wights_values(),weights.second_line_2_wights_values(),weights.second_line_2_wights_values()]

  resp_total = []
  errs = []
  errs_total = []
  temp_values = []
  for i in range(len(inputs)):
    for h in range(1000):
      second_res = hidden_layer(inputs[i], hidden_layer_weidghts)
      third_res, errors_line, new_wei, deltaF, error_to_save = out_layer(gateToLearn[i], second_res, output_weidgths)
      temp_values.append(third_res)
      errs.append(error_to_save)
      output_weidgths = new_wei    
      hidden_layer_weidghts, errors_line = get_errors_hidden_line(hidden_layer_weidghts, deltaF, second_res, inputs[i])
    hidden_layer_weidghts = [weights.first_line_1_wights_values(),weights.first_line_2_wights_values(),weights.second_line_1_wights_values()]
    output_weidgths = [weights.second_line_2_wights_values()]
    resp_total.append(temp_values)
    temp_values = []
    errs_total.append(errs)
    errs = []

  create_graph(resp_total, inputs)
  create_graph(errs_total, inputs)