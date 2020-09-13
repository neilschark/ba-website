import random
import time
import requests
from locust import HttpUser, task, between, events


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    env = kwargs["environment"]
    print("Flushing databases, this may take a while...")
    requests.delete(f"{env.host}/api/delete/integers")
    requests.delete(f"{env.host}/api/delete/strings")
    requests.delete(f"{env.host}/api/delete/bytes")
    print("databases flushed!")


class DatabaseUser(HttpUser):
    wait_time = between(1, 1)

    def __init__(self, user):
        super().__init__(user)
        self.known_strings = []

    def on_start(self):
        for _ in range(0, 1):
            self.known_strings.append(self.client.post(
                "/api/create/simple-string",
                json={"max_string_size": 10}, name="[INIT]/api/create/simple-string[INIT]"
            ).json()["id"])
        print("on_start done!")

    #@task(5)
    #def create_string(self):
    #    if len(self.known_strings) < 5:
    #        self.known_strings.append(
    #            self.client.post(
    #                "/api/create/simple-string", json={"max_string_size": 20}
    #            ).json()["id"]
    #        )

    #@task(5)
    #def get_string(self):
    #    if self.known_strings:
    #        self.client.get(f"/api/get/string/{random.choice(self.known_strings)}", name="/api/get/string/[id]")

    @task
    def get_string(self):
        if self.known_strings:
            self.client.get(f"/api/get/string/{self.known_strings[0]}", name="/api/get/string/[id]")

    #@task(5)
    #def delete_string(self):
    #    if self.known_strings:
    #        id_to_delete = random.choice(self.known_strings)
    #        self.client.delete(f"/api/delete/string/{id_to_delete}", name="/api/delete/string/[id]")
    #        self.known_strings.remove(id_to_delete)

    #@task(2)
    #def get_multiple_strings(self):
    #    self.client.get("/api/get/strings/3")
