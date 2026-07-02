from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)
    host = "https://programa-informatico-atrapa-suenos.onrender.com"

    @task(3)
    def inicio(self):
        self.client.get("/")

    @task(2)
    def partes_pc(self):
        self.client.get("/Partes del computador")

    @task(1)
    def robot(self):
        self.client.get("/robot_controler")