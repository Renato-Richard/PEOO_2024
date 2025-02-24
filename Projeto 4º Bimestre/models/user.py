import json
from models.crud import CRUD
class User:
    def __init__(self, user_id):
        self.__user_id = user_id
    def to_json(self):
        dic = {}
    def __str__(self):
        return f"{self.__user_id}"
class Users(CRUD):
    @classmethod
    def save(cls):
        with open("users.json", mode="w") as file:
            json.dump(cls.objetos, file, default = vars)
    @classmethod
    def open(cls):
        cls.objetos = []
        try:
            with open("users.json", mode="r") as file:
                text = json.load(file)
            for obj in text:   
                u = User(obj["user_id"])
            cls.objetos.append(u)
        except FileNotFoundError:
            pass