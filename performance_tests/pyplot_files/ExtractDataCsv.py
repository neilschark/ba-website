import csv
from TableDataGenerator import write_table_data

def extract_data_csv(deployments, timestamp, test_type, x_position, y_position, calc_average=True):
    data = {}
    for deployment in deployments:
        with open(
            f"../test_results/stats_history/{timestamp}__{deployment}__{test_type}_stats_history.csv", "r"
        ) as csvfile:
            # Initialize lists
            try:
                data[deployment]["x"] = []
            except KeyError:
                data[deployment] = {}
                data[deployment]["x"] = []
            data[deployment]["y"] = []

            reader = csv.reader(csvfile, delimiter=",")
            # Skip header
            next(reader)

            temp_dict = {}

            for row in reader:
                x_value = row[x_position]
                y_value = row[y_position]
                try:
                    x_value = int(x_value)
                except ValueError:
                    x_value = 0
                try:
                    y_value = float(y_value)
                except ValueError:
                    y_value = float(0.0)

                try:
                    temp_dict[x_value].append(y_value)
                except KeyError:
                    temp_dict[x_value] = [y_value]

        if calc_average:
            average_dict = {}
            for key, value in temp_dict.items():
                if key != 0 and len(value) > 2:
                    #calc average
                    average_dict[key] = round(sum(value)/len(value), 2)

            for key, value in average_dict.items():
                data[deployment]["x"].append(key)
                data[deployment]["y"].append(value)
        else:
            for key, value in temp_dict.items():
                for element in value:
                    data[deployment]["x"].append(key)
                    data[deployment]["y"].append(element)

    return data
