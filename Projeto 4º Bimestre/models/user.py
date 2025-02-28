import json
from models.crud import CRUD
class User:
    def __init__(self, user_id, user_name, email, password, birth_date, created_at, updated_at):
        self.__user_id = user_id
        self.__user_name = user_name
        self.__email = email
        self.__password = password
        self.__birth_date = birth_date
        self.__created_at = created_at
        self.__updated_at = updated_at
    def to_json(self):
        pass
    def __str__(self):
        return f"{self.__user_id} - {self.__user_name} - {self.__email} - {self.__password} - {self.__birth_date} - {self.__created_at} - {self.__updated_at}"
class Users(CRUD):
    @classmethod
    def save(cls):
        with open("json/users.json", mode="w") as file:
            json.dump(cls.objetos, file, default = vars)
    @classmethod
    def open(cls):
        cls.objetos = []
        try:
            with open("json/users.json", mode="r") as file:
                text = json.load(file)
            for obj in text:   
                u = User(obj["user_id"])
            cls.objetos.append(u)
        except FileNotFoundError:
            pass