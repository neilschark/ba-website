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
        self.known_bytes = []

    def on_start(self):
        for _ in range(0, 2):
            self.known_bytes.append(self.client.post(
                "/api/create/zero-bytes",
                json={"max_byte_size": 10}, name="[INIT]/api/create/zero-bytes[INIT]"
            ).json()["id"])
        print("on_start done!")

    @task(5)
    def create_bytes(self):
        if len(self.known_bytes) < 5:
            self.known_bytes.append(
                self.client.post(
                    "/api/create/zero-bytes", json={"max_byte_size": 10}
                ).json()["id"]
            )

    @task(5)
    def get_bytes(self):
        if self.known_bytes:
            self.client.get(f"/api/get/bytes/{random.choice(self.known_bytes)}", name="/api/get/bytes/[id]")

    @task(5)
    def delete_bytes(self):
        if self.known_bytes:
            id_to_delete = random.choice(self.known_bytes)
            self.client.delete(f"/api/delete/bytes/{id_to_delete}", name="/api/delete/bytes/[id]")
            self.known_bytes.remove(id_to_delete)

    #@task(2)
    #def get_multiple_bytes(self):
    #    self.client.get("/api/get/multiple-bytes/3")
