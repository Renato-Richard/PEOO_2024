import json
from models.crud import CRUD
from datetime import datetime
class City:
    def __init__(self, id: int, city_name: str, total_shows_by_city: int, updated_at):
        self.id = id
        self.__city_name = city_name
        self.__total_shows_by_city = total_shows_by_city
        self.__updated_at = updated_at
    def to_json(self):
        dic = {}
        dic["id"] = self.id
        dic["city_name"] =  self.__city_name
        dic["total_shows_by_city"] = self.__total_shows_by_city
        if isinstance(self.__updated_at, datetime):
            dic["updated_at"] = self.__updated_at.strftime("%d/%m/%Y %H:%M")
        else:
            dic["updated_at"] = self.__updated_at
        return dic
    def update_total_shows_by_city():
        pass
    def search_shows_by_city():
        pass
    def update_updated_at():
        pass
    def __str__(self):
        return f"{self.id} - {self.__city_name} - {self.__total_shows_by_city} - {self.__updated_at}"
class Cities(CRUD):
    @classmethod
    def save(cls):
        with open("json/cities.json", mode="w") as file:
            json.dump([obj.to_json() for obj in cls.objetos], file, default=str, indent=4)
    @classmethod
    def open(cls):
        cls.objetos = []
        try:
            with open("json/cities.json", mode="r") as file:
                text = json.load(file)
            for obj in text:   
                c = City(obj["id"], obj["city_name"], obj["total_shows_by_city"], obj["updated_at"])
            cls.objetos.append(c)
        except FileNotFoundError:
            pass