import json
from models.crud import CRUD
class City:
    def __init__(self, city_id: int, city_name: str, total_shows_by_city: int, updated_at):
        self.__city_id = city_id
        self.__city_name = city_name
        self.__total_shows_by_city = total_shows_by_city
        self.__updated_at = updated_at
    def to_json(self):
        dic = {}
    def __str__(self):
        return f"{self.__city_id} - {self.__city_name} - {self.__total_shows_by_city} - {self.__updated_at}"
class Cities(CRUD):
    @classmethod
    def save(cls):
        with open("cities.json", mode="w") as file:
            json.dump(cls.objetos, file, default = vars)
    @classmethod
    def open(cls):
        cls.objetos = []
        try:
            with open("cities.json", mode="r") as file:
                text = json.load(file)
            for obj in text:   
                c = City(obj["id"], obj["city_name"], obj["total_shows_by_city"], obj["updated_at"])
            cls.objetos.append(c)
        except FileNotFoundError:
            pass