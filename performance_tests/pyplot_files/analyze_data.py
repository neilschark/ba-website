import os
import sys
import multiprocessing
import time

start = time.time()

timestamp = sys.argv[1]
data_type = sys.argv[2]

try:
    subprocesses = int(sys.argv[3])
except IndexError:
    subprocesses = os.cpu_count()

commands = [
"python database_int_step350_latency.py",
"python database_int_step350_rps.py",
"python database_int_step350_latency_zoom.py",
"python database_int_step350_rps_zoom.py",
"python database_string_step40_latency.py",
"python database_string_step40_rps.py",
"python factorial_step800_latency.py",
"python factorial_step800_rps.py",
"python factorial_step800_latency_zoom.py",
"python factorial_step800_rps_zoom.py",
"python factorial_250_latency.py",
"python factorial_250_rps.py",
"python factorial_500_latency.py",
"python factorial_500_rps.py",
"python database_int_125_latency.py",
"python database_int_125_rps.py",
"python database_int_250_latency.py",
"python database_int_250_rps.py",
"python database_string_25_latency.py",
"python database_string_25_rps.py",
"python database_string_10_latency.py",
"python database_string_10_rps.py",
]

def do_command(command_in):
    os.system(command_in)


for i, command in enumerate(commands): 
    commands[i] = command + f" {str(timestamp)} {str(data_type)}"

pool = multiprocessing.Pool(processes=subprocesses)
pool.map(do_command, commands)
pool.close()
end = time.time()
duration = end - start
print(f"All done in {duration} seconds!")