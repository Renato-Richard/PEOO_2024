import json
from models.crud import CRUD
class Ticket:
    def __init__(self, id, user_id, show_id, ticket_price, is_used, updated_at):
        self.id = id
        self.__user_id = user_id
        self.__show_id = show_id
        self.__ticket_price = ticket_price
        self.__updated_at = updated_at
    def ticket_limit(self):
        pass
    def to_json(self):
        dic = {}
        dic["id"] = self.id
        dic["user_id"] =  self.__user_id
        dic["show_id"] = self.__show_id
        dic["ticket_price"] = self.__ticket_price
        dic["updated_at"] = self.__updated_at.datetime().strftime("%d/%m/%Y %H:%M")
        return dic
    def __str__(self):
        return f"{self.id} - {self.__user_id} - {self.__show_id} - {self.__ticket_price} - {self.__is_used} - {self.__updated_at}"
class Tickets(CRUD):
    @classmethod
    def save(cls):
        with open("json/tickets.json", mode="w") as file:
            json.dump(cls.objetos, file, default = vars)
    @classmethod
    def open(cls):
        cls.objetos = []
        try:
            with open("json/tickets.json", mode="r") as file:
                text = json.load(file)
            for obj in text:   
                t = Tickets(obj["ticket_id"])
                cls.objetos.append(t)
        except FileNotFoundError:
            pass