import json
from datetime import datetime
from models.crud import CRUD
class Ticket:
    def __init__(self, id, show_id, ticket_price, updated_at: datetime):
        self.id = id
        self.__show_id = show_id
        self.__ticket_price = ticket_price
        self.__updated_at = updated_at
    def ticket_limit(self):
        pass
    def to_json(self):
        dic = {}
        dic["id"] = self.id
        dic["show_id"] = self.__show_id
        dic["ticket_price"] = self.__ticket_price
        if isinstance(self.__updated_at, datetime):
            dic["updated_at"] = self.__updated_at.strftime("%d/%m/%Y %H:%M")
        else:
            dic["updated_at"] = self.__updated_at
        return dic
    def __str__(self):
        return f"{self.id} - {self.__show_id} - {self.__ticket_price} - {self.__updated_at}"
class Tickets(CRUD):
    @classmethod
    def save(cls):
        with open("json/tickets.json", mode="w") as file:
            json.dump([obj.to_json() for obj in cls.objetos], file, default=str, indent=4)
    @classmethod
    def open(cls):
        cls.objetos = []
        try:
            with open("json/tickets.json", mode="r") as file:
                text = json.load(file)
            for obj in text:   
                t = Tickets(obj["id"], ["show_id"], ["ticket_price"], ["updated_at"])
                cls.objetos.append(t)
        except FileNotFoundError:
            pass