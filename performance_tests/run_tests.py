import os
import datetime


class LocustTest:
    def __init__(
        self,
        name,
        filename,
        number_of_users=100,
        spawn_rate=100,
        step_load=False,
        step_users=100,
        step_time="5m",
        run_time="5m",
    ):
        self.name = name
        self.filename = filename
        self.users = number_of_users
        self.spawn_rate = spawn_rate
        self.step_load = step_load
        self.step_users = step_users
        self.step_time = step_time
        self.run_time = run_time


def main():
    timestamp = datetime.datetime.now().replace(microsecond=0).isoformat() #"2020-08-13T00:58:04"
    hosts = [
        {"name": "classic", "url": "http://192.168.69.210:1337"},
        {"name": "docker", "url": "http://192.168.69.211:1337"},
        {"name": "orchestration", "url": "http://192.168.69.212:1337"},
    ]

    tests = []
    tests.append(
        LocustTest(
            name="database_int_step350",
            filename="database_int",
            number_of_users=350,
            spawn_rate=10,
            step_load=True,
            step_users=10,
            step_time="12s",
            run_time="10m",
        )
    )
    tests.append(
        LocustTest(
            name="database_int_250",
            filename="database_int",
            number_of_users=250,
            spawn_rate=50,
            run_time="5m",
        )
    )
    tests.append(
        LocustTest(
            name="database_string_10",
            filename="database_string",
            number_of_users=10,
            spawn_rate=5,
            step_load=False,
            run_time="5m",
        )
    )
    #tests.append(
    #    LocustTest(
    #        name="factorial_500",
    #        filename="factorial",
    #        number_of_users=500,
    #        spawn_rate=100,
    #        step_load=False,
    #        run_time="5m",
    #    )
    #)
    #tests.append(
    #    LocustTest(
    #        name="factorial_250",
    #        filename="factorial",
    #        number_of_users=250,
    #        spawn_rate=100,
    #        step_load=False,
    #        run_time="5m",
    #    )
    #)
    #tests.append(
    #    LocustTest(
    #        name="database_string_25",
    #        filename="database_string",
    #        number_of_users=25,
    #        spawn_rate=5,
    #        step_load=False,
    #        run_time="5m",
    #    )
    #)
    #tests.append(
    #    LocustTest(
    #        name="database_int_125",
    #        filename="database_int",
    #        number_of_users=125,
    #        spawn_rate=25,
    #        step_load=False,
    #        run_time="5m",
    #    )
    #)

    

    for host in hosts:
        for test in tests:
            if test.step_load:
                command = f'locust -f ./locustfiles/{test.filename}.py --headless --host {host["url"]} -u {test.users} -r {test.spawn_rate} --run-time {test.run_time} --step-load --step-users {test.step_users} --step-time {test.step_time} --csv={timestamp}__{host["name"]}__{test.name}'
            else:
                command = f'locust -f ./locustfiles/{test.filename}.py --headless --host {host["url"]} -u {test.users} -r {test.spawn_rate} --run-time {test.run_time} --csv={timestamp}__{host["name"]}__{test.name}'
            os.system(command)

    os.system("mv *failures*.csv ./test_results/failures")
    os.system("mv *stats_history*.csv ./test_results/stats_history")
    os.system("mv *stats*.csv ./test_results/stats")


if __name__ == "__main__":
    main()


#    tests.append(
#        LocustTest(
#            name="factorial_step800",
#            filename="factorial",
#            number_of_users = 800,
#            spawn_rate=10,
#            step_load=True,
#            step_users=10,
#            step_time="2s",
#            run_time="3m",
#        )
#    )
#    tests.append(
#        LocustTest(
#            name="database_string_step40",
#            filename="database_string",
#            number_of_users = 40,
#            spawn_rate=1,
#            step_load=True,
#            step_users=1,
#            step_time="2s",
#            run_time="2m",
#        )
#    )
#    tests.append(
#        LocustTest(
#            name="database_int_step200",
#            filename="database_int",
#            number_of_users = 200,
#            spawn_rate=4,
#            step_load=True,
#            step_users=4,
#            step_time="2s",
#            run_time="2m",
#        )
#    )

#tests.append(
    #    LocustTest(
    #        name="factorial_step800",
    #        filename="factorial",
    #        number_of_users=800,
    #        spawn_rate=10,
    #        step_load=True,
    #        step_users=10,
    #        step_time="12s",
    #        run_time="16m",
    #    )
    #)
    #tests.append(
    #    LocustTest(
    #        name="database_string_step40",
    #        filename="database_string",
    #        number_of_users=40,
    #        spawn_rate=1,
    #        step_load=True,
    #        step_users=1,
    #        step_time="12s",
    #        run_time="9m",
    #    )
    #)
    #tests.append(
    #    LocustTest(
    #        name="database_int_step200",
    #        filename="database_int",
    #        number_of_users=200,
    #        spawn_rate=4,
    #        step_load=True,
    #        step_users=4,
    #        step_time="12s",
    #        run_time="9m",
    #    )
    #)