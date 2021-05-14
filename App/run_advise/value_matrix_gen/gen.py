
import csv
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
strongest_weakest_path = os.path.join(my_path, "data/strongest_weakest.csv")
suffix_pred_path = os.path.join(my_path, "data/suffix_pred.csv")
event_pred_path = os.path.join(my_path, "data/event_pred.csv")
duration_pred_path = os.path.join(my_path, "data/duration_pred.csv")
output_path = os.path.join(my_path, "data/value_matrix.csv")

def createValMatrix(path, output_name):
    with open(path, 'r') as file:

        reader = csv.reader(file, delimiter=';')
        valueMatrix = []
        for row in reader:
            print(row)

            data_values = row
            data_values.pop(0)

            try:
                date_values_double = [float(numeric_string) for numeric_string in data_values]
                date_values_double.sort()
                print(date_values_double)

                l = len(row)
                for idx, item in enumerate(row):
                    fItem = float(item)
                    if fItem == date_values_double[0]:
                        row[idx] = 2
                    elif fItem == date_values_double[1]:
                        row[idx] = 1
                    elif fItem == date_values_double[l-2]:
                        row[idx] = -1
                    elif fItem == date_values_double[l-1]:
                        row[idx] = -2
                    else:
                        row[idx] = 0

                valueMatrix.append(row)

            except:
                valueMatrix.append(row)


    with open(f'output/{output_name}.csv', 'w', newline='') as output:
        csvWriter = csv.writer(output, delimiter=',')
        csvWriter.writerows(valueMatrix)

with open(strongest_weakest_path, 'r') as file:

    reader = csv.reader(file, delimiter=';')
    imp_strong_dict = {}
    imp_weak_dict = {}
    for row in reader:
        imp_strong_dict[row[0]] = row[1]
        imp_weak_dict[row[0]] = row[1]

    createValMatrix(suffix_pred_path, 'suffix_matrix')
    createValMatrix(event_pred_path, 'event_matrix')
    createValMatrix(duration_pred_path, 'duration_matrix')


