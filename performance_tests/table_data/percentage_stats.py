import sys

classic = float(sys.argv[1])
docker = float(sys.argv[2])
orchestration = float(sys.argv[3])

delta_docker = docker - classic
delta_orchestration = orchestration - classic

docker_percent = round(-(100-(100/classic)*docker), 2)
orchestration_percent = round(-(100-(100/classic)*orchestration), 2)

classic = str(classic).replace(".", ",")
docker = str(docker).replace(".", ",")
docker_percent = str(docker_percent).replace(".", ",")
orchestration = str(orchestration).replace(".", ",")
orchestration_percent = str(orchestration_percent).replace(".", ",")

print(f"& {classic} & {docker} ({docker_percent}\%) & {orchestration} ({orchestration_percent}\%)\\\ ")