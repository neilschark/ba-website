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
        self.known_ints = []

    def on_start(self):
        self.known_ints = self.known_ints + self.client.post(
            "/api/create/random-integers",
            json={"number_of_integers": 3, "seed": time.time()}, name="[INIT]/api/create/random-integers[INIT]"
        ).json()["ids"]
        print("on_start done!")

    @task
    def do_stuff(self):
        self.get_integer()
        self.create_integer()
        self.get_integer()
        self.create_integer()
        self.delete_integer()
        self.get_integer()
        self.delete_integer()
        self.get_integers()
       

    def create_integer(self):
        if len(self.known_ints) < 2000:
            self.known_ints.append(
                self.client.post(
                    "/api/create/random-integer", json={"seed": time.time()}
                ).json()["id"]
            )


    def get_integer(self):
        if self.known_ints:
            self.client.get(f"/api/get/integer/{random.choice(self.known_ints)}", name="/api/get/integer/[id]")


    def delete_integer(self):
        if self.known_ints:
            id_to_delete = random.choice(self.known_ints)
            self.client.delete(f"/api/delete/integer/{id_to_delete}", name="/api/delete/integer/[id]")
            self.known_ints.remove(id_to_delete)


    def get_integers(self):
        self.client.get("/api/get/integers/100")
