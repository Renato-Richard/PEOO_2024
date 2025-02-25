import json
from models.crud import CRUD
class Ticket:
    def __init__(self, ticket_id):
        self.__ticket_id = ticket_id
    def to_json(self):
        pass
    def __str__(self):
        return f"{self.__ticket_id}"
class Tickets(CRUD):
    @classmethod
    def save(cls):
        with open("tickets.json", mode="w") as file:
            json.dump(cls.objetos, file, default = vars)
    @classmethod
    def open(cls):
        cls.objetos = []
        try:
            with open("tickets.json", mode="r") as file:
                text = json.load(file)
            for obj in text:   
                t = Tickets(obj["ticket_id"])
            cls.objetos.append(t)
        except FileNotFoundError:
            pass