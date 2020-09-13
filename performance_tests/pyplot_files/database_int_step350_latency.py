import matplotlib.pyplot as plt
import sys
from ExtractDataCsv import extract_data_csv
from TableDataGenerator import write_table_data

timestamp = sys.argv[1]
data_type = sys.argv[2]
test_type = "database_int_step350"
deployments = ["classic", "docker", "orchestration"]
save_filename = f"{timestamp}__{test_type}_latency"
average_data = {}

# Get data from csv
data = extract_data_csv(deployments, timestamp, test_type, x_position=1, y_position=14)

cut_front = 0
cut_back = 0

write_table_data(data, save_filename, cut_front, cut_back)

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

#calculate average
#for deployment, deployment_data in data.items():
#    average_data[deployment] = round(sum(deployment_data["y"])/len(deployment_data["y"]), 2)

# get first timestamp
#start_timestamps = {}
#for deployment in deployments:
#    start_timestamps[deployment] = data[deployment]["x"][0]
## Calc timestamps starting from 0
#for deployment, deployment_data in data.items():
#    for iterator, timestamp in enumerate(deployment_data["x"]):
#        deployment_data["x"][iterator] = timestamp - start_timestamps[deployment]

plt.plot(data["classic"]["x"], data["classic"]["y"], color="tab:blue", marker=".")
plt.plot(data["docker"]["x"], data["docker"]["y"], color="tab:green", marker=".")
plt.plot(data["orchestration"]["x"], data["orchestration"]["y"], color="tab:orange", marker=".")

plt.title("Datenbank (Integer): Latenz der Antwort (99,9%ile, ms)")
plt.xlabel("Anzahl der Nutzer")
plt.ylabel("Latenz der Antwort (99,9%ile, ms)")
#plt.legend([f'Klassisch (Ø: {average_data["classic"]})', f'Docker (Ø: {average_data["docker"]})', f'K3s (Ø: {average_data["orchestration"]})'], loc=0)
plt.legend(['Klassisch', 'Docker', 'K3s'], loc=0)

# Limit graph scale:
#plt.xlim(0)
#plt.ylim(96, 102)

plt.savefig(f"../graphs/{save_filename}.{data_type}")
