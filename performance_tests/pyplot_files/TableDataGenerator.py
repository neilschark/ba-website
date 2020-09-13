import json

def write_table_data(data, save_filename, cut_front=0, cut_back=0):
    # delete entries that are too early:
    for deployment, deployment_data in data.items():
        for i in range(0, cut_front):
            del(deployment_data["x"][0])
            del(deployment_data["y"][0])

    # delete entries that are too late:
    for deployment, deployment_data in data.items():
        for i in range(0, cut_back):
            del(deployment_data["x"][-1])
            del(deployment_data["y"][-1])
            
    sorted_data = {}
    for deployment, deployment_data in data.items():
        sorted_data[deployment] = {}
        for i, element in enumerate(deployment_data["x"]):
            try:
                sorted_data[deployment][element].append(deployment_data["y"][i])
            except KeyError:
                sorted_data[deployment][element] = []
                sorted_data[deployment][element].append(deployment_data["y"][i])

    for deployment, deployment_data in sorted_data.items():
        for users, value_list in deployment_data.items():
            value_list_copy = value_list.copy()
            if len(value_list_copy) > 10:
                for _ in range(0, 4):
                    del value_list_copy[0]
                    del value_list_copy[-1]
                    
            average = round(sum(value_list_copy)/len(value_list_copy), 2)
            sorted_data[deployment][users] = {"values": value_list, "average": average}


    with open(f"../table_data/{save_filename}.json", "w") as json_file:
        json_file.write(json.dumps(sorted_data, indent=4))
