import argparse
import math

import matplotlib.pyplot as plt
import numpy as np

import read_images
import random


def activation_function_calculation(inputs, weights_val):
    x = 0
    for index, input in enumerate(inputs):
      x += input * weights_val[index]
    real_output = 1 / (1 + math.exp(-x))
    return real_output


def back_propagation_calculation(gateToLearn, inputs, hidden_layer_weights, output_calculated_weigths, output_weigths, real_output, lerning_rate, all_time_weights_h, all_time_weights_o, calculate_bp):
    if calculate_bp:
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
    else:
        return hidden_layer_weights, output_weigths, 0, real_output, all_time_weights_h, all_time_weights_o


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


def create_graph(elements):
    for i in range(len(elements)):
      x = np.arange(0, len(elements[i]))
      y = elements[i]
      plt.plot(x, y)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", '--numberOfCels',
                          help='Ejecutar compuerta OR')
    parser.add_argument("-m", '--numberOfEntriesPerCell',
                          help='Ejecutar compuerta OR')

    args = parser.parse_args()
    number_of_cells = args.numberOfCels
    number_of_entries_per_cells = args.numberOfEntriesPerCell
    gateToLearn = ""


    imagesA01 = read_images.get_pixels('images/1A4353.jpg')
    imagesB01 = read_images.get_pixels('images/1B4698.jpg')
    imagesA02 = read_images.get_pixels('images/2A4353.jpg')
    imagesB02 = read_images.get_pixels('images/2B4698.jpg')
    imagesA03 = read_images.get_pixels('images/3A4353.jpg')
    imagesB03 = read_images.get_pixels('images/3B4698.jpg')
    imagesA04 = read_images.get_pixels('images/4A4353.jpg')
    imagesB04 = read_images.get_pixels('images/4B4698.jpg')
    imagesA05 = read_images.get_pixels('images/5A4353.jpg')
    imagesB05 = read_images.get_pixels('images/5B4698.jpg')
    imagesA06 = read_images.get_pixels('images/6A4353.jpg')
    imagesB06 = read_images.get_pixels('images/6B4698.jpg')
    imagesA07 = read_images.get_pixels('images/7A4353.jpg')
    imagesB07 = read_images.get_pixels('images/7B4698.jpg')
    imagesA08 = read_images.get_pixels('images/8A4353.jpg')
    imagesB08 = read_images.get_pixels('images/8B4698.jpg')


    inputs = [
        [imagesA01, 0, True],
        [imagesB01, 1, True],
        [imagesA02, 0, True],
        [imagesB02, 1, True],
        [imagesA03, 0, True],
        [imagesB03, 1, True],
        [imagesA04, 0, True],
        [imagesB04, 1, True],
        [imagesA05, 0, True],
        [imagesB05, 1, True],
        [imagesA06, 0, False],
        [imagesB06, 1, False],
        [imagesA07, 0, False],
        [imagesB07, 1, False],
        [imagesA08, 0, False],
        [imagesB08, 1, False],
    ]

    number_of_cells = 100
    number_of_entries_per_cells = 7680

    hidden_layer_weights = random_weights(number_of_cells, number_of_entries_per_cells)
    output_weigths = random_weights(1, int(number_of_cells) + 1)

    iterations = 0
    max_iter = 10000
    hidden_layer_res = []
    lerning_rate = 0.5
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
        if(len(temp_weigths) == 7680):
          splited_weights.append(temp_weigths)
          temp_weigths = []

    print(f"hidden_layer_weights: {hidden_layer_weights}")
    print(f"hidden_layer_weights: {len(hidden_layer_weights)}")

    print(f"splited_weights: {splited_weights}")
    print((f"splited_weights {len(splited_weights)}"))

    while iterations < max_iter:
        for i in range(len(inputs)):
            print("Calculo salidas capa oculta")
            output_layer = [1]
            for j in range(len(splited_weights)):
              hidden_layer_res = activation_function_calculation(inputs[i][0], splited_weights[j])
              output_layer.append(hidden_layer_res)

            output_activation_res = activation_function_calculation(output_layer, output_weigths)

            splited_weights, output_weigths, error, real_output, all_time_weights_h, all_time_weights_o = back_propagation_calculation(inputs[i][1], inputs[i][0], splited_weights, output_layer, output_weigths, output_activation_res, lerning_rate, all_time_weights_h, all_time_weights_o, inputs[i][2])
            errs_total[i].append(error)
            real_output_total[i].append(real_output)
        err = check_error(errs_total, tolerance)
        print(f"err: {err}")
        if err:
          break

        iterations += 1
    print(f"Iteraciones totales: {iterations}")
    #hidden_graph_h = historical_values(all_time_weights_h, hidden_graph_h, 9)
    #hidden_graph_o = historical_values(all_time_weights_o, hidden_graph_o, 4)
    #hidden_graph.extend(hidden_graph_h)
    #hidden_graph.extend(hidden_graph_o)

    create_graph(errs_total)
    resp_to_graph = real_output_total[-6:]
    create_graph(resp_to_graph)
    #create_graph(hidden_graph, weights_legends)
    # create_graph(real_output_total, inputs)
