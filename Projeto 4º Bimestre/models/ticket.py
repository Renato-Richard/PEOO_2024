import json
from models.crud import CRUD
class Ticket:
    def __init__(self, ticket_id, user_id, show_id, ticket_price, is_used, updated_at):
        self.__ticket_id = ticket_id
        self.__user_id = user_id
        self.__show_id = show_id
        self.__ticket_price = ticket_price
        self.__updated_at = updated_at
    def ticket_limit(self):
        pass
    def to_json(self):
        pass
    def __str__(self):
        return f"{self.__ticket_id} - {self.__user_id} - {self.__show_id} - {self.__ticket_price} - {self.__is_used} - {self.__updated_at}"
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