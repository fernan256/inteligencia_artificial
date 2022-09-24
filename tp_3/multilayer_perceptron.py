import argparse
import weights

def get_x(inputs, weights_val):
  x = 0
  print(inputs)
  print(weights_val)
  for index, input in enumerate(inputs):
    print(inputs)
    print(weights_val)
    x += input * weights_val[index]
  return x

def first_percep_lin(gateToLearn, inputs):
  print("first inputs")
  weightsL1 = weights.first_line_1_wights_values()
  weightsL2 = weights.first_line_2_wights_values()
  second_inputs = []
  for i in range(4):
    first_res = get_x(inputs[i], weightsL1)
    second_res = get_x(inputs[i], weightsL2)
    second_inputs.append([1,first_res,second_res])
  return second_inputs

def second_percep_lin(gateToLearn, inputs):
  print("seconds inputs")
  weightsL3 = weights.second_line_1_wights_values()
  weightsL4 = weights.second_line_2_wights_values()
  weightsL5 = weights.second_line_3_wights_values()
  third_inputs = []
  for i in range(4):
    first_res = get_x(inputs[i], weightsL3)
    second_res = get_x(inputs[i], weightsL4)
    third_res = get_x(inputs[i], weightsL5)
    third_inputs.append([1,first_res,second_res,third_res])
  return third_inputs

def third_percep_lin(gateToLearn, inputs):
  print("thirds inputs")
  weightsL6 = weights.third_line_wights_values()
  final = 0
  for i in range(4):
    final = get_x(inputs[i], weightsL6)
  return final



if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-or", '--orGate',
                        help='Ejecutar compuerta OR', action='store_true')
  args = parser.parse_args()
  orOption = args.orGate
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
  
  first_res = first_percep_lin(gateToLearn, inputs)

  print(first_res)

  second_res = second_percep_lin (gateToLearn,first_res)

  print(second_res)

  third_res = third_percep_lin (gateToLearn,second_res)

  print(third_res)
