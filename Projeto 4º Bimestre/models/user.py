import json
from datetime import datetime, date
from models.crud import CRUD
class User:
    def __init__(self, id, user_name, email, password, birth_date):
        self.id = id
        self.__user_name = user_name
        self.__email = email
        self.__password = password
        self.__birth_date = birth_date
        self.__created_at = datetime.now()
        # self.__updated_at = updated_at
    def to_json(self):
        dic = {}
        dic["id"] = self.id
        dic["user_name"] =  self.__user_name
        dic["email"] = self.__email
        dic["password"] = self.__password
        if isinstance(self.__birth_date, date):
            dic["birth_date"] = self.__birth_date.strftime("%d/%m/%Y")
        else:
            dic["birth_date"] = self.__birth_date
        if isinstance(self.__created_at, datetime):
            dic["created_at"] = self.__created_at.strftime("%d/%m/%Y %H:%M")
        else:
            dic["created_at"] = self.__created_at
        # dic["updated_at"] = self.__updated_at.strftime("%d/%m/%Y %H:%M")
        return dic
    def __str__(self):
        return f"{self.id} - {self.__user_name} - {self.__email} - {self.__password} - {self.__birth_date} - {self.__created_at} - {self.__updated_at}"
class Users(CRUD):
    @classmethod
    def save(cls):
        with open("json/users.json", mode="w") as file:
            json.dump([obj.to_json() for obj in cls.objetos], file, default=str, indent=4)
    @classmethod
    def open(cls):
        cls.objetos = []
        try:
            with open("json/users.json", mode="r") as file:
                text = json.load(file)
            for obj in text:
                birth_date = datetime.strptime(obj["birth_date"], "%d/%m/%Y") if isinstance(obj["birth_date"], str) else obj["birth_date"]
                created_at = datetime.strptime(obj["created_at"], "%d/%m/%Y %H:%M") if isinstance(obj["created_at"], str) else obj["created_at"]
                u = User(obj["id"], obj["user_name"], obj["email"], obj["password"], birth_date)
                cls.objetos.append(u)
        except FileNotFoundError:
            pass