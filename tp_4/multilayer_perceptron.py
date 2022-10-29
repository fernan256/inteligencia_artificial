import argparse
import weights
import math

import matplotlib.pyplot as plt
import numpy as np

import random


def activation_function_calculation(inputs, weights_val):
    x = 0
    for index, input in enumerate(inputs):
      x += input * weights_val[index]
    real_output = 1 / (1 + math.exp(-x))
    return real_output


def back_propagation_calculation(gateToLearn, inputs, hidden_layer_weights, output_calculated_weigths, output_weigths, real_output, lerning_rate, all_time_weights_h, all_time_weights_o):
    error = gateToLearn - real_output
    print(f"error: {error}")
    print(f"real_output: {real_output}")
    delta_f = real_output * (1 - real_output) * error
    # print(f"delta_f: {delta_f}")
   
    for i in range(len(hidden_layer_weights)):
        activation_hidden = output_calculated_weigths[1:]
        delta_f_hidden = activation_hidden[i] * (1 - activation_hidden[i]) * delta_f
        for j in range(len(hidden_layer_weights[i])):
            delta_w_h = lerning_rate * inputs[j] * delta_f_hidden
            hidden_layer_weights[i][j] = hidden_layer_weights[i][j] + delta_w_h
            # print(hidden_layer_weights[i][j])
            all_time_weights_h.append(hidden_layer_weights[i][j])
    
    for k in range(len(output_calculated_weigths)):
        # print(f"output_calculated_weidgths[k]: {output_calculated_weigths[k]}")
        delta_w_o = lerning_rate * output_calculated_weigths[k] * delta_f
        # print(f"delta_w_o: {delta_w_o}")
        # print(f"output_weidgths[k]: {output_weigths[k]}")
        output_weigths[k] = output_weigths[k] + delta_w_o
        # print(f"output_weidgths[k]: {output_weigths[k]}")
        all_time_weights_o.append(output_weigths[k])
    # print(f"hidden_layer_weidghts: {hidden_layer_weights}")
    # print(f"output_weidgths: {output_weigths}")

    # print(f"all_time_weights: {all_time_weights_o}")
    return hidden_layer_weights, output_weigths, error, real_output, all_time_weights_h, all_time_weights_o


def historical_values(all_time_values, hidden_graph_values, number_elements):
    m = 0
    for n in range(len(all_time_values)):
      if m == number_elements:
        m = 0
      hidden_graph_values[m].append(all_time_values[n])
      m += 1

    return hidden_graph_values


def random_weights(number_of_cells, number_of_entries):
    amount_entries = int(number_of_cells) * int(number_of_entries)
    result_arr = []
    n = 0
    while n in range(amount_entries):
      val = random.uniform(-1,1)
      result_arr.append(val)
      n += 1
    print(result_arr)
    return result_arr


def check_error(errorList, tolerance):
    sum_err = 0
    for i in range(len(errorList)):
        for x in errorList[i]:
          sum_err += abs(x)
        final_err_per_n = sum_err / len(errorList[i])
    final_err = final_err_per_n / len(errorList)
    print(f"final_err: {final_err}")
    if final_err <= tolerance:
      return True


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
    parser.add_argument("-n", '--numberOfCels',
                          help='Ejecutar compuerta OR')
    parser.add_argument("-m", '--numberOfEntriesPerCell',
                          help='Ejecutar compuerta OR')

    args = parser.parse_args()
    orOption = args.orGate
    andOption = args.andGate
    xorOPtion = args.xorGate
    number_of_cells = args.numberOfCels
    number_of_entries_per_cells = args.numberOfEntriesPerCell
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

    hidden_layer_weights = random_weights(number_of_cells, number_of_entries_per_cells)
    output_weigths = random_weights(1, int(number_of_cells) + 1)

    iterations = 0
    max_iter = 10000
    hidden_layer_res = []
    lerning_rate = 0.4
    tolerance = 0.1
    errs_total = []
    real_output_total = []
    hidden_graph_h = []
    hidden_graph_o = []
    all_time_weights_h = []
    all_time_weights_o = []
    splited_weights = []
    temp_weigths = []

    hidden_graph = []

    weights_legends = []

    all_time_weights_h.extend(hidden_layer_weights)
    all_time_weights_o.extend(output_weigths)

    for i in range(len(hidden_layer_weights)):
        hidden_graph_h.append([])

    for i in range(len(output_weigths)):
        hidden_graph_o.append([])

    temp_weights_legends = []
    temp_weights_legends.extend(hidden_graph_h)
    temp_weights_legends.extend(hidden_graph_o)

    for i in range(len(temp_weights_legends)):
        weights_legends.append(f"w{i}")

    for i in range(len(inputs)):
        errs_total.append([])

    for i in range(len(inputs)):
        real_output_total.append([])

    for n in range(len(hidden_layer_weights)):
        temp_weigths.append(hidden_layer_weights[n])
        if(len(temp_weigths) == 3):
          splited_weights.append(temp_weigths)
          temp_weigths = []

    while iterations < max_iter:
        for i in range(len(inputs)):
            print("Calculo salidas capa oculta")
            output_layer = [1]
            for j in range(len(splited_weights)):
              hidden_layer_res = activation_function_calculation(inputs[i], splited_weights[j])
              output_layer.append(hidden_layer_res)
            
            output_activation_res = activation_function_calculation(output_layer, output_weigths)

            splited_weights, output_weigths, error, real_output, all_time_weights_h, all_time_weights_o = back_propagation_calculation(gateToLearn[i], inputs[i], splited_weights, output_layer, output_weigths, output_activation_res, lerning_rate, all_time_weights_h, all_time_weights_o)
            errs_total[i].append(error)
            real_output_total[i].append(real_output)
        err = check_error(errs_total, tolerance)
        print(f"err: {err}")
        if err:
          break
            
        iterations += 1
    print(f"Iteraciones totales: {iterations}")
    hidden_graph_h = historical_values(all_time_weights_h, hidden_graph_h, 9)
    hidden_graph_o = historical_values(all_time_weights_o, hidden_graph_o, 4)
    hidden_graph.extend(hidden_graph_h)
    hidden_graph.extend(hidden_graph_o)

    create_graph(errs_total, inputs)
    create_graph(hidden_graph, weights_legends)
    # create_graph(real_output_total, inputs)