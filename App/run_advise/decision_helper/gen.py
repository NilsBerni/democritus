
import csv
import os.path

import numpy

my_path = os.path.abspath(os.path.dirname(__file__))
strongest_weakest_path = os.path.join(my_path, "data/strongest_weakest.csv")
suffix_pred_path = os.path.join(my_path, "data/suffix_pred.csv")
event_pred_path = os.path.join(my_path, "data/event_pred.csv")
output_path = os.path.join(my_path, "data/value_matrix.csv")

def createValMatrix(path, output_name, imp_strong_dict):
    with open(path, 'r') as file:

        reader = csv.reader(file, delimiter=';')
        logValueMatrix = {}
        outputCsv = []
        for row in reader:
            print(row)

            data_values = row.copy()
            data_values.pop(0)

            try:
                date_values_double = [float(numeric_string) for numeric_string in data_values]
                date_values_double.sort()
                print(date_values_double)

                l = len(data_values)
                for idx, item in enumerate(data_values):
                    fItem = float(item)
                    if fItem == date_values_double[0]:
                        data_values[idx] = 2
                    elif fItem == date_values_double[1]:
                        data_values[idx] = 1
                    elif fItem == date_values_double[l-2]:
                        data_values[idx] = -1
                    elif fItem == date_values_double[l-1]:
                        data_values[idx] = -2
                    else:
                        data_values[idx] = 0

                logValueMatrix[row[0]] = data_values

            except:
                logValueMatrix[row[0]] = data_values


        outputCsv.append(['Dataset']+ logValueMatrix['Dataset'])
        for key, value in imp_strong_dict.items():
            outputCsv.append([key]+logValueMatrix[value])


    with open(f'output/{output_name}.csv', 'w', newline='') as output:
        csvWriter = csv.writer(output, delimiter=';')
        csvWriter.writerows(outputCsv)



with open(strongest_weakest_path) as file:

    s_w_dict = {}
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        s_w_dict[row[0]] = row[1]

    createValMatrix(event_pred_path, "event_matrix", s_w_dict)