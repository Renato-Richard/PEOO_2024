import json
from datetime import datetime, date, time
from models.crud import CRUD
class Show:
    def __init__(self, id: int, band_id: int, city_id: int, description_of_show: str, show_date: date, show_time: time, is_virtual: bool, available_tickets: int, ticket_price: str, sold_tickets: int, show_status: str, updated_at: datetime):
        self.id = id
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
        dic["id"] = self.id
        dic["band_id"] =  self.__band_id
        dic["city_id"] = self.__city_id
        dic["description_of_show"] = self.__description_of_show
        if isinstance(self.__show_date, date):
            dic["show_date"] = self.__show_date.strftime("%d/%m/%Y")
        else:
            dic["show_date"] = self.__show_date
        if isinstance(self.__show_time, time):
            dic["show_time"] = self.__show_time.strftime("%H:%M")
        else:
            dic["show_time"] = self.__show_time
        dic["is_virtual"] = self.__is_virtual
        dic["available_tickets"] = self.__available_tickets
        dic["ticket_price"] = self.__ticket_price
        dic["sold_tickets"] = self.__sold_tickets
        dic["show_status"] = self.__show_status
        if isinstance(self.__updated_at, datetime):
            dic["updated_at"] = self.__updated_at.strftime("%d/%m/%Y %H:%M")
        else:
            dic["updated_at"] = self.__updated_at
        return dic
    def update_available_tickets():
        pass
    def buy_tickets():
        pass
    def update_sold_tickets():
        pass
    def update_updated_at():
        pass
    def __str__(self):
        return f"{self.id} - {self.__band_id} - {self.__city_id} - {self.__description_of_show} - {self.__show_date} - {self.__show_time} - {self.__is_virtual} - {self.__available_tickets} - {self.__ticket_price} - {self.__sold_tickets} - {self.__show_status} - {self.__updated_at}"
class Shows(CRUD):
    @classmethod
    def save(cls):
        with open("json/shows.json", mode="w") as file:
            json.dump([obj.to_json() for obj in cls.objetos], file, default=str, indent=4)
    @classmethod
    def open(cls):
        cls.objetos = []
        try:
            with open("json/shows.json", mode="r") as file:
                text = json.load(file)
            for obj in text:   
                s = Show(obj["id"], obj["band_id"], obj["city_id"], obj["description_of_show"], obj["show_date"], obj["show_time"], obj["is_virtual"], obj["available_tickets"], obj["ticket_price"], obj["sold_tickets"], obj["show_status"], obj["updated_at"])
                cls.objetos.append(s)
        except FileNotFoundError:
            pass