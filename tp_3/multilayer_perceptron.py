import argparse
import weights
import math

import matplotlib.pyplot as plt
import numpy as np

def get_x(inputs, weights_val):
  x = 0
  # print(f"i::: {inputs}")
  # print(f"w:::: {weights_val}")
  for index, input in enumerate(inputs):
    # print(inputs)
    # print(weights_val)
    x += input * weights_val[index]
  # print(f"x: {x}")
  real_output = 1 / (1 + math.exp(-x))
  print(f"real_output1111: {real_output}")
  return real_output

# def first_percep_lin(gateToLearn, inputs):
#   print("first inputs")
#   weightsL1 = weights.first_line_1_wights_values()
#   weightsL2 = weights.first_line_2_wights_values()
#   second_inputs = []
#   for i in range(4):
#     first_res = get_x(inputs[i], weightsL1)
#     second_res = get_x(inputs[i], weightsL2)
#     second_inputs.append([1,first_res,second_res])
#   return second_inputs

def second_percep_lin(inputs, weidghts_to_use):
  # print(f"seconds inputs11111:::::::::: {inputs}")
  print(f"seconds inputs22222:::::::::: {weidghts_to_use}")
  first_line_outputs = [1]
  temp1 = [1]
  # for i in range(4):
  for i in range(len(weidghts_to_use)):
    responses = get_x(inputs, weidghts_to_use[i])
    # print(f"responses: {responses}")
    # temp1.append(responses)
    # if(len(temp1) == 3):
    first_line_outputs.append(responses)
      # temp1 = [1]
  # print(f"first_line_outputs: {first_line_outputs}")
  return first_line_outputs


def third_percep_lin(gateToLearn, inputs, outs):
  print(f"thirds inputs {inputs}")
  final = 0
  outputs = []
  # for i in range(1):
  # print(f"bbbbbb: {inputs}")
  for a in range(len(outs)):
    final = get_x(inputs, outs[a])
    error = gateToLearn[a] - final
    print(f"final: {final}")
    outputs.append(final)
    deltaF = final * ( 1 - final) * error

  errors_line = []
  new_wiedths = []
  # print(f"outs:: {outs}{inputs} ")
  for i in range(len(inputs)):
    # for j in range(len(outs[0])):
    # print(f"1212121: {len(outs)}")
    deltaW = 0.1 * inputs[i] * deltaF
    # print(f"deltaW1::: {deltaW}")
    # print(f" outs[i][j]: { outs[i][j]}")
    weightsValues = outs[0][i] + deltaW
    # print(f"newwieght::: {weightsValues}")
    errors_line.append(deltaW)
    new_wiedths.append(weightsValues)

  # print(f"deltaF: {deltaF}")
  # print(f"new_wiedths: {new_wiedths}")
  # print(f"inputs: {inputs}")
  # print(f"outs: {outs}")
  return final, errors_line, new_wiedths, deltaF


def get_error_first_line(weights_to_calculate, deltaF, outs ,inputs):
  outs = outs[1:]
  print(f"errorssssss : {weights_to_calculate} {deltaF} {inputs}")
  errors_line = []
  new_wiedths = []
  temp = []
  # print(f"weights_to_calculate::: {weights_to_calculate}")

  for i in range(len(inputs)):
    deltaOc1 = outs[i] * ( 1 - outs[i]) * deltaF
    print(f"deltaOc1::: {deltaOc1}")
    for j in range(len(weights_to_calculate[i])):
      # print(f"1212121: {j}")
      # b = inputs[i][j]
      # print(f"aaaaa: {b}")
      print(f"inputs[i]1111111::: {inputs[j]} wwwwwww {weights_to_calculate[i][j]}")
      deltaW = 0.1 * inputs[j] * deltaOc1
      print(f"deltaW2::: {deltaW}")
      print(f"weights_to_calculate[i][j]::: {weights_to_calculate[i][j]}")
      weightsValues = weights_to_calculate[i][j] + deltaW
      print(f"weightsValues::: {weightsValues}")
      errors_line.append(deltaW)
      temp.append(weightsValues)
      print(f"temp: {temp}")
      if(len(temp) == 3):
        print(f"insideeeee::: {weightsValues}")
        new_wiedths.append(temp)
        temp = []
  # print(f"new_wiedthsssssssssssss: {new_wiedths}")
  return new_wiedths, errors_line

def create_graph(elements,title):  
  x = np.arange(0, len(elements))
  y = elements

  fig, ax = plt.subplots()
  fig.suptitle(title, fontsize=20)
  # plt.xlabel('xlabel', fontsize=18)
  # plt.ylabel('ylabel', fontsize=16)
  ax.plot(x, y)
  plt.show()



if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-xor", '--orGate',
                        help='Ejecutar compuerta OR', action='store_true')
  parser.add_argument("-n", '--amountPr',
                        help='Ejecutar compuerta OR', action='store_true')

  args = parser.parse_args()
  xorOption = args.orGate
  gateToLearn = ""

  inputs = [
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 1]
  ]
  inputs2 = [
    [1, 0, 1]
  ]
  orGateOutput = [0,1,1,1]
  andGateOutput = [0,0,0,1]
  xorGateOutput = [0,1,1,0]
  learning_rate = 0.1
  if xorOption:
    gateToLearn = xorGateOutput

  first_line = [weights.first_line_1_wights_values(),weights.first_line_2_wights_values(),weights.second_line_1_wights_values()]
  outs = [weights.second_line_2_wights_values()]
  # first_res = first_percep_lin(gateToLearn, inputs)

  # print(first_res)
  resp_total = []
  errs = []
  for h in range(1000):
    for i in range(len(inputs2)):
      print(inputs2[i])
      
      second_res = second_percep_lin(inputs2[i], first_line)

      # print(f"secccccc: {second_res}")

      third_res, errors_line, new_wei, deltaF = third_percep_lin (gateToLearn,second_res,outs)

      # print(f"deltaFssssssss: {deltaF}")
      resp_total.append(third_res)
      errs.append(errors_line)
      print(third_res)

      outs = [new_wei]
      print(f"outs: {outs}")
      
      first_line, errs = get_error_first_line(first_line, deltaF, second_res, inputs2[i])
      # print(f"first_line111111111111: {first_line}")
    # get_error
  create_graph(resp_total, "total")
  create_graph(errs, "errs")