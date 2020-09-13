import random
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


class FactorialUser(HttpUser):
    wait_time = between(1, 1)

    @task
    def factorize_number(self):
        self.client.get("/api/factorial/10000")
