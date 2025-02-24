import json
from models.crud import CRUD
class Show:
    def __init__(self, show_id: int, band_id: int, city_id: int, description_of_show: str, show_date: str, show_time: str, is_virtual: bool, available_tickets: int, ticket_price: str, sold_tickets: int, show_status: str, updated_at):
        self.__show_id = show_id
        self.__band_id = band_id
        self.__city_id = city_id
        self.__description_of_show = description_of_show
        self.__show_date = show_date
        self.__show_time = show_time
        self.__is_virtual = is_virtual
        self.__available_tickets = available_tickets
        self.__ticket_price = ticket_price
        self.__sold_tickets = sold_tickets
        self.__show_status = show_status
        self.__updated_at = updated_at
    def to_json(self):
        dic = {}
    def __str__(self):
        return f"{self.__show_id} - {self.__band_id} - {self.__city_id} - {self.__description_of_show} - {self.__show_date} - {self.__show_time} - {self.__is_virtual} - {self.__available_tickets} - {self.__ticket_price} - {self.__sold_tickets} - {self.__show_status} - {self.__updated_at}"
class Shows(CRUD):
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
                s = Show(obj["show_id"], obj["band_id"], obj["city_id"], obj["description_of_show"], obj["show_date"], obj["show_time"], obj["is_virtual"], obj["available_tickets"], obj["ticket_price"], obj["sold_tickets"], obj["show_status"], obj["updated_at"])
            cls.objetos.append(s)
        except FileNotFoundError:
            pass